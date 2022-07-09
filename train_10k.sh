shuf /workspace/datasets/fasttext/labeled_queries_10000.txt > /workspace/datasets/fasttext/shuffled_labeled_queries_10k.txt
wc -l /workspace/datasets/fasttext/shuffled_labeled_queries_10k.txt

head -50000 /workspace/datasets/fasttext/shuffled_labeled_queries_10k.txt > shuffled_labeled_queries_10k.train
tail -10000 /workspace/datasets/fasttext/shuffled_labeled_queries_10k.txt > shuffled_labeled_queries_10k.test

wc -l shuffled_labeled_queries_10k.train
wc -l shuffled_labeled_queries_10k.test

~/fastText-0.9.2/fasttext supervised -input shuffled_labeled_queries_10k.train -output query-classifier-10k

~/fastText-0.9.2/fasttext test query-classifier-10k.bin shuffled_labeled_queries_10k.test 1
~/fastText-0.9.2/fasttext test query-classifier-10k.bin shuffled_labeled_queries_10k.test 3
~/fastText-0.9.2/fasttext test query-classifier-10k.bin shuffled_labeled_queries_10k.test 5