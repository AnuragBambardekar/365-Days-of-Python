from collections import UserString

class LocalizedString(UserString):
    translations = {
        'hello': {
            'en': 'Hello',
            'fr': 'Bonjour',
            'es': 'Hola'
        },
        'apples': {
            'en': 'apples',
            'fr': 'pommes',
            'es': 'manzanas'
        },
        # Add more translations for other strings and languages
    }

    def __init__(self, text, language='en'):
        super().__init__(self.translate(text, language))

    @staticmethod
    def translate(text, language):
        if text in LocalizedString.translations:
            if language in LocalizedString.translations[text]:
                return LocalizedString.translations[text][language]
        return text

# Create a localized string object
localized_hello = LocalizedString('hello', language='fr')
localized_apples = LocalizedString('apples', language='es')

# Print the localized strings
print(localized_hello)  # Output: Bonjour
print(localized_apples)  # Output: manzanas
