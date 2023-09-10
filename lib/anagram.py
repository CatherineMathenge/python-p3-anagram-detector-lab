class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        # Filter words from word_list that are anagrams of self.word
        return [word for word in word_list if self.is_anagram(word)]

    def is_anagram(self, other_word):
        # Check if two words are anagrams
        return sorted(self.word.lower()) == sorted(other_word.lower())

# Example usage:
# anagram = Anagram("enlist")
# matches = anagram.match(["listen", "silent", "hippopotamus"])
# print(matches)  # Output will be ["listen", "silent"] for this example
