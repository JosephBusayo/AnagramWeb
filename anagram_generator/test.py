import unittest
from anagramSolver import AnagramSolver

class TestAnagramSolver(unittest.TestCase):
    
    def test_permutate_string(self):
        anagram = AnagramSolver("orb")
        result = anagram.permutate_string()
        self.assertEqual(result, ['orb', 'obr', 'rob', 'rbo', 'bor', 'bro'] )
        
    
    def test_get_anagram(self):
        anagram = AnagramSolver("orb")
        result = anagram.get_anagram()
        self.assertEqual(result, {'rob', 'bro', 'bor', 'orb'})
        
    
if __name__ == '__main__':
    unittest.main()