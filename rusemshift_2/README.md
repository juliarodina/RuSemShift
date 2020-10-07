**RuSemShift_2** features semantic change scores of Russian words between Soviet (1918-1990)
 and post-Soviet (1991-2017) time periods.

# Files
- `binary.csv`: word list before annotation (with part of speech tags). 
The 'GROUND_TRUTH' column contains binary labels (changed/not changed) taken from prior linguistic work.
- `raw_annotations.tsv`: list of sentences presented to annotators and their judgments (before averaging).
- `testset.tsv`: the **RuSemShift_2** dataset itself, with averaged semantic relatedness measures (see below)
- `testset_filtered.tsv`: the filtered version of the dataset. 
Words with inter-rater agreement less than 0.2 are excluded. 
We recommend to use this version, as it more or less guarantees the annotation consistency.

# Annotation
The original target word list was borrowed from the New Words and Meanings dictionary by Burtseva at al. 
It consists of 42 words which acquired a new sense or lost an old one: 35 nouns and 7 adjectives. 

We added 27 random fillers and the resulting set of 69 words from annotated via crowdsourcing.
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

