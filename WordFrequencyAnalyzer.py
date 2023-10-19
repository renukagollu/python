""" Implementation of WordFrequencyAnalyzer Interface."""
from collections import Counter
from typing import List, Tuple


class WordFrequency:
    """
    Represents a word and its frequency.
    Attributes:
        word (str): The word itself.
        frequency (int): The frequency or count of the word in the text.
    """
    def __init__(self, word: str, frequency: int):
        self.word = word
        self.frequency = frequency


class WordFrequencyAnalyzer:
    @staticmethod
    def calculate_highest_frequency(text: str) -> int:
        """ Calculate the highest frequency of any word in the input text.
            Args:
                text (str): The input text.
            return:
                int: max frequency of word.
        """
        word_counts = WordFrequencyAnalyzer.get_word_counts(text)
        if not word_counts:
            return 0
        return max(word_counts.values())

    @staticmethod
    def calculate_frequency_for_word(text: str, word: str) -> int:
        """ Calculate the frequency of a specific word in the input text.
            Args:
                text (str): The input text.
                word (str): The word for which to calculate the frequency.
            return:
                int: The frequency of the specified word in the text.
        """
        word_counts = WordFrequencyAnalyzer.get_word_counts(text)
        return word_counts.get(word.lower(), 0)

    @staticmethod
    def calculate_most_frequent_n_words(text: str, n: int) -> List[WordFrequency]:
        """ Calculate the most frequent n words in the text.
            Args:
                text (str): The input text.
                n (int): The number of most frequent words to retrieve.
            return:
                List[WordFrequency]: A list of WordFrequency objects representing the most frequent words.
        """
        word_counts = WordFrequencyAnalyzer.get_word_counts(text)
        if not word_counts:
            return []

        sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0].lower()))
        most_frequent_n_words = sorted_word_counts[:n]
        return most_frequent_n_words

    @staticmethod
    def get_word_counts(text: str) -> dict:
        """ Calculate word frequencies in the input text.
            Args:
                text: The input text.
            return:
                dict: A dictionary where keys are words and values are their frequencies.
        """
        words = WordFrequencyAnalyzer.extract_words(text)
        return dict(Counter(words))

    @staticmethod
    def extract_words(text: str) -> List[str]:
        """ Extract words from the input text.
            Args:
                text: The input text.
            return:
                List[str]: A list of words in lowercase.
        """
        text = text.lower()
        return [word.strip(".,!?") for word in text.split() if word.isalpha()]



# Example usage and test cases
# input_text = """I'm in the Netharlands, because i'm not in India. 
# If this code is working in fine condition, it will provide me an oppurtunity in the Netharlands """
# #"The sun shines over the lake"
# analyzer = WordFrequencyAnalyzer()

# print("Highest Frequency:", analyzer.calculate_highest_frequency(input_text))
# print("Frequency for 'the':", analyzer.calculate_frequency_for_word(input_text, "i'm"))
# print("Most frequent 2 words:", analyzer.calculate_most_frequent_n_words(input_text, 2))


