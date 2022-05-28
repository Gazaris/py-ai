import random
from pagerank import DAMPING, SAMPLES, transition_model, sample_pagerank, iterate_pagerank

corpus = {"1": {"2", "3"}, "2": {"3"}, "3": {"2"}}
# res = sample_pagerank(corpus, DAMPING, SAMPLES)
yes = corpus.copy()
yes["1"] = {"3"}
print(yes)
