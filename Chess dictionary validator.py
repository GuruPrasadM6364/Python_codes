print('Name: Guru Prasad M\nUSN: 1AY24AI037 \nSection: M\n ')

def is_valid_chess_board(board):
    valid_positions = [f"{file}{rank}" for file in "abcdefgh" for rank in "12345678"]
    valid_pieces = {
        "wking", "wqueen", "wrook", "wbishop", "wknight", "wpawn",
        "bking", "bqueen", "brook", "bbishop", "bknight", "bpawn"
    }

    white_king_count = 0
    black_king_count = 0
    white_pieces = 0
    black_pieces = 0

    for position, piece in board.items():
        if position not in valid_positions:
            print(f"Invalid position: {position}")
            return False

        if piece not in valid_pieces:
            print(f"Invalid piece: {piece}")
            return False

        if piece == "wking":
            white_king_count += 1
        elif piece == "bking":
            black_king_count += 1
        if piece.startswith("w"):
            white_pieces += 1
        elif piece.startswith("b"):
            black_pieces += 1

    if white_king_count != 1 or black_king_count != 1:
        print("There must be exactly one white king and one black king.")
        return False

    if white_pieces > 16 or black_pieces > 16:
        print("Too many pieces for one side.")
        return False

    return True

chess_board = {
    'e1': 'wking',
    'e8': 'bking',
    'd1': 'wqueen',
    'd8': 'bqueen',
    'a1': 'wrook',
    'h1': 'wrook',
    'a8': 'brook',
    'h8': 'brook',
    'b1': 'wknight',
    'g1': 'wknight',
    'b8': 'bknight',
    'g8': 'bknight',
    'c1': 'wbishop',
    'f1': 'wbishop',
         'c8': 'bbishop',
    'f8': 'bbishop',
    'a2': 'wpawn',
    'b2': 'wpawn',
    'c2': 'wpawn',
    'd2': 'wpawn',
    'e2': 'wpawn',
    'f2': 'wpawn',
    'g2': 'wpawn',
    'h2': 'wpawn',
    'a7': 'bpawn',
    'b7': 'bpawn',
    'c7': 'bpawn',
    'd7': 'bpawn',
    'e7': 'bpawn',
    'f7': 'bpawn',
    'g7': 'bpawn',
    'h7': 'bpawn',
}

if is_valid_chess_board(chess_board):
    print("The chess board is valid.")
else:
    print("The chess board is invalid.")
