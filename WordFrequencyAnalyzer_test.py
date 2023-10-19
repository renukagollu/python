"""Test cases for WordFrequencyAnalyzer."""
import WordFrequencyAnalyzer
import unittest
from unittest import mock
class TestWordFrequencyAnalyzer(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.analyzer = WordFrequencyAnalyzer.WordFrequencyAnalyzer()
        
    
    @mock.patch.object(
            WordFrequencyAnalyzer.WordFrequencyAnalyzer, 'get_word_counts', autospec=True,
            return_value={'the': 2, 'sun': 1, 'shines': 1, 'over': 1, 'lake': 1})
    def test_calculate_highest_frequency(self,mock_get_word_count):
        input_text = "The sun shines over the lake."
        # Run Function
        result = self.analyzer.calculate_highest_frequency(input_text)
        # Verify
        self.assertEqual(result, 2)
        mock_get_word_count.assert_called_once()
    

    @mock.patch.object(
            WordFrequencyAnalyzer.WordFrequencyAnalyzer, 'get_word_counts', autospec=True,
            return_value={'the': 3, 'sun': 1, 'shines': 1, 'over': 1, 'lake': 1})
    def test_calculate_frequency_for_word(self,mock_get_word_count):
        input_text = "The sun shines over the lake."
        # Run Function
        result = self.analyzer.calculate_frequency_for_word(input_text, 'the')
        # Verify
        self.assertEqual(result, 3)  # 'the' appears 4 times
        mock_get_word_count.assert_called_once()
    

    @mock.patch.object(
            WordFrequencyAnalyzer.WordFrequencyAnalyzer, 'get_word_counts', autospec=True,
            return_value={'the': 2, 'sun': 1, 'shines': 1, 'over': 1, 'lake': 1})
    def test_calculate_most_frequent_n_words(self,mock_get_word_count):
        input_text = "The sun shines over the lake."
        expected = [('the', 2),('lake', 1),('over', 1)]
        # Run Function
        result = self.analyzer.calculate_most_frequent_n_words(input_text, 3)
        # Verify
        self.assertEqual(result, expected)
        mock_get_word_count.assert_called_once()


    @mock.patch.object(
            WordFrequencyAnalyzer.WordFrequencyAnalyzer, 'extract_words', autospec=True,
            return_value=['the', 'sun', 'shines', 'over', 'the', 'lake'])
    def test_get_word_counts(self,mock_extract_words):
        input_text = "The sun shines over the lake."
        # Run Function
        result = self.analyzer.get_word_counts(input_text)
        # Verify
        self.assertEqual(len(result),5)
        mock_extract_words.assert_called_once()
    

    def test_extract_words(self):
        input_text = "The sun shines over the lake."
        # Run Function
        result = self.analyzer.extract_words(input_text)
        # Verify
        self.assertEqual(type(result),list)


if __name__ == '__main__':
    unittest.main()