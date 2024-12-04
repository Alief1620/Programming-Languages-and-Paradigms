import re
from collections import Counter

stop_words = set(["i", "a", "the", "is", "in", "to", "of", "that", "this", "on", "for", "it", "with", "an", "as", "by"])


def analyze_text(text):
    paragraphs = text.split('\n')
    sentences = re.split(r'[.!?]', text)
    words = re.findall(r'\b\w+\b', text.lower())

    num_paragraphs = len(paragraphs)
    num_sentences = len(sentences)
    num_words = len(words)

    print(f"Liczba akapitow: {num_paragraphs}")
    print(f"Liczba zdan: {num_sentences}")
    print(f"Liczba slow: {num_words}")

    filtered_words = filter(lambda word: word not in stop_words, words)
    word_count = Counter(filtered_words)
    most_common_words = word_count.most_common(5)

    print("\nNajczesciej wystepujace slowa (bez stop words):")
    for word, count in most_common_words:
        print(f"{word}: {count} razy")

    def reverse_word(word):
        if word[0].lower() == 'a':
            return word[::-1]
        return word

    reversed_words = map(reverse_word, words)
    transformed_text = ' '.join(reversed_words)

    print("\nPrzeksztalcony tekst (slwa zaczynajace sie na 'a' lub 'A' sa odwrocone):")
    print(transformed_text)


text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"""

analyze_text(text)
