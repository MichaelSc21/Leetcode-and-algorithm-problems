"""Question 2: Loops
Red and Green are playing a game which consists of placing square tiles on a grid and trying to form loops
of their own colour. Each tile incorporates a red line and a green line, touching different edges of the tile.
There are six different types of tile that are used in the game. Red and green lines are shown by solid and
dashed lines respectively. The numbers by the tiles will be used when inputting grids.
Tiles are placed adjacent to each other on the grid. A line meeting another line of the same colour —
across a shared edge between tiles — is treated as a single continuous line across multiple tiles. If the
lines are different colours the lines are treated as being separate. A loop is a line that begins on one tile
and continues along additional tiles until it rejoins itself on the first tile.
At the end of the game each player scores a single point for each tile that contains part of a line forming a
loop of their colour. A tile can contribute towards the score of both players.
In the example to the right there is a single loop; the numbers
indicate how the grid will be input.
• This is a red (solid) loop covering six tiles.
• This is not a loop as the green (dashed) line does not
 rejoin itself.
The red player has scored 6 points and the green player 0.


2(a) [ 25 marks ]
Write a program that reads in a grid and outputs the score for each player.
Your program should first read in a single integer (2 ≤ n ≤ 6) indicating the size of the
(square) grid. You should then read in n lines representing the rows (starting at the
top), each of which will contain n digits representing the tiles on the grid in order.
You should output two values: the score for the red played followed by the score for
the green player."""



"""
the numbers in the dictionary represent each square
the characters in the list represent the whether the middle of each edge of the square meets with a solid(r) or dashed(g) line
the characters start representing the top edge of the square and finish off with the left edge, going clockwise

"""


dict = {1: ['r', 'g', 'r', 'g'], 2:['g', 'r', 'g', 'r'], 3:['r', 'g', 'g', 'r'], 4: ['r', 'r', 'g', 'g'], 5:['g', 'r', 'r', 'g'], 6:['g', 'g', 'r', 'r']}

n = 4
grid = []

grid_input = [
[1, 3, 4, 1],
[5, 2, 6, 4],
[4, 2, 3, 5],
[4, 4, 5, 4]
]
#creating the grid based on the input
for column in grid_input:
    list = []
    for row in column:
        list.append(dict[row])
    grid.append(list)
del list
for i in grid:
    print(i)




