# Minesweeper
In this project I implemented an AI that can make moves based on the knowledge of the field (for example where mines are definetely are or which cells are definetely safe).

## Installing dependencies
```
pip3 install -r requirements.txt 
```

## Usage
```
pyton puzzle.py
```

## Output
After launch, a window with a minesweeper field should open up. After that the player can make a move themself or press a button so that AI makes a move for them. AI does not mark mines but avoids making a move on the places where mines definitely are. Sometimes AI would make a random move when it doesn't have enough information about which move would be safe to make. 
