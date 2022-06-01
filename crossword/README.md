# crossword

In this project, the AI, given the structure of the crossword and all the possible words it can take on (dictionary), can solve (generate) the puzzle.

## Usage

```
python generate.py data/structure1.txt data/words1.txt output.png
```
The first argument is script name, the second is the path to the txt formatted structure of the puzzle, third is the words set and the last one is the name which you want your solved puzzle picture to have.
You can change dictionaries and structures in pairs, all available ones are provided in *data* directory.

## Output

```
$ python generate.py data/structure1.txt data/words1.txt output.png
██████████████
███████M████R█
█INTELLIGENCE█
█N█████N████S█
█F██LOGIC███O█
█E█████M████L█
█R███SEARCH█V█
███████X████E█
██████████████
```

In the addition to this output in the console, the program will create an image with the solved puzzle.