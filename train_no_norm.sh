shuf /workspace/datasets/fasttext/labeled_queries_1000_no_norm.txt > /workspace/datasets/fasttext/shuffled_labeled_queries_1k_no_norm.txt
wc -l /workspace/datasets/fasttext/shuffled_labeled_queries_1k_no_norm.txt

head -50000 /workspace/datasets/fasttext/shuffled_labeled_queries_1k_no_norm.txt > shuffled_labeled_queries_1k_no_norm.train
tail -10000 /workspace/datasets/fasttext/shuffled_labeled_queries_1k_no_norm.txt > shuffled_labeled_queries_1k_no_norm.test

wc -l shuffled_labeled_queries_1k_no_norm.train
wc -l shuffled_labeled_queries_1k_no_norm.test

~/fastText-0.9.2/fasttext supervised -input shuffled_labeled_queries_1k_no_norm.train -output query-classifier-1k_no_norm

~/fastText-0.9.2/fasttext test query-classifier-1k_no_norm.bin shuffled_labeled_queries_1k_no_norm.test 1
~/fastText-0.9.2/fasttext test query-classifier-1k_no_norm.bin shuffled_labeled_queries_1k_no_norm.test 3
~/fastText-0.9.2/fasttext test query-classifier-1k_no_norm.bin shuffled_labeled_queries_1k_no_norm.test 5