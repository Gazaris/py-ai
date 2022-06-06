# Nim

AI that learns to play nim game with itself and then plays it with the user.

## Usage

```
python play.py
```

## Output example

```
$ python play.py
Playing training game 1
Playing training game 2
Playing training game 3
...
Playing training game 9999
Playing training game 10000
Done training

Piles:
Pile 0: 1
Pile 1: 3
Pile 2: 5
Pile 3: 7

AI's Turn
AI chose to take 1 from pile 2.
```

After launch the AI will start playing nim with itself, learning from experience. After it's done playing with itself, the program will output state of piles in the current game session and a move that AI made. After that the player makes a move and the moves alternate until the game is over and someone has won the game.