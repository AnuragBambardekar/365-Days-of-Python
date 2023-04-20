from nltk.sentiment import SentimentIntensityAnalyzer
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float

def get_mood(input_text: str) -> Mood:
    sia = SentimentIntensityAnalyzer()
    sentiment_dict = sia.polarity_scores(input_text)
    sentiment: float = sentiment_dict['compound']

    if sentiment >= 0.5:
        return Mood('😁', sentiment)
    elif sentiment <= -0.5:
        return Mood('😠', sentiment)
    else:
        return Mood('😐', sentiment)
    

if __name__ == "__main__":
    while True:
        text: str = input("Text: ")
        mood: Mood = get_mood(text)

        print(f'{mood.emoji} ({mood.sentiment})')
