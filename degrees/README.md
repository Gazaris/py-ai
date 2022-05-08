# Degrees
This is a project that determines how many “degrees of separation” apart two actors are.

## Usage
```
python degrees.py [directory]
```
If directory is not specified, ```large``` is chosen.
The project is also provided with ```small``` directory option for tests rather than actual use.

## Output example
```
$ python degrees.py large
Loading data...
Data loaded.
Name: Emma Watson
Name: Jennifer Lawrence
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
```

After launch the program will prompt the user to enter first name and then the second name.
If was entered a name, that several people have, user would be prompted to clarify.

Then, the program will output the amount of degrees of separation the two entered actors have.

And finally, output each degree between actors as a string.
