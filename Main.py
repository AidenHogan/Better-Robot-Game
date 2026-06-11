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
    "water": arcade.color.SEA_BLUE,
    "stone": arcade.color.ASH_GREY
    }
TILE_SIZE = 40
MAP_SIZE = 20


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
        #Track our current z level.  2 = surface
        self.current_z = 2

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        # Create empty variable to hold our tile map
        self.tile_map = []
        #Defines layers of the world
        Z_LEVELS = 5 #0 is 2 blocks into the sky.  2 is surface.  5 is max underground.

        #Makes map and controls tile spawn rate based on elevation
        for z_index in range(Z_LEVELS):
            new_layer = []
            if z_index == 2:
                tile_types = ["grass", "iron_ore", "water"]
                tile_weights = [0.8, .05, .15]
            else:
                tile_types = ["stone", "iron_ore", "water"]
                tile_weights = [.7, .15, .15]
            #Creates a map of strings
            for row_index in range(MAP_SIZE):
                new_row = []
                for col_index in range(MAP_SIZE):
                    #[0] pulls the string from the list random choices generates
                    chosen_tile = random.choices(tile_types, weights = tile_weights)[0]
                    new_row.append(chosen_tile) 

                new_layer.append(new_row) #adds the rows to our tile_map
            
            self.tile_map.append(new_layer) 


    def on_draw(self):
        """Render the screen."""
        # The clear method should always be called at the start of on_draw.
        # It ensures that you have a clean slate for drawing each frame of the game.
        self.clear()

        #Layer we're currently looking at
        current_layer = self.tile_map[self.current_z]


        #Offset the screen to center the tile map
        total_rows = len(current_layer)
        total_cols = len(current_layer[0])
        map_pixel_width = total_cols * TILE_SIZE
        map_pixel_height = total_rows * TILE_SIZE
        x_offset = (WINDOW_WIDTH - map_pixel_width) / 2
        y_offset = (WINDOW_HEIGHT - map_pixel_height) / 2
        #Draw the tile map we created in setup
        for row_index in range(len(current_layer)):
            for col_index in range(len(current_layer[row_index])):
                tile_name = current_layer[row_index][col_index] #gets the string at position in the map
                tile_color = TILE_COLORS[tile_name] #assigns it a color based on name (tile_type)
                #The center of each tile, increase by tile size with increasing index
                #   and start at half the tile size
                center_x = (col_index * TILE_SIZE) + (TILE_SIZE/2) + x_offset
                center_y = (row_index * TILE_SIZE) + (TILE_SIZE/2) + y_offset
                #Make and draw the rectanges 
                tile_rect = arcade.XYWH(center_x, center_y, TILE_SIZE, TILE_SIZE)
                arcade.draw_rect_filled(tile_rect, tile_color)

    #Allows traversal of z layers
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            if self.current_z > 0:
                self.current_z -= 1
        if key == arcade.key.DOWN:
            if self.current_z < 4:
                self.current_z += 1
def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()