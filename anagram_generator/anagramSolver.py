from itertools import permutations


def load_words():
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    with open('words_alpha.txt') as word_file:
        all_words = set(word_file.read().split()) #set to remove duplicates
        #remove words without vowels
        english_words = [word for letter in vowels for word in all_words if letter in word]
    return english_words

class AnagramSolver :    
    def __init__(self, word):
        self.word = word

    def permutate_string(self):
        res = []
        for i in range(3, len(self.word)+1):
            res += (permutations(self.word, i)) #permutates starting from three letter words
        perm = [''.join(i) for i in res] #turns the inner tuples to single string
        return perm

    def get_anagram(self):
        valid_words = (load_words()) #removing possible duplicates
        perm_list = (self.permutate_string())
        
        #eleminating two letter words and words greater than length of the string
        possible_words = [i for i in valid_words if (len(i) > 2) and (len(i) <= len(self.word)) ]
        result = [i for i in perm_list if i in possible_words]
        
        return (set(result))
