

with open(r"Storage\backstory.json") as backstory: 
    info = json.load(backstory)
    backstory = info["backstory"]
    protagonist = info["protagonist"]
    location = info["location"]
    theme_description = info["theme"]

    print("Backstory:\n",backstory)
    print("Protagonist:\n",protagonist)
    print("Location:\n",location)
    print("Theme:\n",theme_description)


def specifications(backstory, location, protagonist, theme_description):
    specifications_worldgen="""
    Everything after this is a description of the map theme and specific requirements:

    CONTEXT:
    Backstory: {backstory}
    Protagonist: {protagonist} lives in {location}.
    Current Location: {location}

    MAP GENERATION TASK:
    Create a 10x10 map strictly following all previously defined JSON rules (map_width: 10, map_height: 10, 100 tiles with sequential IDs 1-100).

    THEME: {theme_description}

    TILE NAMING AND CONTENT - VERY IMPORTANT:
    1.  **Specificity is Key:** The `name` and `description` for each tile MUST be highly specific to {location} and the broader Delhi urban/suburban environment.
    2.  **Generate NEW Tile Names:** Generate *new* tile names that reflect this specific location and its characteristics. Do NOT feel constrained to only use tile names from any pre-existing generic list if they don't fit {location}. Your goal is to make this feel like a real part of Dwarka.
        *   For example, instead of a generic "street", use "dwarka_sector_22_residential_street", "dwarka_main_road_sector_22", or "dwarka_market_lane".
        *   Instead of just "park", use "dwarka_sector_22_community_park".
    3.  **Focus on Dwarka Sector 22:** A significant portion of the map (e.g., at least 20-30 tiles, clustered or spread logically) should explicitly represent different aspects of `Dwarka Sector 22` (e.g., `dwarka_sector_22_apartment_block_A`, `dwarka_sector_22_local_market_entrance`, `dps_dwarka_school_boundary_wall`).
    4.  **Surrounding Areas:** Remaining tiles should represent other immediate parts of Dwarka or very close, logically connected areas within Delhi that one might find near Dwarka Sector 22 (e.g., `dwarka_metro_station_sector_21_approach`, `adjoining_dwarka_sector_commercial_strip`, `road_to_dwarka_expressway`).
    5.  **Variety within Theme:** Even within Dwarka, show variety: different types of residential buildings, specific shops, parts of the school, different types of roads, green spaces, service areas, etc.
    6.  **Connectivity (Implied "Dungeon-like" for Urban):** Arrange tiles to suggest a connected urban layout. Roads should logically connect. Parks might be bordered by streets or buildings. Markets should have distinct areas.
    7.  **NO Global Tiles:** Absolutely AVOID tile names like 'malaysia_city', 'pakistan_farmland', 'china_great_wall', etc. The map is EXCLUSIVELY about {location} and its immediate Delhi surroundings. The large list of diverse tiles you provided in the initial problem description should be seen as an example of JSON *formatting* for tiles, NOT a list to pick from for *this specific Dwarka map*.

    Consider the provided backstory and protagonist's location when populating the map with relevant details.
    """
    print(specifications_worldgen)

    return specifications_worldgen

print(specifications(backstory, protagonist, location, theme_description))