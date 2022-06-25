### tuning week 1

pre-ranking w: 0, re-score weight: 2

baseline

```jsx
Simple MRR is 0.311
LTR Simple MRR is 0.144
Hand tuned MRR is 0.483
LTR Hand Tuned MRR is 0.155

Simple p@10 is 0.113
LTR simple p@10 is 0.062
Hand tuned p@10 is 0.176
LTR hand tuned p@10 is 0.068
Simple better: 786      LTR_Simple Better: 591  Equal: 10
HT better: 902  LTR_HT Better: 583      Equal: 11
```

name_match_phrase with slop (more advanced matching with analysis)

```jsx
Simple MRR is 0.329
LTR Simple MRR is 0.202
Hand tuned MRR is 0.467
LTR Hand Tuned MRR is 0.207

Simple p@10 is 0.143
LTR simple p@10 is 0.075
Hand tuned p@10 is 0.155
LTR hand tuned p@10 is 0.082
Simple better: 717      LTR_Simple Better: 632  Equal: 15
HT better: 798  LTR_HT Better: 615      Equal: 16
```

with customer reviews

```jsx
Simple MRR is 0.334
LTR Simple MRR is 0.448
Hand tuned MRR is 0.437
LTR Hand Tuned MRR is 0.447

Simple p@10 is 0.141
LTR simple p@10 is 0.199
Hand tuned p@10 is 0.219
LTR hand tuned p@10 is 0.204
Simple better: 731      LTR_Simple Better: 892  Equal: 13
HT better: 877  LTR_HT Better: 826      Equal: 21
Saving Better/Equal analysis to /workspace/ltr_output/analysis
```

with descriptions

```jsx
Simple MRR is 0.300
LTR Simple MRR is 0.501
Hand tuned MRR is 0.449
LTR Hand Tuned MRR is 0.485

Simple p@10 is 0.119
LTR simple p@10 is 0.190
Hand tuned p@10 is 0.195
LTR hand tuned p@10 is 0.200
Simple better: 572      LTR_Simple Better: 801  Equal: 12
HT better: 751  LTR_HT Better: 795      Equal: 19
Saving Better/Equal analysis to /workspace/ltr_output/analysis
```