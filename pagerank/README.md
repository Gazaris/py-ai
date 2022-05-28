# pagerank

In this project I created an AI that determines the probability of some hypothetical web surfer getting on a page from the set based on links to that page on other pages.

## Usage

```
python pagerank.py corpus
```
Instead of corpus, choose one of the provided folders.

## Output

After launch the program will scan the directory for html pages and detect any links to other pages, creating a dictionary. AI then takes that dictionary and calculates the probability of surfer happening to be on every page with two algorithms. The output of those algorithms then outputted in the console.
