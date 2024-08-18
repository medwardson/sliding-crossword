from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_crossword_hints(words):
    hints = []
    for word in words:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a program that creates crosswords."},
                {"role": "user", "content": f"Write a crossword hint for the word '{word}'. Only give the hint, don't prefix it with 'A clue for' or anything similar."}
            ]
        )
        hint = completion.choices[0].message.content
        hints.append(hint)
    return hints

# Example usage
# words = ["haiku", "puzzle", "python"]
# hints = generate_crossword_hints(words)
