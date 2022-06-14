import math
import nltk
import sys
import os
import string

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    
    # Checking if entered string was a directory
    if not os.path.isdir(directory):
        raise Exception("No such directory!")

    # Getting all txt files contents
    diction = dict()
    for filename in os.listdir(directory):
        if os.path.splitext(filename)[1] == ".txt":
            with open(os.path.join(directory, filename), "r") as f:
                diction[filename] = f.read()
    
    return diction


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    
    # Separate the sentence into a list of words
    words = nltk.tokenize.word_tokenize(document)
    
    # Removing all words that don't contain any letters
    words = [w for w in words if any(c.isalpha() for c in w)]

    # Converting every words to lowercase
    words = [w.lower() for w in words]

    # Removing punctuation from words
    for w in words:
        for c in w:
            if c in string.punctuation:
                w = w.replace(c, "")
    
    # Removing stopwords and returning the result
    return [w for w in words if not w in nltk.corpus.stopwords.words("english")] 


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    idfs = dict()
    words = sum(documents.values(), [])
    for word in words:
        if word not in idfs:
            f = sum(word in documents[d] for d in documents)
            idfs[word] = math.log(len(documents) / f)
    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    # All in one string because why not
    # file_scores = { file: sum(files[file].count(word) * idfs[word] for word in query if word in files[file]) for file in files}

    file_scores = dict()
    for file in files:
        score = 0
        for word in query:
            if word in files[file]:
                score += files[file].count(word) * idfs[word]
        file_scores[file] = score
    
    # Returning a list of all filenames, sorted by their score in descending order
    filenames = list(files.keys())
    filenames.sort(key=lambda f: file_scores[f], reverse=True)
    return filenames[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    s_scores = dict()
    s = list(sentences.keys())
    for sent in sentences:
        score = sum(idfs[word] for word in query if word in sentences[sent])
        s_scores[sent] = score
    s.sort(key=lambda sentence: s_scores[sentence], reverse=True)
    res = s[:n]
    if s_scores[res[-1]] == s_scores[s[n]]:
        first = 1 / len(res[-1]) * sum(word in res[-1] for word in query)
        second = 1 / len(s[n]) * sum(word in s[n] for word in query)
        if first < second:
            res[-1] = s[n]
    return res


if __name__ == "__main__":
    main()
