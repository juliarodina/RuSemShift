# RuSemShift
**RuSemShift** is a large-scale human-annotated dataset of diachronic semantic shifts in Russian.
Lexical semantic change is a process when a word changes its meaning over time. 
This dataset provides information about relative degree of historical semantic change for dozens of Russian words. 
It is based on sentence contexts  extracted from the [Russian National Corpus](https://rusvectores.org/static/corpora/).

This is the first semantic change dataset for Russian created in a large-scale crowd-sourcing annotation effort. 
The annotation followed the [DURel framework](https://www.aclweb.org/anthology/N18-2027/),
which makes **RuSemShift** fully compatible with [semantic change datasets developed for other languages](https://www.aclweb.org/anthology/2020.semeval-1.1/).
It can be used to evaluate automatic systems for semantic change detection.
Please check our paper for more details:

_Julia Rodina and Andrey Kutuzov. 
[RuSemShift: a dataset of historical lexical semantic changes in Russian](https://www.aclweb.org/anthology/2020.coling-main.90/)
Proceedings of the 28th International Conference on Computational Linguistics (COLING 2020).
Association for Computational Linguistics, Barcelona, Spain (2020)._

**RuSemShift** consists of two subsets each covering a specific pair of time periods:
- **RuSemShift_1**: pre-Soviet and Soviet times (1682-1916 -> 1918-1990)
- **RuSemShift_2**: Soviet and post-Soviet times (1918-1990 -> 1991-2016)

See the description of each subset in their respective directories.

# License
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />
<span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Dataset" property="dct:title" rel="dct:type">RuSemShift</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/juliarodina/RuSemShift" property="cc:attributionName" rel="cc:attributionURL">Julia Rodina and Andrey Kutuzov</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

# Acknowledgments
The creation of **RuSemShift** was supported by the Russian Science Foundation grant 20-18-00206.
