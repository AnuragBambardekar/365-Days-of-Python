# pip install textblob
from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float

def get_mood(input_text: str, *, threshold: float) -> Mood:
    sentiment: float = TextBlob(input_text).sentiment.polarity

    friendly_threshold: float = threshold
    hostile_threshold: float = -threshold

    if sentiment >= friendly_threshold:
        return Mood('😁', sentiment)
    elif sentiment <= hostile_threshold:
        return Mood('😠', sentiment)
    else:
        return Mood('😐', sentiment)
    

if __name__ == "__main__":
    while True:
        text: str = input("Text: ")
        mood: Mood = get_mood(text, threshold=0.3)

        print(f'{mood.emoji} ({mood.sentiment})')


'''
Text: I hate AI
😠 (-0.8)
Text: I'm feeling good today but its also the worst day of my life
😐 (-0.15000000000000002)
Text: Hello World
😐 (0.0)
Text: Starship is the best
😁 (1.0)
Text: i dont like mangoes
😐 (0.0)
Text: i hate mangoes
😠 (-0.8)
Text: lets gooo
😐 (0.0)
Text: i like NJ
😐 (0.0)
Text: i love apples
😁 (0.5)
'''