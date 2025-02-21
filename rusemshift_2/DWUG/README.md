# RuSemShift-2: Test data set for Diachronic Word Usage Graphs for Russian

### Type

Dataset

### Authors

Julia Rodina and Andrey Kutuzov

### Description

This data collection contains diachronic Word Usage Graphs (WUGs) for Russian. 
Find a description of the data format, code to process the data and further datasets on the [WUGsite](https://www.ims.uni-stuttgart.de/data/wugs).

Important notes:

This dataset was annotated in a crowd-working effort with hundreds of annotators.
Therefore, pairwise inter-rater agreement scores are meaningless and are not provided.
This also means that the same annotator name may correspond to a different person for two different use pairs. 
E.g. the judgment of annotator1 for two different use pairs could be done by a different person.

- Version 2.0.0 of the data set was an update of the original RuSemShift data set. The annotated data remains the same, but the following points differ:
  * we change the data format to be compatible with [WUG data sets](https://www.ims.uni-stuttgart.de/data/wugs),
  * missing target word indices are inferred with [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/),
  * punctuation at the beginning or end of target words are excluded from target word indices,
  * change scores are calculated with the code from the [WUG repository](https://github.com/Garrafao/WUGs). This code first aggregates judgments of use pairs with the median over all annotators and then averages all the scores for the measures EARLIER, LATER, COMPARE. Hence, the change scores slightly differ from the ones in the original dataset.

As described in the paper below, the data was further optimized for the CoMeDi shared task. Version 2.0.1 reflects some of the changes described in the paper, i.e., correction of target word and target sentence indices, plus minor additional changes.

Please find more information on the provided data in the papers referenced below.
 
Version: 2.0.1, 11.1.2025. WUG version. Correct target word and target sentence indices. Map floats to integers in judgments. Update plots. Add compare plots.

### Reference

Julia Rodina and Andrey Kutuzov. [RuSemShift: a dataset of historical lexical semantic changes in Russian](https://www.aclweb.org/anthology/2020.coling-main.90/), in Proceedings of the 28th International Conference on Computational Linguistics (COLING 2020). Association for Computational Linguistics, Barcelona, Spain (2020).

Dominik Schlechtweg, Tejaswi Choppa, Wei Zhao, Michael Roth. 2025. [The CoMeDi Shared Task: Median Judgment Classification & Mean Disagreement Ranking with Ordinal Word-in-Context Judgments](https://aclanthology.org/2025.comedi-1.4/). In Proceedings of the 1st Workshop on Context and Meaning--Navigating Disagreements in NLP Annotations.
