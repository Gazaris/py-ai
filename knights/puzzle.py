from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Stating that A can only be a Knight or a Knave (not neither and not both)
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # Translating A's saying
    # If A is a Knight his saiyng must be true
    Implication(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Stating that A can only be a Knight or a Knave (not neither and not both)
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # Stating that B can only be a Knight or a Knave (not neither and not both)
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # Translating A's saying
    Implication(AKnight, And(AKnave, BKnave)),
    # If A is a Knive, his saying is false, so B can be only a Knight
    Implication(AKnave, BKnight)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Stating that A can only be a Knight or a Knave (not neither and not both)
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # Stating that B can only be a Knight or a Knave (not neither and not both)
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # Translating A's saying
    Implication(AKnight, And(AKnight, BKnight)),
    # If A is a Knive, his saying is false, so B can be only a Knight
    Implication(AKnave, BKnight),
    # Translating B's saying
    Implication(BKnight, And(BKnight, AKnave))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Stating that A can only be a Knight or a Knave (not neither and not both)
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # Stating that B can only be a Knight or a Knave (not neither and not both)
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # Stating that C can only be a Knight or a Knave (not neither and not both)
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # A's saying (makes no sense to put it in,
    # because A is already either a Knight or a Knave,
    # but also if A happens to be a Knave)
    # Implication(AKnight, Or(AKnight, AKnave)),

    # Instead I will put this in because it is the only way
    # A's words would make sense
    AKnight,
    # B's first saying
    Implication(BKnight, Implication(AKnight, AKnave)),

    # B's second saying
    Implication(BKnight, CKnave),
    Implication(BKnave, CKnight),

    # C's saying
    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
