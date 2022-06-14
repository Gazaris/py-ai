# Parser

In this project I implemented an AI that parces sentences extracting noun phrases.

## Installing dependencies

```
pip3 install -r requirements.txt
python reqs.py
```

## Usage

```
pyton parser.py [filename]
```

## Output

```
$python .\parser.py .\sentences\1.txt
        S     
        |
        MS
   _____|___
  NP        |
  |         |
  NA        VP
  |         |
  N         V
  |         |
holmes     sat

Noun Phrase Chunks
holmes
```

After launch the AI will prompt the user to enter a sentence and after pressing enter the sentence will be processed and the parced sentence tree with all extracted noun phrases will be written into the console. If a filename was specified, the program will take a sentence from it instead of prompting the user to enter a sentence. Keep in mind that the program will be able to process only words it has and in the meaning they written inside the **TERMINALS** variable. For example, the word "*walk*" is present in the program only as a noun and not as a verb.
