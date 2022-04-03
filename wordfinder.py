"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Machine to read a file with a list of words and return a random word.
    
    >>> wf = WordFinder("words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """

    def __init__(self, file):
        "Select file to read all words inside a file"
        file_dir = open(file, 'r')
        self.words_find = self.read_file(file_dir)
        file_dir.close()
        
        print(f"{len(self.words_find)} words read")

    def read_file(self, file_dir):
        "Read each line on the file and return a list with all word find it"
        words_list = []
        for line in file_dir:
            words_list.append(line.strip())

        return words_list

    def random(self):
        "Return a random word from a words list."
        return random.choice(self.words_find)


class SpecialWordFinder(WordFinder):
    """Special WordFinder class excludes blank lines or comments on the lines.
    
    >>> swf = SpecialWordFinder("words.txt")
    3 words read

    """
    def special_read(self, file):
        "Read each line on the file and return a list with all word find it skipping blanks/comments."
        words_list = []
        for line in file:
            if line.strip() and not line.startswith("#"):
                words_list.append(line.strip())

        return words_list