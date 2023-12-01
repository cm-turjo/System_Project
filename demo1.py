import pytesseract

def convert_to_bengali_words(number):
    # Use pytesseract to convert the number to Bengali words
    bengali_words = pytesseract.image_to_string(f"{number}.png", lang="ben")
    return bengali_words

# Example usage
eng_num = 1895
ben_words = convert_to_bengali_words(eng_num)
print(ben_words)
