class StringProcessor:
    def __init__(self, value):
        self.value = value
    
    def reverse(self):
        return self.value[::-1]
    
    def capitalize(self):
        return self.value.capitalize()
