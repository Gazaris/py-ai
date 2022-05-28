import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    if page not in corpus:
        print("No such page in corpus!")
        exit()

    result = dict()
    if len(corpus[page]) > 0:
        random_probability = round((1 - damping_factor) / len(corpus), 4)
        main_probability = round(damping_factor / len(corpus[page]), 4)
        for key in corpus:
            if key in corpus[page]:
                result[key] = main_probability + random_probability
            else:
                result[key] = random_probability
    else:
        equal_probability = round((1 / len(corpus)), 4)
        for key in corpus:
            result[key] = equal_probability
    return result


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Initializing result dictionary
    res = dict()
    for key in corpus:
        res[key] = 0
    # First sample
    random.seed()
    page = random.choice(list(corpus.keys()))
    res[page] += 1
    # All remaining samples
    for i in range(n - 1):
        trans_mod = transition_model(corpus, page, damping_factor)
        page = random.choices(list(trans_mod.keys()), weights=trans_mod.values(), k=1)[0]
        res[page] += 1
    for key in res:
        res[key] = round((res[key] / (n / 100)) / 100, 4)
    return res


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Initializing result dictionary
    N = len(corpus)
    res = dict()
    for key in corpus:
        res[key] = 1 / N
    
    first_con = round((1 - damping_factor) / N, 4)
    unprecise = True
    while unprecise:
        unprecise = False
        # Making a copy of old res to compare new one to
        old_res = res.copy()
        # Updating every page's probability until there's almost no difference
        for key in res:
            # Finding every page that links to the current
            i_pages = list()
            for page in corpus:
                if (page != key and key in corpus[page]) or len(corpus[page]) == 0:
                    i_pages.append(page)
            # Calculating the sum of all probabilities
            prob_sum = 0
            for i in i_pages:
                if len(corpus[i]) == 0:
                    nl = len(res)
                else:
                    nl = len(corpus[i])
                prob_sum += res[i] / nl
            # Calculating new probability for current page
            res[key] = first_con + (damping_factor * prob_sum)
        for key in res:
            if abs(res[key] - old_res[key]) > 0.001:
                unprecise = True
    return res                    


if __name__ == "__main__":
    main()
