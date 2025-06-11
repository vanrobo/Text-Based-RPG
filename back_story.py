import ai
import prompts

sno = int(input("Enter a number from 1-4: "))

ai.generate(prompts.back_story, rf"Storage\Saveslots\{sno}\backstory.json", "the protagonist is a micro organism on a small asteroid drifting around the sun") # generates the backstory