import time

def calculate_wpm(words_typed, time_elapsed):
    minutes_elapsed = time_elapsed / 60.0
    wpm = words_typed / minutes_elapsed
    return wpm

def calculate_accuracy(sentence, user_input):
    sentence_words = sentence.split()
    user_words = user_input.split()
    num_correct = 0
    for i in range(min(len(sentence_words), len(user_words))):
        if sentence_words[i] == user_words[i]:
            num_correct += 1
    accuracy = (num_correct / len(sentence_words)) * 100.0
    return accuracy

def main():
    print("Type the following sentence:")
    sentence = "The quick brown fox jumps over the lazy dog"
    print(sentence)
    
    input("Press Enter to start the timer...")
    
    start_time = time.time()
    
    user_input = input("Type the sentence above and press Enter when done:\n")
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    words_typed = len(user_input.split())
    
    wpm = calculate_wpm(words_typed, time_elapsed)
    
    accuracy = calculate_accuracy(sentence, user_input)
    
    print(f"You typed {words_typed} words in {time_elapsed:.2f} seconds.")
    print(f"That's a typing speed of {wpm:.2f} words per minute!")
    print(f"Your accuracy was {accuracy:.2f}%.")

if __name__ == "__main__":
    main()
