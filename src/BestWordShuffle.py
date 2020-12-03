import random

class BestWordShuffle:

    def __init__(self):
        self.score = 0
        self.original_word = ""
        self.shuffled_word = ""

    def shuffle_score(self):
        count = 0
        for i in range(0, len(self.original_word)):
            if self.shuffled_word[i] == self.original_word[i]:
                count += 1

        return count

    # def shuffle(self, word):
    #     """
    #     This is first logic for getting the best word shuffle. But it somehow fails as the length of the
    #     words increase along with words with repetitive letters in it. So we need a better logic.
    #     """
    #     self.original_word = word
    #     word_length = len(self.original_word)
    #     word_list = [None] * word_length
    #
    #     for word_char_index in range(0, word_length):
    #         if word_char_index+1 != word_length:
    #             word_list[word_char_index] = self.original_word[word_char_index+1]
    #         else:
    #             word_list[word_char_index] = self.original_word[0]
    #     self.shuffled_word = ''.join(word_list)

    def shuffle(self, word):
        self.original_word = word
        original_word_length = len(self.original_word)

        # Define an empty list of None of same length as original word
        shuffle_word_list = [None] * original_word_length

        # Create the character-to-index map
        char_to_index_map = self.get_char_to_index_map(word)

        # Shuffle logic
        if original_word_length == 1:
            self.shuffled_word = self.original_word
        elif original_word_length == 2:
            if len(list(set(self.original_word))) == 1:
                self.shuffled_word = self.original_word
            else:
                # Now shuffle
                pass

    def do_shuffle(self, word, word_length, shuffle_word_list):

        # Create char-to-index map
        char_to_index_map = self.get_char_to_index_map(word)

        for ch in char_to_index_map.keys():
            # get index of char in original word
            index_position_in_original_word_for_char = char_to_index_map[ch]
            if len(index_position_in_original_word_for_char) > 1:
                print("The letter is getting repeated.")
            else:
                print("The letter is not getting repeated.")
                available_indexes = [av_i for av_i in range(0,word_length) if av_i not in
                                     index_position_in_original_word_for_char]
                shuffle_word_list[random.choice(available_indexes)] = ch

        return shuffle_word_list


    def get_char_to_index_map(self, word):
        # Find distinct characters in word
        distinct_chars = list(set(word))

        char_to_index = {}

        for ch in distinct_chars:
            char_to_index[ch] = self.get_char_index(word, ch)

        return char_to_index


    def get_char_index(self, word, ch):
        return [index for index, ltr in enumerate(word) if ltr == ch]
