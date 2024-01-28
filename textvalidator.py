class TextValidator:
    def validate_text(self, text):
        invalid_chars = set(',_#*')
        if any((char in invalid_chars) for char in text):
            return False
