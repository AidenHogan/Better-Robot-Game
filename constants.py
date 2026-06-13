
import arcade #Game library #type: ignore (removes yellow line. trust)

#Window Settings
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Robotica"

#World generation settings
TILE_SIZE = 40
MAP_SIZE = 20
SURFACE_LEVEL = 2
Z_LEVELS = 5 #0 is the highest sky level.  The number here is the lowest (undeground). SURFACE_LEVEL is set above


# Define colors and tile types for the tile map
TILE_COLORS = {
    "grass": arcade.color.LIGHT_GREEN,
    "iron_ore": arcade.color.BATTLESHIP_GREY,
    "water": arcade.color.SEA_BLUE,
    "stone": arcade.color.ASH_GREY,
    "sky": [135, 206, 250, 125] #Sky blue, opacity 125 = 50%, 0 = invisible, 250 = 100%
    }