#Setup the game here

import arcade #Game library
import random

#Setup window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Robotica"

# Define colors for the tile map
TILE_COLORS = {
    "grass": arcade.color.LIGHT_GREEN,
    "iron_ore": arcade.color.BATTLESHIP_GREY,
    "water": arcade.color.SEA_BLUE
    }
TILE_SIZE = 40

#Ripped from arcade example.  Idk what it does beyond making the window
#https://api.arcade.academy/en/stable/tutorials/platform_tutorial/step_01.html
#I added a tile map
class GameView(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class to set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        self.background_color = arcade.csscolor.BLACK

        # Create empty variable to hold our tile map
        self.tile_map = []

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        #Tiles we use and their probabilities
        tile_weights = [("grass", .8), ("iron_ore", .05), ("water", .15)]
        #Tile properties
        tile_types = [t[0] for t in tile_weights]
        tile_weights = [t[1] for t in tile_weights]
        #Creates a map of strings
        for row_index in range(20):
            new_row = []
            for col_index in range(20):
                new_row.append(random.choices(tile_types, weights = tile_weights)[0]) #[0] pulls the string from the list random choices generates
            self.tile_map.append(new_row) #adds the rows to our tile_map


    def on_draw(self):
        """Render the screen."""

        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.
        self.clear()

        # Code to draw other things will go here

        #Offset the screen to center the tile map
        total_rows = len(self.tile_map)
        total_cols = len(self.tile_map[0])
        map_pixel_width = total_cols * TILE_SIZE
        map_pixel_height = total_rows * TILE_SIZE
        x_offset = (WINDOW_WIDTH - map_pixel_width) / 2
        y_offset = (WINDOW_HEIGHT - map_pixel_height) /2
        #Draw the tile map we created in setup
        for row_index in range(len(self.tile_map)):
            for col_index in range(len(self.tile_map[row_index])):
                tile_name = self.tile_map[row_index][col_index] #gets the string at position in the map
                tile_color = TILE_COLORS[tile_name] #assigns it a color based on name (tyle_type)
                #Center is the center of each tile, so increase by tile size with increasing index, and start at half the tile size
                center_x = (col_index * TILE_SIZE) + (TILE_SIZE/2) + x_offset
                center_y = (row_index * TILE_SIZE) + (TILE_SIZE/2) + y_offset
                tile_rect = arcade.XYWH(center_x, center_y, TILE_SIZE, TILE_SIZE)
                arcade.draw_rect_filled(tile_rect, tile_color)
def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()