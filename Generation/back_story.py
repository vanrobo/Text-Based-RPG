import ai
import prompts

def generate_backstory(sno,protag_name, data="The User has entered no backstory, generate a random one."):
    data.join(f"The Protagonist's name is {protag_name}")
    ai.generate(prompts.back_story, rf"Storage\Saveslots\{sno}\backstory.json", data) # generates the backstory

def generate_backstory_lite(sno,protag_name, data="The User has entered no backstory, generate a random one."):
    data.join(f"The Protagonist's name is {protag_name}")
    ai.generatelite(prompts.back_story, rf"Storage\Saveslots\{sno}\backstory.json", data) # generates the backstory