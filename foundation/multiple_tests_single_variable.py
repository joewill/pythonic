from enum import Enum


def main():
    d_text = input("Which direction [n,e,s,w,ne,se,sw,nw]?")
    m = Moves.parse(d_text)

    if m is None:
        print("That's not a move!")
        return

    print(m)

    # **************Less pythonic
    # if m == Moves.North or m == Moves.East or m == Moves.Soutth or m == Moves.West:
    #     print("That's a direct move")
    # else:
    #     print("That's a diagonal move")

    # **************More pythonic
    # if m in {Moves.North, Moves.East, Moves.South, Moves.West}:
    #     print("That's a direct move")
    # else:
    #     print("That's a diagonal move")

    # **************More pythonic, tiny bit faster
    direct_moves = {Moves.North, Moves.East, Moves.South, Moves.West}
    if m in direct_moves:
        print("That's a direct move")
    else:
        print("That's a diagonal move")


class Moves(Enum):
    North = 1
    East = 2
    South = 3
    West = 4
    NorthEast = 5
    SouthEast = 6
    SouthWest = 7
    NorthWest = 8

    @staticmethod
    def parse(text: str):
        if not text:
            return None

        text = text.strip().lower()

        if text == 'n':
            return Moves.North
        if text == 'e':
            return Moves.East
        if text == 's':
            return Moves.South
        if text == 'w':
            return Moves.West

        if text == 'ne':
            return Moves.NorthEast
        if text == 'se':
            return Moves.SouthEast
        if text == 'sw':
            return Moves.SouthWest
        if text == 'nw':
            return Moves.NorthWest


if __name__ == '__main__':
    main()
