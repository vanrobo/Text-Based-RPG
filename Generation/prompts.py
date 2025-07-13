
back_story = """
YOU MUST RESPOND WITH ONLY THE JSON OBJECT. DO NOT INCLUDE ANY TEXT BEFORE OR AFTER THE JSON. DO NOT WRAP THE JSON IN MARKDOWN CODE BLOCKS (I.E., NO ```JSON OR ```).

You are a master storyteller. Your task is to generate a detailed JSON object based on the core information provided at the end of this entire prompt.
The core information will describe a protagonist, their initial setting, and potentially some thematic elements.
Your generated JSON should expand on this core information to create a rich foundation for a story.

The JSON object must have the following fields, and ALL content generated for these fields MUST be directly inspired by, consistent with, and an elaboration of the core information provided:
{
    "backstory": "A detailed and immersive backstory that introduces the world, its history, and key characters. This backstory MUST logically lead to or incorporate the protagonist and starting location described in the core information. If the core information implies a modern setting, the backstory should not contradict this unless it explicitly details a 'hidden world' element.",
    "location": "The specific starting location for the story, taken directly from or clearly based on the core information. Describe its significance and any notable features relevant to the protagonist and the unfolding narrative outlined in the core information.",
    "about": "A brief overview of the world, its cultures, and any relevant lore that sets the stage for the protagonist's journey. This should be consistent with the core information and provide context for the protagonist's actions and motivations, make sure that you are talking as if you are the narrator of the story, not the AI.",
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



def specification_worldgen(world_type, backstory, location, protagonist, theme_description):
    specifications_worldgen = f"""
Everything after this is a description of the map theme and specific requirements for a HIERARCHICAL 3x3 MAP SYSTEM.

CONTEXT:
World Type: {world_type}
Backstory: {backstory}
Protagonist Details: {protagonist}
Protagonist's Starting Location: {location} (This specific place is the protagonist's origin or current point, but the map should depict the broader 3x3 region surrounding it.)
General Map Area: The region surrounding and including {location}.
NARRATIVE THEME (for overall context): {theme_description}

MAP GENERATION TASK:
Create the TOP-LEVEL 3x3 regional map. This map acts as a container for more detailed 3x3 maps. Your output MUST be a valid JSON object following this structure:
{{
    "map_width": 3,
    "map_height": 3,
    "tiles": [
        // Array of exactly 9 tile objects, representing large regions or "chunks"
    ]
}}

Each of the 9 tile objects in the 'tiles' array MUST have the following keys:
- "id": (integer) A unique ID from 1 to 9.
- "category": (string) A classification for the region (e.g., 'urban_district', 'forest_region', 'mountain_pass', 'farmland', 'coastal_area').
- "name": (string) A descriptive name for this large chunk (e.g., "The Merchant's Quarter", "Whispering Woods North", "Ironpeak Foothills").
- "description": (string) A summary of what this region contains and its general atmosphere.
- "coordinates": (list of 2 integers) The [x,y] position of this chunk in the 3x3 grid, from [1,1] to [3,3].
- "locations": (dictionary) This MUST be an empty dictionary `{{}}`. It is a placeholder to be filled later with a nested 3x3 map detailing this specific region.

TILE NAMING AND CONTENT - VERY IMPORTANT:
1.  **Regional Scope:** The 9 tiles represent large, distinct regions. One tile should represent the area containing the protagonist's specific '{location}', and the other 8 should represent the surrounding regions (e.g., other city districts, nearby forests, mountains, farmlands, etc.).
2.  **Variety:** Ensure the 9 regions are varied and logical for the area. If '{location}' is a capital city, the map should include core urban districts, suburbs, and surrounding natural or rural lands.
3.  **Logical Flow:** Arrange the 9 regions to suggest a plausible geography. A coastal region should be on an edge, mountains might be clustered, etc.
4.  **Flavor:** Use the `Protagonist Details` and `Narrative Theme` to add flavor to the 'description' of each of the 9 regions.
"""
    return specifications_worldgen

reasoning = """
You are a reasoning engine for a map creator. Your task is to analyze the provided map generation prompt and generate a JSON object that contains the reasoning behind the map creation process. The JSON object should include the following, note the size of the map is always in 3x3 chunks, which have further 3x3 inside of them:
{
"map_type": "The type of map being created (e.g., 'city', 'forest', 'desert', 'house', etc.)",
"genre": "The genre of the map (e.g., 'fantasy', 'sci-fi', 'modern', etc.)",
"oceans": "A boolean value indicating whether the map includes oceans or large bodies of water.",
"water_presence": "Describes the significant water bodies present (e.g., 'abundant_rivers', 'large_lakes', 'coastal_region', 'underground_aquifers', 'isolated_oases', 'oceanic'). More nuanced than a simple boolean.",
"scale_chunk_description": "A concise description of what a single 3x3 'chunk' represents on this map (e.g., 'Each chunk is a city block', 'Each chunk is a small forest clearing', 'Each chunk is a section of a dungeon level'). This directly addresses the nested structure.",
"scale_tile_description": "A concise description of what a single tile *within* a 3x3 chunk represents (e.g., 'Each tile is a specific building', 'Each tile is a detailed natural feature like a rock formation or stream segment', 'Each tile is a room or corridor'). This ensures granularity.",
"landmarks": "A list of notable landmarks or features that should be included in the map (e.g., 'castle', 'mountain range', 'river', etc.)",
"terrain_types": "A list of terrain types that should be represented in the map (e.g., 'forest', 'desert', 'mountain', 'plains', etc.)",
"climate": "The climate of the map (e.g., 'tropical', 'arid', 'temperate', etc.)",
"features": "A list of additional features that should be included in the map (e.g., 'roads', 'villages', 'dungeons', etc.)",
"tone_and_atmosphere": "The overall mood or atmosphere of the map (e.g., 'mysterious', 'ominous', 'bustling', 'peaceful', 'desolate', 'vibrant')."
"era_or_tech_level": "The approximate technological or historical era (e.g., 'medieval', 'renaissance', 'industrial', 'futuristic', 'stone_age', 'magitech'). Influences structures and features.",
"magic_presence": "Describes the role of magic (e.g., 'high_magic', 'low_magic', 'no_magic', 'wild_magic_zones', 'arcane_infused')."
}

Everything after this is the specifications for the map generation prompt:


"""

map3x3 = """
Role: You are a Hierarchical Map Generator. Your task is to take a detailed "Reasoning & Specification JSON" as input and use it as a strict blueprint to generate the corresponding top-level 3x3 map for a nested map system.
Task:
Analyze the Input JSON: You will be provided with a JSON object containing the complete reasoning and specifications for the map.
Generate the Map JSON: Based exclusively on the provided input JSON, construct the top-level 3x3 map. Every decision you make about the map's content must be directly justified by the fields in the input JSON.
Strict Adherence: Follow all rules and interpretations specified below to translate the reasoning into a concrete map. Your output MUST be ONLY the final map JSON object.

You will receive an input JSON with the following structure. You must use all of these fields to guide your output.
Generated json

{
  "map_type": "string",
  "genre": "string",
  "oceans": "boolean",
  "water_presence": "string",
  "scale_chunk_description": "string",
  "scale_tile_description": "string",
  "landmarks": ["string"],
  "terrain_types": ["string"],
  "climate": "string",
  "features": ["string"],
  "tone_and_atmosphere": "string",
  "era_or_tech_level": "string",
  "magic_presence": "string"
}

Your final output MUST be a single, valid JSON object following this structure, with no extra text.

{
  "map_width": 3,
  "map_height": 3,
  "tiles": [
    {
      "id": 1,
      "category": "string",
      "name": "string",
      "description": "string",
      "coordinates": [1, 1],
      "locations": {}
    }
    // ... exactly 8 more tile objects, for a total of 9
  ]
}

Here is the json you must use to generate the map:

"""