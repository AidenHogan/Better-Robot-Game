# Contains most of the game settings and other immutable characteristics
import arcade # Game library

#Window Settings
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Robotica"

#World generation settings
TILE_SIZE = 40
MAP_SIZE = 20
SURFACE_LEVEL = 50
Z_LEVELS = 100 #0 is the highest sky level.  The number here is the lowest (undeground). SURFACE_LEVEL is set above


# Define colors and tile types for the tile map
TILE_COLORS = {
    "grass": arcade.color.LIGHT_GREEN,
    "iron_ore": arcade.color.BATTLESHIP_GREY,
    "water": arcade.color.SEA_BLUE,
    "stone": arcade.color.ASH_GREY,
    "sky": [135, 206, 250, 15] #Sky blue, opacity 125 = 50%, 0 = invisible, 250 = 100%
    }

# Defines areas which will determine what tile types can spawn where
# For 100 levels: First 20 are sky, Next 10 are Mountain layers
# Next 5 are Woodland layers, Next two are Grasslands, Next is Marsh
# Next is Beach trees, Next two are Dunes, Next is Beach
# Next 10 are water/ocean layers, The rest is underground
TILE_HEIGHT_RANGES = {
    "sky": (0,20),
    "mountain": (20, 30),
    "woodlands": (30, 35),
    "grasslands": (35, 37),
    "marsh": (37, 37),
    "beach_trees": (38, 38),
    "dunes": (38, 40),
    "beach": (40, 40),
    "ocean": (40, 50),
    "underground": (50, 100)
}