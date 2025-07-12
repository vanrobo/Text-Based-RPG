import ai
import prompts

def generate_backstory(sno, data="The User has entered no backstory, generate a random one."):
    ai.generate(prompts.back_story, rf"Storage\Saveslots\{sno}\backstory.json", data) # generates the backstory