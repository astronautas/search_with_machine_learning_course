import os
import argparse
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import csv

# Useful if you want to perform stemming.
import nltk
from tokenizers import normalizers
from tokenizers.normalizers import BertNormalizer
import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem import PorterStemmer, SnowballStemmer
from tqdm import tqdm
import string
import pprint

pp = pprint.PrettyPrinter(indent=4)

# progressbar
tqdm.pandas()

threshold = 1000

snowball = nltk.stem.SnowballStemmer("english")
hf_normalizer = normalizers.Sequence([BertNormalizer()])


downcaser = lambda sentence: hf_normalizer.normalize_str(sentence)
normalizer = lambda sentence: sentence.translate(
    str.maketrans("", "", string.punctuation)
)
stemmer = lambda sentence: " ".join(
    [snowball.stem(word) for word in word_tokenize(sentence)]
)
pipeline = lambda sentence: downcaser(stemmer(normalizer(sentence)))

categories_file_name = r"/workspace/datasets/product_data/categories/categories_0001_abcat0010000_to_pcmcat99300050000.xml"

queries_file_name = r"/workspace/datasets/train.csv"
output_file_name = (
    f"/workspace/datasets/fasttext/labeled_queries_{threshold}_no_norm.txt"
)

parser = argparse.ArgumentParser(description="Process arguments.")
general = parser.add_argument_group("general")
general.add_argument(
    "--min_queries",
    default=1,
    help="The minimum number of queries per category label (default is 1)",
)
general.add_argument("--output", default=output_file_name, help="the file to output to")

args = parser.parse_args()
output_file_name = args.output

if args.min_queries:
    min_queries = int(args.min_queries)

# The root category, named Best Buy with id cat00000, doesn't have a parent.
root_category_id = "cat00000"

tree = ET.parse(categories_file_name)
root = tree.getroot()

# Parse the category XML file to map each category id to its parent category id in a dataframe.
categories = []
parents = []
for child in root:
    id = child.find("id").text
    cat_path = child.find("path")
    cat_path_ids = [cat.find("id").text for cat in cat_path]
    leaf_id = cat_path_ids[-1]
    if leaf_id != root_category_id:
        categories.append(leaf_id)
        parents.append(cat_path_ids[-2])
parents_df = pd.DataFrame(
    list(zip(categories, parents)), columns=["category", "parent"]
)
cat_parent_map = dict(zip(parents_df.category, parents_df.parent))

parents_df.to_csv("/tmp/parents_df_dev.csv")

# Read the training data into pandas, only keeping queries with non-root categories in our category tree.
df = pd.read_csv(queries_file_name)[["category", "query"]]
df = df[df["category"].isin(categories)]

# dev sampling
# df = df.sample(100_000)

# IMPLEMENT ME: Convert queries to lowercase, and optionally implement other normalization, like stemming.
# Lowercasing, punctuation striping, stemming
# df["query"] = df["query"].progress_apply(lambda query: pipeline(query))
# df = df[df["query"] != ""]  # some queries after normalization are lost :/ but <1%

# IMPLEMENT ME: Roll up categories to ancestors to satisfy the minimum number of queries per category.
while True:
    # Unroll
    query_counts = (
        df.groupby("category")
        .agg(num_queries=("query", "count"))
        .reset_index()
        .sort_values("num_queries", ascending=False)
        .assign(
            is_below_threshold_flag=lambda dframe: dframe["num_queries"] < threshold
        )
    )

    # Start from the bottom
    cats_to_unroll = set(
        query_counts[query_counts["is_below_threshold_flag"] == True][
            "category"
        ].tolist()
    )

    if not cats_to_unroll:
        break

    # If a category has no parent but needs to be rolledup, just filter out all occurences
    cats_to_filter_out = cats_to_unroll.difference(set(cat_parent_map.keys()))

    if cats_to_filter_out:
        df = df[~df["category"].isin(cats_to_filter_out)]

    df["category"] = df["category"].apply(
        lambda cat: cat if cat not in cats_to_unroll else cat_parent_map[cat]
    )

# Create labels in fastText format.
df["label"] = "__label__" + df["category"]


# Output labeled query data as a space-separated file, making sure that every category is in the taxonomy.
df = df[df["category"].isin(categories)]

print(len(df["category"].value_counts()))
pp.pprint(df["category"].value_counts())

df["output"] = df["label"] + " " + df["query"]
df[["output"]].to_csv(
    output_file_name,
    header=False,
    sep="|",
    escapechar="\\",
    quoting=csv.QUOTE_NONE,
    index=False,
)
