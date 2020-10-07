**RuSemShift_1** features semantic change scores of Russian words between pre-Soviet (1682-1916) 
and Soviet (1918-1990) time periods.

# Files
- `binary.csv`: word list before annotation (with part of speech tags). 
The 'GROUND_TRUTH' column contains binary labels (changed/not changed) taken from prior linguistic work.
- `raw_annotations.tsv`: list of sentences presented to annotators and their judgments (before averaging).
- `testset.tsv`: the **RuSemShift_1** dataset itself, with averaged semantic relatedness measures (see below)
- `testset_filtered.tsv`: the filtered version of the dataset. 
Words with inter-rater agreement less than 0.2 are excluded. 
We recommend to use this version, as it more or less guarantees the annotation consistency.

# Annotation
The original target word list was borrowed from ["Two centuries in two thousand words: Neural embedding models in detecting diachronic lexical changes"](https://www.academia.edu/31065097/Two_centuries_in_two_thousand_words_Neural_embedding_models_in_detecting_diachronic_lexical_changes). 
It consists of 43 words which acquired a new sense or lost an old one: 38 nouns and 5 adjectives. 

We added 28 random fillers and the resulting set of 71 words from annotated via crowdsourcing.
The annotators were asked to estimate the relatedness between senses of a target word in two different sentences according to the following grade schema:
- 0: Cannot decide
- 1: Unrelated 
- 2: Distantly related
- 3: Closely Related
- 4: Identical

# Relatedness measures
The resulting scores were then averaged to produce four measures of semantic relatedness. 
They follow the [DURel framework](https://www.aclweb.org/anthology/N18-2027/):
- EARLIER: mean relatedness within the first time period (pre-Soviet)
- LATER: mean relatedness within the second time period (Soviet)
- **COMPARE**: mean relatedness between sentences from two different time periods
- **∆LATER** (delta later): difference between EARLIER and LATER

The last two measures can actually be used as the degrees of semantic change.

