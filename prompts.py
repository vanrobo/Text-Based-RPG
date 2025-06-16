
back_story = """
YOU MUST RESPOND WITH ONLY THE JSON OBJECT. DO NOT INCLUDE ANY TEXT BEFORE OR AFTER THE JSON. DO NOT WRAP THE JSON IN MARKDOWN CODE BLOCKS (I.E., NO ```JSON OR ```).

You are a master storyteller. Your task is to generate a detailed JSON object based on the core information provided at the end of this entire prompt.
The core information will describe a protagonist, their initial setting, and potentially some thematic elements.
Your generated JSON should expand on this core information to create a rich foundation for a story.

The JSON object must have the following fields, and ALL content generated for these fields MUST be directly inspired by, consistent with, and an elaboration of the core information provided:
{
    "backstory": "A detailed and immersive backstory that introduces the world, its history, and key characters. This backstory MUST logically lead to or incorporate the protagonist and starting location described in the core information. If the core information implies a modern setting, the backstory should not contradict this unless it explicitly details a 'hidden world' element.",
    "location": "The specific starting location for the story, taken directly from or clearly based on the core information. Describe its significance and any notable features relevant to the protagonist and the unfolding narrative outlined in the core information.",
    "protagonist": {
        "name": "Protagonist's Name, based on the core information.",
        "background": "Their history and origin, elaborated from the core information.",
        "motivations": "What drives them forward, derived from or consistent with the core information.",
        "unique_abilities": ["Ability 1 (must align with the protagonist's description in the core information; can be mundane skills or special talents)", "Ability 2 (if applicable)"],
        "traits": {
            "personality": ["Trait 1", "Trait 2", "Trait 3 (all traits should reflect the protagonist in the core info)"],
            "physical": ["Trait 1", "Trait 2"],
            "emotional": ["Trait 1", "Trait 2"]
        },
        "other_notable_features": "Any other important details about the protagonist, expanded from the core information."
    },
    "theme": "A central theme or themes that emerge from or are suggested by the core information provided about the protagonist, location, and potential conflicts.",
    "setting": "A description of the world where the story takes place. This setting MUST be built around and be consistent with the protagonist's starting location and background from the core information. If the core information describes a modern city, the setting should be that modern city, perhaps with hidden fantastical elements if the core information or backstory implies them.",
    "conflict": "The central conflict or challenge that drives the narrative forward. This conflict should directly involve or stem from the protagonist and their situation as described in the core information."
}

Everything after this line is the CORE INFORMATION you must use to fill the JSON above:
"""


world_gen = """
Prompt: 
You are a map generator. Your task is to create a 10x10 (10 tiles wide by 10 tiles high) 2D map represented in JSON format. You will be given a description of the desired map theme/setting (e.g., 'medieval forest', 'sci-fi city', 'tropical island'). You will then generate a JSON object containing the following keys:
map_width: (integer) The width of the map in tiles. This MUST always be 10.
map_height: (integer) The height of the map in tiles. This MUST always be 10.
tiles: (array of objects) An array where each object represents a tile in the map. Each tile object must have the following keys:
id: (integer, 1-based) A unique numerical ID for the tile, starting from 1 in the top-left corner and incrementing sequentially row by row. Example: for a 10x10 map, the IDs would be 1 through 100.
name: (string) A descriptive name of the tile type. This name should be relevant to the map's theme and should be easily understandable (e.g., 'forest_tree', 'city_street', 'sand_beach'). Use underscore naming conventions for the name. Avoid overly generic names like "grass" unless specific instructions state otherwise. Be as specific and descriptive as possible with the tile names.
Follow these rules STRICTLY:
The JSON output MUST be valid and parsable. 
map_width and map_height MUST BOTH always be 10, regardless of the input theme.
The tiles array MUST contain exactly 100 elements.
The id values in the tiles array MUST be sequential and start from 1, row by row, ending at 100.
The name values MUST be descriptive and relevant to the specified theme. The tile names should be different and capture the visual and gameplay variety you might expect.
Even if the theme implies a different size, you MUST generate a 10x10 map. For example, even if I asked for "a tiny village," the generated map still must be 10x10.
Example Input:
'Create a map with a medieval forest theme.'
Desired JSON Output Structure (showing only a few tiles for brevity,note these don't have to be the same as the example, it may be a city or anything else):
{
    "map_width": 10,
    "map_height": 10,
    "tiles": [ 
        {"id": 1, "name": "verdan_forest", description: "A lush green forest with towering trees."},
        {"id": 2, "name": "forest_clearing", description: "A small clearing in the forest with wildflowers."},
        {"id": 3, "name": "ancient_oak_tree", description: "A massive oak tree with a thick trunk."},
        {"id": 4, "name": "forest_stream", description: "A gentle stream flowing through the forest."},
        {"id": 5, "name": "mossy_rock", description: "A large rock covered in moss."},
        //rest of the tiles here
        {"id": 99, "name": "forest_cave_entrance", description: "An entrance to a dark cave in the forest."},
        {"id": 100, "name": "forest_path", description: "A narrow path winding through the forest."}
    ]
}
"""

main_story =  f""" """

big_map = """YOU MUST RESPOND WITH ONLY THE JSON OBJECT. DO NOT INCLUDE ANY TEXT BEFORE OR AFTER THE JSON. DO NOT WRAP THE JSON IN MARKDOWN CODE BLOCKS (I.E., NO ```JSON OR ```).

Prompt:

You are a map generator. Your task is to create a 3x3 (3 tiles wide by 3 tiles high) 2D map represented in JSON format. You will be given a description of the desired map theme/setting (e.g., 'medieval forest', 'sci-fi city', 'tropical island'). You will then generate a JSON object containing the following keys:
map_width: (integer) The width of the map in tiles. This MUST always be 3.
map_height: (integer) The height of the map in tiles. This MUST always be 3.
tiles: (array of objects) An array where each object represents a tile in the map. Each tile object must have the following keys:
id: (integer, 1-based) A unique numerical ID for the tile, starting from 1 in the top-left corner and incrementing sequentially row by row. Example: for a 3x3 map, the IDs would be 1 through 9.
name: (string) A descriptive name of the tile type. This name should be relevant to the map's theme and should be easily understandable (e.g., 'forest_tree', 'city_street', 'sand_beach'). Use underscore naming conventions for the name. Avoid overly generic names like "grass" unless specific instructions state otherwise. Be as specific and descriptive as possible with the tile names.
coordinates: (a list of 2 integers) It  should contain the locations coordinate in the form [x,y] where x and y are integers ranging from 1 to 3. Their values should correspond with their ids. For example - id 1 would have coordinates [1,1], id 2 would have [2,1] id 3 would have [3,1], id 4 would have [1,2] and so on and so forth till id 9 which will have [3,3]
locations: this must be an empty dictionary that can be filled up later with additional maps if necessary

Follow these rules STRICTLY:
The JSON output MUST be valid and parsable. 
map_width and map_height MUST BOTH always be 3, regardless of the input theme.
The tiles array MUST contain exactly 9 elements.
The id values in the tiles array MUST be sequential and start from 1, row by row, ending at 100.
The name values MUST be descriptive and relevant to the specified theme. The tile names should be different and capture the visual and gameplay variety you might expect.
The coordinates MUST be a list with 2 elements occupying ONE LINE inside the JSON. The coordinates should look like [1,2]
      "coordinates": [
        1,
        1
      ],

      but rather SHOULD BE like

      "coordinates: [1,1]


      
The locations must always remain an empty dictionary which can be filled with values later as required
Even if the theme implies a different size, you MUST generate a 3x3 map. For example, even if I asked for "a tiny village," the generated map still must be 3x3."""

def specification_worldgen(world_type, backstory, location, protagonist, theme_description):
    specifications_worldgen = f"""
    Everything after this is a description of the map theme and specific requirements:

    CONTEXT:
    World Type:  {world_type}
    Backstory: {backstory}
    Protagonist Details: {protagonist}
    Protagonist's Starting Location: {location} (This specific place is the protagonist's origin or current point, but the map should depict a broader regional area surrounding it.)
    General Map Area: The region surrounding and including {location}.

    MAP GENERATION TASK:
    Create a 10x10 map strictly following all previously defined JSON rules (map_width: 10, map_height: 10, 100 tiles with sequential IDs 1-100, each tile having id, name, and description).

    NARRATIVE THEME (for overall context): {theme_description}
    MAP THEME (for tile generation - Visual/Structural): Generate a regional map. Each tile should represent a significant zone, district, geographical feature, or major transport route in and around the area described by '{location}'.
    If '{location}' refers to a specific part of a city (e.g., a district or sector), the map should include other parts of that main city and also depict the transition to its surrounding environment (e.g., suburbs, countryside, other nearby towns/cities, industrial zones, as appropriate for the type of place '{location}' describes).

    TILE NAMING AND CONTENT - VERY IMPORTANT:
    1.  **Regional Scope & Relevance to '{location}':** The `name` and `description` for each tile MUST reflect a broader, regional scale. Tile names should be specific to the types of zones and features one would expect to find in and around an area like '{location}'. Avoid overly generic names.
    2.  **Generate NEW Tile Names for Regional Scale:**
        *   Consider '{location}' as a central point of reference.
        *   Tiles should represent distinct districts of the main city implied by '{location}', larger geographical features (rivers, large parks, hills if applicable), major highways, and representative zones of surrounding towns or rural areas.
        *   For example, if '{location}' is 'Sector X, MainCity, Country', tiles could be 'MainCity_downtown_core', 'Sector_X_overview_tile', 'highway_north_of_MainCity', 'rural_farmland_west_of_MainCity', 'neighboring_town_alpha'.
        *   The specific place mentioned in '{location}' should be represented as one or a few tiles showing its general character within the larger regional map, not a hyper-detailed layout of it.
    3.  **Distribution of Tiles:**
        *   A good portion of the map (e.g., 50-60 tiles) should represent different key areas and aspects of the main city or urban conglomeration implied by '{location}'.
        *   The remaining tiles (e.g., 30-40 tiles) should depict the surrounding environment, such as satellite towns, industrial areas, agricultural land, natural landscapes, or other connecting regions relevant to '{location}'.
    4.  **Variety at Regional Scale:** Show appropriate variety for a region surrounding '{location}'. This could include dense urban areas, suburban residential zones, commercial centers, industrial parks, transportation networks (roads, railways, airports if applicable), and natural elements (rivers, forests, coastlines, etc., if consistent with '{location}').
    5.  **Logical Flow (Approximate):** Try to arrange tiles to suggest a plausible geographical relationship between different zones, even if it's a simplification.
    6.  **Granularity:** Tiles represent zones or large areas. Avoid detailing individual small buildings from '{location}' unless it's a landmark so significant it would define an entire regional map tile.
    7.  **NO Unrelated Global Tiles:** Focus exclusively on the region suggested by '{location}' and its plausible surroundings. Do not include tiles from distant, unrelated countries or continents.
    8.  **Descriptions are Mandatory:** Each tile must have a `description` field providing concise, flavorful text that reflects its character within the regional map themed around '{location}'.

    When generating the map, interpret '{location}' to understand the type of environment (urban, suburban, rural, etc.) and generate a believable regional map for that kind of setting. The protagonist details (provided as {protagonist}) can add flavor to descriptions where appropriate.
    """
    return specifications_worldgen

def specification_backstory(name, location, ):
    print(name)




def specification_map_generation (world_type, backstory, location, protagonist, theme_description):
    specifications_map_generation  = f""" Everything after this is a description of the map theme and specific requirements:

    CONTEXT:
    World Type:  {world_type}
    Backstory: {backstory}
    Protagonist Details: {protagonist}
    Protagonist's Starting Location: {location} (This specific place is the protagonist's origin or current point, but the map should depict a broader regional area surrounding it.)
    General Map Area: The region surrounding and including {location}."""


    return specifications_map_generation