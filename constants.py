# Multiplayer
PORT = 9009



WINDOW_NAME = "HEX BOARD GAME"

# Colours
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BACKGROUND_COLOUR = (40, 41, 35)

# Board
HEX_RADIUS = 20
TEXT_OFFSET = 45
HEX_OFFSET = 95


# Game window
SIZE = 11
WIDTH = 2 * HEX_OFFSET + (1.75 * HEX_RADIUS) * SIZE + HEX_RADIUS * SIZE
HEIGHT = 2 * HEX_OFFSET + (1.75 * HEX_RADIUS) * SIZE
MWIDTH = 850.0
MHEIGHT = 610.0
GAME_RESOLUTION = (WIDTH, HEIGHT)
MENU_RESOLUTION = (MWIDTH, MHEIGHT)


# Player
PLAYER_COLORS = [(240, 0, 0), (0, 128, 255), (255, 255, 255)]


about_text = """
Hex is a two player abstract strategy board game in
which players attempt to connect opposite sides of a
rhombus-shaped board made of hexagonal cells.

It is traditionally played on an 11×11 rhombus board,
although other board sizes are also popular. The board
is composed of hexagons called cells or hexes. Each
player is assigned a pair of opposite sides of the 
board, which they must try to connect by alternately
placing a stone of their color onto any empty hex. 
Once placed, the stones are never moved or removed.

A player wins when they successfully connect their 
sides together through a chain of adjacent stones. 
Draws are impossible in Hex due to the topology of the game board.

Despite the simplicity of its rules, the game has deep 
strategy and sharp tactics. It also has profound 
mathematical underpinnings.
"""