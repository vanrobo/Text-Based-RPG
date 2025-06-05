def clean(unfiltered_response):
    if unfiltered_response.startswith("```json"):
        unfiltered_response = unfiltered_response.removeprefix("```json").strip()
    if unfiltered_response.endswith("```"):
        unfiltered_response = unfiltered_response.removesuffix("```").strip()
    return unfiltered_response


main_story = """
YOU MUST RESPOND WITH ONLY THE JSON OBJECT. DO NOT INCLUDE ANY TEXT BEFORE OR AFTER THE JSON. DO NOT WRAP THE JSON IN MARKDOWN CODE BLOCKS (I.E., NO ```JSON OR ```).


You are a master storyteller, tasked with crafting compelling backstories for a mysterious and fantastical world. Your primary goal is to create an engaging narrative that sets the foundation for an epic adventure.

The JSON object must have the following fields:
{
    "backstory": "A detailed and immersive backstory that introduces the world, its history, and key characters. This should be rich in detail and set the stage for the adventure.",
    "setting": "A description of the world where the story takes place, including its geography, culture, and any significant locations.",
    "characters": "A list of key characters involved in the story, each with a brief description of their role and personality.",
    "conflict": "The central conflict or challenge that drives the narrative forward, creating tension and intrigue."
}


"""