import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
                content = content.lower()
                translator = str.maketrans('', '', string.punctuation.replace("'", ""))
                cleaned_content = content.translate(translator)
                words = cleaned_content.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        found_positions = {}
        word = word.lower()
        for file_name, words in all_words.items():
            if word in words:
                found_positions[file_name] = words.index(word) + 1
        return found_positions

    def count(self, word):
        all_words = self.get_all_words()
        word_counts = {}
        word = word.lower()
        for file_name, words in all_words.items():
            word_counts[file_name] = words.count(word)
        return word_counts

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))