import re

def extract_phone_numbers(text):
    # Improved regular expression to find phone numbers with various formats
    phone_pattern = r'\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}|\b\d{3}\.\d{3}\.\d{4}\b|\(\d{3}\)\s\d{3}-\d{4}'

    """
    \+?: Match 0 or 1 occurrence of the plus sign +.
    \d{1,3}: Match 1 to 3 digits (country code).
    [-.\s]?: Match 0 or 1 occurrence of a hyphen, period, or whitespace character.
    \(?\d{3}\)?: Match 3 digits inside optional parentheses (area code).
    [-.\s]?: Match 0 or 1 occurrence of a hyphen, period, or whitespace character.
    \d{3}: Match 3 digits (the first part of the phone number).
    [-.\s]?: Match 0 or 1 occurrence of a hyphen, period, or whitespace character.
    \d{4}: Match 4 digits (the second part of the phone number).
    """

    phone_numbers = re.findall(phone_pattern, text)
    return phone_numbers

def clean_phone_numbers(numbers):
    # Remove any non-digit characters from the phone numbers
    return [re.sub(r'\D', '', number) for number in numbers]

if __name__ == "__main__":
    sample_text = """
    Here are some phone numbers:
    +1-123-456-7890
    555.123.4567
    (123) 456-7890
    +91 9876543210
    +1 (732) 522-6946
    001-800-555-1234
    """

    print("Sample Text:")
    print(sample_text)

    numbers = extract_phone_numbers(sample_text)
    print(numbers)
    cleaned_numbers = clean_phone_numbers(numbers)

    if cleaned_numbers:
        print("\nExtracted Phone Numbers:")
        for number in cleaned_numbers:
            print(number)
    else:
        print("\nNo phone numbers found in the text.")
