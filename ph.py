#!/usr/bin/env python3
import sys
from wonderwords import RandomWord

def generate_phrases(num_phrases=12, words_per_phrase=3):
    r = RandomWord()
    phrases = []
    for _ in range(num_phrases):
        words = [r.word() for _ in range(words_per_phrase)]
        phrase = ' '.join(words)
        phrases.append(phrase)
    return phrases

def main():
    # Optional: accept number of phrases and words per phrase from CLI arguments
    num_phrases = 12
    words_per_phrase = 3
    if len(sys.argv) > 1:
        try:
            num_phrases = int(sys.argv[1])
        except ValueError:
            pass
    if len(sys.argv) > 2:
        try:
            words_per_phrase = int(sys.argv[2])
        except ValueError:
            pass

    phrases = generate_phrases(num_phrases, words_per_phrase)
    for phrase in phrases:
        print(phrase)

if __name__ == "__main__":
    main()
