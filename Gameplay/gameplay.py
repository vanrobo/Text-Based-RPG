import json
import os
import time
import threading
# Assuming tile_type.py is in the parent directory or accessible via PYTHONPATH
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from tile_type import Tile, Forest, Mountain, City, Water # Import new tile classes

# game_map_tiles will be a 2D list (list of rows) of Tile objects for the current segment.
game_map_tiles = []
current_player_position = {"x": 0, "y": 0} # Player's current x, y coordinates in the segment

# Assuming segments are 3x3 grids of locations based on "prompts.map3x3"
SEGMENT_WIDTH = 3
SEGMENT_HEIGHT = 3

def load_world_map_segment(save_slot_number: int, segment_index: int = 0):
    """
    Loads a specific segment of the world map from the save slot's world.json.
    It deserializes the tile data into a 2D list of Tile objects.
    """
    global game_map_tiles
    game_map_tiles = [] # Clear previous map data

    # Construct path using os.path.join for portability
    base_storage_path = "Storage"
    save_slot_dir = os.path.join(base_storage_path, "Saveslots", str(save_slot_number))
    save_file_path = os.path.join(save_slot_dir, "world.json")

    # Ensure the save slot directory exists before trying to read from it (relevant if it's expected to be pre-created)
    # However, for loading, we usually expect the file and its directory to exist.
    # os.makedirs(save_slot_dir, exist_ok=True) # More relevant if we were about to write here.

    try:
        with open(save_file_path, "r") as f:
            world_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Save file not found at {save_file_path}")
        return False
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {save_file_path}")
        return False

    if "tiles" not in world_data or not isinstance(world_data["tiles"], list):
        print("Error: Invalid world data format - 'tiles' array missing or not a list.")
        return False

    if segment_index >= len(world_data["tiles"]):
        print(f"Error: Segment index {segment_index} out of bounds for {len(world_data['tiles'])} segments.")
        return False

    segment_data = world_data["tiles"][segment_index]

    if "locations" not in segment_data or not isinstance(segment_data["locations"], list):
        print(f"Error: Invalid segment data - 'locations' array missing or not a list in segment {segment_index}.")
        return False

    raw_locations = segment_data["locations"]
    expected_tile_count = SEGMENT_WIDTH * SEGMENT_HEIGHT
    if len(raw_locations) != expected_tile_count:
        print(f"Warning: Segment {segment_index} has {len(raw_locations)} locations, but expected {expected_tile_count} for a {SEGMENT_WIDTH}x{SEGMENT_HEIGHT} grid. Map may not load correctly as 2D.")
        # Fallback: load as a flat list and issue warning, or handle error more strictly
        # For now, we'll attempt to structure it, but it might fail or be incomplete.

    temp_flat_list = []
    for tile_dict in raw_locations:
        try:
            tile_obj = Tile.from_dict(tile_dict)
            temp_flat_list.append(tile_obj)
        except Exception as e:
            print(f"Error deserializing tile data: {tile_dict}. Error: {e}")
            temp_flat_list.append(Tile("Error Tile", "Failed to load this tile.", False, "?"))

    # Structure the flat list into a 2D grid (list of rows)
    for i in range(SEGMENT_HEIGHT):
        row = temp_flat_list[i*SEGMENT_WIDTH : (i+1)*SEGMENT_WIDTH]
        if len(row) < SEGMENT_WIDTH: # Handle cases where raw_locations was too short
            row.extend([Tile("Void Tile", "Empty space.", False, " ")] * (SEGMENT_WIDTH - len(row)))
        game_map_tiles.append(row)

    print(f"Loaded segment {segment_index} from save slot {save_slot_number} as a {len(game_map_tiles)}x{len(game_map_tiles[0]) if game_map_tiles else 0} grid.")
    return True

def get_tile_at(x: int, y: int):
    """
    Retrieves the Tile object at the given x, y coordinates within the current segment.
    Returns None if coordinates are out of bounds.
    """
    if not game_map_tiles or y < 0 or y >= len(game_map_tiles) or x < 0 or x >= len(game_map_tiles[0]):
        return None
    return game_map_tiles[y][x]

def display_current_tile_info():
    """
    Displays information about the tile at the current player's x, y position.
    """
    tile = get_tile_at(current_player_position["x"], current_player_position["y"])

    if tile:
        print(f"\nCurrent Location ({current_player_position['x']}, {current_player_position['y']}): {tile.name}")
        print(f"Description: {tile.description}")
        print(f"Traversable: {'Yes' if tile.traversable else 'No'}")
        if isinstance(tile, Forest):
            print(f"Resources: {tile.resource_type}")
        elif isinstance(tile, Mountain):
            print(f"Elevation: {tile.elevation}m")
        elif isinstance(tile, City):
            print(f"Population: {tile.population}")
        elif isinstance(tile, Water):
            print(f"Water type: {tile.water_type}")
    else:
        print(f"Current position ({current_player_position['x']}, {current_player_position['y']}) is out of bounds or map not loaded.")

# Example of how you might start a game or load data
def start_game(save_slot: int, start_x: int = 0, start_y: int = 0):
    print(f"Starting game from save slot {save_slot}...")
    if load_world_map_segment(save_slot, 0): # Load the first segment
        current_player_position["x"] = start_x
        current_player_position["y"] = start_y
        display_current_tile_info()
        # Here, you would typically start the main game loop
        # game_loop()
    else:
        print("Failed to load game map. Cannot start game.")

if __name__ == '__main__':
    # This is for testing purposes.
    # In a real game, you'd get the save slot from the user or a menu.

    # To test this, you need a world.json file generated by world_gen.py
    # in, for example, Storage/Saveslots/1/

    # Create a dummy world.json for testing if it doesn't exist
    # NOTE: This section is for direct testing of gameplay.py.
    # It will overwrite any existing world.json in the dummy_save_slot.
    dummy_save_slot = 1
    base_storage_path = "Storage"
    save_slot_dir = os.path.join(base_storage_path, "Saveslots", str(dummy_save_slot))
    dummy_world_file_path = os.path.join(save_slot_dir, "world.json")

    print(f"Setting up dummy world.json for testing at: {dummy_world_file_path}")
    os.makedirs(save_slot_dir, exist_ok=True) # Ensure the directory exists

    # This dummy data explicitly provides 9 tiles for a 3x3 grid.
    dummy_data = {
        "tiles": [ # This outer list represents different segments; we're using one segment.
            {
                "id": "segment0_test", # Changed ID for clarity
                "category": "test_region_3x3",
                "description": "A 3x3 test region for gameplay.py.",
                "locations": [ # 9 tiles for a 3x3 grid, flattened row by row
                    {"type": "Forest", "name": "Greenwood (0,0)", "description": "A quiet forest.", "traversable": True, "symbol": "F", "resource_type": "wood"},
                    {"type": "Mountain", "name": "Peak (1,0)", "description": "A tall mountain.", "traversable": False, "symbol": "M", "elevation": 1200},
                    {"type": "City", "name": "Town (2,0)", "description": "A small town.", "traversable": True, "symbol": "C", "population": 500},

                    {"type": "Water", "name": "River (0,1)", "description": "Flowing river.", "traversable": False, "symbol": "W", "water_type": "river"},
                    {"type": "Tile", "name": "Plains (1,1)", "description": "Open plains.", "traversable": True, "symbol": "."},
                    {"type": "Forest", "name": "Darkwood (2,1)", "description": "A spooky forest.", "traversable": True, "symbol": "F", "resource_type": "ancient wood"},

                    {"type": "City", "name": "Old Town (0,2)", "description": "An old, crumbling town.", "traversable": True, "symbol": "C", "population": 150},
                    {"type": "Mountain", "name": "Foothills (1,2)", "description": "Rocky foothills.", "traversable": True, "symbol": "m", "elevation": 300},
                    {"type": "Water", "name": "Lake (2,2)", "description": "A calm lake.", "traversable": False, "symbol": "L", "water_type": "lake"}
                ]
            }
        ]
    }
    with open(dummy_world_file_path, "w") as f:
        json.dump(dummy_data, f, indent=4)

    start_game(dummy_save_slot, start_x=1, start_y=1) # Start at (1,1) which is Plains

    # Example: Move player and display info using x,y coordinates
    if game_map_tiles: # Check if map loaded
        print("\nMoving player to (0,0)...")
        current_player_position["x"] = 0
        current_player_position["y"] = 0
        display_current_tile_info()

        print("\nMoving player to (2,1)...")
        current_player_position["x"] = 2
        current_player_position["y"] = 1
        display_current_tile_info()

        print("\nAttempting to move out of bounds (3,0)...")
        current_player_position["x"] = 3
        current_player_position["y"] = 0
        display_current_tile_info()

# Removed original Generation imports as they are not used here directly yet
# import Generation.ai as ai
# import Generation.prompts as prompts

