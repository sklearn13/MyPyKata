from src.BestWordShuffle import BestWordShuffle
from unittest.case import TestCase


class TestBestShuffle(TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.word_shuffle = BestWordShuffle()

    def test_one_shuffle(self):
        self.word_shuffle.shuffle('a')
        assert 1 == self.word_shuffle.shuffle_score()

    def test_two_shuffle(self):
        self.word_shuffle.shuffle('up')
        assert 0 == self.word_shuffle.shuffle_score()

    def test_two1_shuffle(self):
        self.word_shuffle.shuffle('aa')
        assert 2 == self.word_shuffle.shuffle_score()

    def test_three_shuffle(self):
        self.word_shuffle.shuffle('tat')
        assert 1 == self.word_shuffle.shuffle_score()

    def test_four_shuffle(self):
        self.word_shuffle.shuffle('seen')
        assert 0 == self.word_shuffle.shuffle_score()
