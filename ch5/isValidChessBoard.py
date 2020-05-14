def isValidChessBoard(board):
    if type(board) != dict or len(board) > 32:
        return False
    for k in list(board.keys()): # Check for valid tiles
        if len(k) > 2:
            return False
        try:
            row = int(k[0])
        except:
            return False
        if not 1 <= row <= 8:
            return False
        if k[1] not in 'abcdefgh':
            return False
    whitePieces = {'pieces': 0, 'pawns': 0, 'kings': 0}
    blackPieces = {'pieces': 0, 'pawns': 0, 'kings': 0}
    for v in list(board.values()): # Check for valid pieces
        if v[0] == 'w':
            whitePieces['pieces'] += 1
            if 'pawn' in v:
                whitePieces['pawns'] += 1
            elif 'king' in v:
                whitePieces['kings'] += 1
        elif v[0] == 'b':
            blackPieces['pieces'] += 1
            if 'pawn' in v:
                blackPieces['pawns'] += 1
            elif 'king' in v:
                blackPieces['kings'] += 1
        else:
            return False
        if whitePieces['pieces'] > 16 or blackPieces['pieces'] > 16: # Check quantities
            return False
        if whitePieces['pawns'] > 8 or blackPieces['pawns'] > 8:
            return False
        if whitePieces['kings'] > 1 or blackPieces['kings'] > 1:
            return False
    return True

board1 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', 
'3e': 'wking'} # True
board2 = 'hello!' # False
board3 = {'2g': 'wking', '3g': 'wking'} # False
board4 = {'9z': 'bpawn'} # False
board5 = {'1h': 'pawnb'} # False
board6 = {'1a': 'bking', '1b': 'bqueen', '1c': 'bbishop', '1d': 'bknight',
'1e': 'brook', '1f': 'bpawn', '1g': 'bpawn', '1h': 'bpawn', '2a': 'bpawn',
'2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bknight',
'2g': 'brook', '2h': 'bbishop'} # True

print(isValidChessBoard(board1))
print(isValidChessBoard(board2))
print(isValidChessBoard(board3))
print(isValidChessBoard(board4))
print(isValidChessBoard(board5))
print(isValidChessBoard(board6))