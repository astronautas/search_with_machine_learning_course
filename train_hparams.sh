shuf /workspace/datasets/fasttext/labeled_queries_1000.txt > /workspace/datasets/fasttext/shuffled_labeled_queries_1k.txt
wc -l /workspace/datasets/fasttext/shuffled_labeled_queries_1k.txt

head -50000 /workspace/datasets/fasttext/shuffled_labeled_queries_1k.txt > shuffled_labeled_queries_1k.train
tail -10000 /workspace/datasets/fasttext/shuffled_labeled_queries_1k.txt > shuffled_labeled_queries_1k.test

wc -l shuffled_labeled_queries_1k.train
wc -l shuffled_labeled_queries_1k.test

~/fastText-0.9.2/fasttext supervised -input shuffled_labeled_queries_1k.train -output query-classifier-1k-hparams -epoch 10 -wordNgrams 2

~/fastText-0.9.2/fasttext test query-classifier-1k-hparams.bin shuffled_labeled_queries_1k.test 1
~/fastText-0.9.2/fasttext test query-classifier-1k-hparams.bin shuffled_labeled_queries_1k.test 3
~/fastText-0.9.2/fasttext test query-classifier-1k-hparams.bin shuffled_labeled_queries_1k.test 5