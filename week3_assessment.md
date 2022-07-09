## For query classification:

How many unique categories did you see in your rolled up training data when you set the minimum number of queries per category to 1000? To 10000?
* 387 for 1k, 69 for 10k. I did try implementing progressive rollup, as suggested in the exercise, but it was too slow... Hence, I iteratively rolled-up all categories below the threshold in batches.

What were the best values you achieved for R@1, R@3, and R@5? You should have tried at least a few different models, varying the minimum number of queries per category, as well as trying different fastText parameters or query normalization. Report at least 2 of your runs.

| Model      | R@1 | R@3 | R@5 |
| ----------- | ----------- |  ----------- |  ----------- |
| Baseline    | 0.485       | 0.637 | 0.703 |
| epoch=10, wordNGrams2   | 0.512        | 0.693 | 0.755 |
| Without normalization | 0.446 | 0.596 | 0.657 |
| 10k cutoff | 0.584 | 0.775 | 0.833 |

Everything makes sense :).

## For integrating query classification with search:

Give 2 or 3 examples of queries where you saw a dramatic positive change in the results because of filtering. Make sure to include the classifier output for those queries.

### Samsung Galaxy Tab
```
samsung galaxy tab

Predicted: pcmcat209000050008:0.5930028557777405
```

Without the predicted categoryLeaf filter, the results are mostly samsung accessories. Filtering by the predicted category yields mostly Samsung Galaxy Tab devices, much more relevant to the query :)

### iPhone 4s

```
iphone 4s
Predicted: pcmcat209400050001:0.4823188781738281
```

Once again, without the filters, mostly accessories are returned. With the filters, proper iPhone devices are among the results.

Give 2 or 3 examples of queries where filtering hurt the results, either because the classifier was wrong or for some other reason. Again, include the classifier output for those queries.

### Apple iPhone

```
apple iphone
Predicted: cat02015:0.022678811103105545
```

Reduced the thresholded to see what happens. If we filter by the predicted category, the results are... pure trash. Mostly irrelevant CDs, food making tools, nothing related to iphones. Without the predicted filtering, there are at least some decent iphone accessories.

```
apple mobile phone
Predicted: pcmcat209400050001:0.06856498122215271
```
Better than the previous one, but still less relevant than by not filtering by the predicted category.

Classifier confidence matters!


