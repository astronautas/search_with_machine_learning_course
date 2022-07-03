# Week 2 

For classifying product names to categories:

* What precision (P@1) were you able to achieve?
    * 0.6096803148518953

* What fastText parameters did you use?
    * wordNgrams=2, epoch=25, lr=1.0

* How did you transform the product names?
    * Normalized them, as in the tutorial. Lowercased, removed all non-alpha numerics except underscore, trim spaces...

* How did you prune infrequent category labels, and how did that affect your precision?
    * Selected labels with >= 500 items in them. Basically, filtering by thresholded value counts of the label column. Massively improved p@1 to ~0.9. Which makes sense, predicting popular categories is easier. Though, we'll still have to deal with infrequent categories somehow in the prod.

* How did you prune the category tree, and how did that affect your precision?
    * Didn't do that.

For deriving synonyms from content:

* What were the results for your best model in the tokens used for evaluation?
    * I did 2 iterations. Baseline with training loss of 1.3 seemed decent. Removing infrequent words by setting minCount=20 seemed to help a bit, but since it's qualitative evaluation, it's hard to say.

* What fastText parameters did you use?
    * epoch=25, minCount=20

* How did you transform the product names?
    * Default tutorial normalization, as explained above.

For integrating synonyms with search:

* How did you transform the product names (if different than previously)?
    * Not really, the same way.

* What threshold score did you use?
    * 0.75

* Were you able to find the additional results by matching synonyms?
    * earbuds - 2.5k with synonyms vs. 1.2k without.
    * nespresso - 8 with synonyms, 8 without. The root cause is that nespresso is not among 1k top words. Didn't add it manually to the synonyms, but it's one of the solutions.
    * dslr - 3.8k with synonyms, 2.8k without. A solid retrieval improvement.