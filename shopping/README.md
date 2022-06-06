# Shopping

AI that predicts whether online shopping customers will complete a purchase given a set of data.

## Installing dependencies

```
pip3 install scikit-learn
```

## Usage

```
python shopping.py shopping.csv
```

## Output example

```
$ python shopping.py shopping.csv
Correct: 4088
Incorrect: 844
True Positive Rate: 41.02%
True Negative Rate: 90.55%
```

After launch the AI will output a number of correct and incorrect guesses and then True positive rate (proportion of actual positive labels that were accurately identified) and True negative rate (same but with negative labels).