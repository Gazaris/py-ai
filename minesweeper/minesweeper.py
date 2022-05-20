import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        if len(self.cells) == self.count:
            return self.cells
        if self.count == 0:
            return {}

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if len(self.cells) == self.count:
            return {}
        if self.count == 0:
            return self.cells

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        self.moves_made.add(cell)

        self.mark_safe(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)
        
        new_sentence = Sentence(set(), count)
        # Going through cell's neighbors
        for i in range(cell[0] - 1, cell[0] + 2):
            if i < 0 or i >= self.height:
                continue
            for j in range(cell[1] - 1, cell[1] + 2):
                if j < 0 or j >= self.width:
                    continue
                # Ignore if it's the cell
                if (i, j) == cell:
                    continue
                """ 
                Adding cell to the sentence if not certain
                if it's a mine or a safe one
                """
                if (i, j) not in self.safes:
                    if (i, j) in self.mines:
                        new_sentence.count -= 1
                    else:
                        new_sentence.cells.add((i, j))
        if count > 0 and len(new_sentence.cells) > 0:
            print("Adding new sentence:", new_sentence)
            print("from cell", cell)
            self.knowledge.append(new_sentence)
        elif count == len(new_sentence.cells):
            if count == 0:
                print("No cells to mark.")
            else:
                print("Marking as mines:", new_sentence.cells)
                print("from cell", cell)
                for c in new_sentence.cells:
                    self.mark_mine(c)
        else:
            print("Marking as safes:", new_sentence.cells)
            print("from cell", cell)
            for c in new_sentence.cells:
                self.mark_safe(c)

        # Checking every sentence in knowledge base in a loop until there's nothing to conclude
        changed = True
        pass_num = 0
        while changed:
            pass_num += 1
            print("deduct pass", pass_num)
            print("knowledge: [")
            for sent in self.knowledge:
                print(sent)
            print("]")
            if pass_num >= 50:
                print("something went wrong...")
                exit()
            changed = False
            if len(self.knowledge) > 1:
                listi = range(len(self.knowledge) - 1) # [0:-1]
                listj = range(1, len(self.knowledge)) # [1:]
                breaki = False
                for i in listi:
                    if breaki:
                        break
                    for j in listj[i:]:
                        """
                        Actually checking the sentences for duplicates
                        and if something can be concluded from any pair
                        """
                        if self.knowledge[i].cells.issubset(self.knowledge[j].cells):
                            # Duplicates check
                            if self.knowledge[i] == self.knowledge[j]:
                                del self.knowledge[j]
                            # New sentence from j check
                            else:
                                # Removing recurring cells
                                for el in self.knowledge[i].cells:
                                    if el in self.knowledge[j].cells:
                                        self.knowledge[j].cells.remove(el)
                                # Changing mines num
                                self.knowledge[j].count -= self.knowledge[i].count
                            breaki = True
                            changed = True
                            break
                        elif self.knowledge[j].cells.issubset(self.knowledge[i].cells):
                            # Removing recurring cells
                            for el in self.knowledge[j].cells:
                                if el in self.knowledge[i].cells:
                                    self.knowledge[i].cells.remove(el)
                            # Changing mines num
                            self.knowledge[i].count -= self.knowledge[j].count
                            breaki = True
                            changed = True
                            break
            else:
                break

        # Clear the list from all sentences without mines or only with mines
        changed = True
        check_start = 0 # for not checking the ones sentences that were already checked
        pass_num = 0
        while changed:
            changed = False
            pass_num += 1
            print("clear pass", pass_num)
            print("knowledge: [")
            for sent in self.knowledge:
                print(sent)
            print("]")
            if pass_num >= 100:
                print("something went wrong...")
                exit()
            if check_start < len(self.knowledge):
                for snum in range(check_start, len(self.knowledge)):
                    print("checking", self.knowledge[snum])
                    if self.knowledge[snum].count == 0:
                        mark = self.knowledge[snum].cells.copy()
                        for c in mark:
                            self.mark_safe(c)
                        del self.knowledge[snum]
                        check_start = snum
                        changed = True
                        break
                    elif self.knowledge[snum].count == len(self.knowledge[snum].cells):
                        mark = self.knowledge[snum].cells.copy()
                        for c in mark:
                            self.mark_mine(c)
                        del self.knowledge[snum]
                        check_start = snum
                        changed = True
                        break

        print("end knowledge: [")
        for sent in self.knowledge:
            print(sent)
        print("]")

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        for safe_one in self.safes:
            if safe_one not in self.moves_made:
                self.moves_made.add(safe_one)
                print(safe_one)
                return safe_one
        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """

        if len(self.moves_made) == (self.height * self.width) - len(self.mines):    
            return None
        random.seed()
        while True:
            checking_cell = (random.randrange(self.height), random.randrange(self.width))
            if checking_cell not in self.mines and \
               checking_cell not in self.moves_made:
               print(checking_cell)
               return checking_cell

