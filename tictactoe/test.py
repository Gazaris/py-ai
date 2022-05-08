from tictactoe import minimax, player, terminal, actions, X, O, EMPTY


def main():
    board = [[X, O, X],
             [O, X, X],
             [O, O, EMPTY]]
    
    print(minimax(board))
    # print(terminal(board))
    

if __name__ == "__main__":
    main()
