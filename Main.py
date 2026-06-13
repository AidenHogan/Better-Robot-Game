#Setup the game here
import arcade #game library.  #type: ignore (removes false 'not-used' flag)
import random
import constants #All of our game settings

#Responsible for creating the game window, creating and drawing the map.  
class GameView(arcade.Window):
    #Setup
    def __init__(self):

        # Call the parent class to set up the window
        super().__init__(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT, constants.WINDOW_TITLE)
        self.background_color = arcade.csscolor.BLACK
        
        # Track our current z level.
        self.current_z = constants.SURFACE_LEVEL

    """High level summary of what happens on game start"""
    def setup(self):
        self.tile_map = self.generate_world_data()
        self.calculate_screen_offsets()

    # Map data creation
    def generate_world_data(self):
         # Holds our tile map
        new_map = []

        # Makes map and controls tile spawn rate based on elevation
        for z_index in range(constants.Z_LEVELS):
            new_layer = []
            if z_index < constants.SURFACE_LEVEL: #Sky
                tile_types = ["sky"]
                tile_weights = [1]
            elif z_index == constants.SURFACE_LEVEL: #Surface
                tile_types = ["grass", "iron_ore", "water"]
                tile_weights = [0.8, .05, .15]
            else: #Underground
                tile_types = ["stone", "iron_ore", "water"]
                tile_weights = [.8, .15, .05]
            #Creates a map of strings
            for row_index in range(constants.MAP_SIZE):
                new_row = []
                for col_index in range(constants.MAP_SIZE):
                    #[0] pulls the string from the list random choices generates
                    chosen_tile = random.choices(tile_types, weights = tile_weights)[0]
                    new_row.append(chosen_tile) #Add each tile to the row

                new_layer.append(new_row) #adds the rows to each layer
            
            new_map.append(new_layer) #Add each layer to our full tile_map
        return new_map
    
    # Offset the screen to center the in game map
    def calculate_screen_offsets(self):
        total_rows = len(self.tile_map[0])
        total_cols = len(self.tile_map[0])
        map_pixel_width = total_cols * constants.TILE_SIZE
        map_pixel_height = total_rows * constants.TILE_SIZE
        self.x_offset = (constants.WINDOW_WIDTH - map_pixel_width) / 2
        self.y_offset = (constants.WINDOW_HEIGHT - map_pixel_height) / 2

    """High level summary of what is drawn to the screen each frame"""
    def on_draw(self):
        self.clear()
        self.draw_visible_layers()

    # Handles depth and painting the map to screen
    def draw_visible_layers(self):
        #all maps are the same size
        tile_map_size = self.tile_map[0]

        if self.current_z >= constants.SURFACE_LEVEL:
            layers_to_draw = [self.current_z]
            current_layer = self.tile_map[self.current_z]
        else:
            layers_to_draw = []
            #Start at surface, stop just past the current z, step back by 1
            for depth in range(constants.SURFACE_LEVEL, self.current_z -1, -1):
                layers_to_draw.append(depth)
       
        #Draw the tile map we created in setup
        for depth in layers_to_draw:
            current_layer = self.tile_map[depth]
            for row_index in range(len(tile_map_size)): #use any tile_map, they're all the same size
                for col_index in range(len(tile_map_size[row_index])):
                    tile_name = current_layer[row_index][col_index] #gets the string at position in the map
                    tile_color = constants.TILE_COLORS[tile_name] #assigns it a color based on name (tile_type)
                    #The center of each tile, increase by tile size with increasing index
                    #   and start at half the tile size
                    center_x = (col_index * constants.TILE_SIZE) + (constants.TILE_SIZE/2) + self.x_offset
                    center_y = (row_index * constants.TILE_SIZE) + (constants.TILE_SIZE/2) + self.y_offset
                    #Make and draw the rectanges 
                    tile_rect = arcade.XYWH(center_x, center_y, constants.TILE_SIZE, constants.TILE_SIZE)
                    arcade.draw_rect_filled(tile_rect, tile_color)    

    # Handles player input
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            if self.current_z > 0: #Min
                self.current_z -= 1
        if key == arcade.key.DOWN:
            if self.current_z < constants.Z_LEVELS-1: #Max-1
                self.current_z += 1
def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()