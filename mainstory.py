import ai
import prompts

sno = int(input("Enter a number from 1-4: "))

ai.generate(prompts.main_story, rf"Storage\Saveslots\{sno}\backstory.json", "the protagonist is named shreyansh, who lives in delhi") # generates the backstory