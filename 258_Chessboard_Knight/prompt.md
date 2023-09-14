# Prompt

given a chess board of n rows (top to bottom) and n columns (left to right).
In each move, a knight moves either:
- 2 column positions and 1 row position
- 2 row positions and 1 column position

In other words, a move is 2 steps along one axis and 1 step along a perpendicular axis.

Given, a starting position A and ending position B, calculate the minimum number of moves needed by the knight to move from A to B if it is possible. If it is not possible, return -1. All moves must remain within the chess board.

example:
n=9
startRow=4
startCol=4
endRow=4
endCol=8

chess board has a size of 9x9.
- starts at position 4,4 (startRow,startCol)
- move 1 step up or down, then 2 steps right to reach either (3,6) or (5,6).
-move 2 steps right and 1 step down or up as necessary to reach the position (4,8)
-minimum number of moves to move from (4,4) to (4,8) is 2.