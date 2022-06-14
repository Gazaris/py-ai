# Question

In this project I implemented an AI answers query questions.

## Installing dependencies

```
pip3 install -r requirements.txt
python reqs.py
```

## Usage

```
pyton questions.py corpus
```

```corpus``` is a directory with all the documents that will be analyzed. The corpus of the documents can be freely modified or updated to get different results or make the AI be able to answer many more questions. 

## Output

```
$ python questions.py corpus
Query: What are the types of supervised learning?
Types of supervised learning algorithms include Active learning , classification and regression.

$ python questions.py corpus
Query: When was Python 3.0 released?
Python 3.0 was released on 3 December 2008.

$ python questions.py corpus
Query: How do neurons connect in a neural network?
Neurons of one layer connect only to neurons of the immediately preceding and immediately following layers.
```

After launch the user will be prompted to enter a question about some information in the corpus and AI will try to find the most related answer in the corpus documents. Note that after launch the AI can not output anything for some time, that's because it needs time to read all of the corpus documents.
