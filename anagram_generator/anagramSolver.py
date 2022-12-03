from itertools import permutations




class AnagramSolver :    
    def __init__(self, word):
        self.word = word.lower()

    def get_words(self):
        file = open('words_alpha.txt', 'r')
        content = file.read()
        words_list =content.split('\n')
        file.close()
        temp_word_list = [ w for w in words_list if(2<len(w)) and (len(w)<=len(self.word)) ]
        return temp_word_list
        
    def permutate_string(self):
        res = []
        for i in range(3, len(self.word)+1):
            res += (permutations(self.word, i)) #permutates starting from three letter words
        perm = [''.join(i) for i in res] #turns the inner tuples to single string
        return perm

    def get_anagram(self):
        valid_words = (self.get_words()) 
        perm_list = (self.permutate_string())
        
        result = [word for word in perm_list if word in valid_words]
        result = sorted(set(result))
        return (result)
        
        
        """ 
            eleminating two letter words and words greater than length of the string
            possible_words = [i for i in valid_words if (len(i) > 2) and (len(i) <= len(self.word)) ]
            result = [i for i in perm_list if i in possible_words] 
        """
        
""" def load_words():
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    with open('words_alpha.txt') as word_file:
        all_words = set(word_file.read().split()) #set to remove duplicates
        #remove words without vowels
        english_words = [word for letter in vowels for word in all_words if letter in word]
    return english_words """
    
""" vowels = ('a', 'e', 'i', 'o', 'u', 'y')
with open('words_alpha.txt') as word_file:
    with open('new_file', 'w') as output:
        for letter in vowels:
            for word in word_file:
                if letter in word:
                    output.write(word) """