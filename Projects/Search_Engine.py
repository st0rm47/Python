###--->Creating a Search Engine

def search(text, word):
    text_lower = text.lower()
    word_lower = word.lower()

    if word_lower in text_lower:
        index = text_lower.index(word_lower)
        return f"Found '{word}' at index {index} in the text."
    else:
        return "Oops, Sorry! Word not found in the text."

text = input("Enter your text: ")
word = input("Enter your word: ")

print(search(text, word))
