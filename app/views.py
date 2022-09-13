from django.shortcuts import render
from django.views import View

from anagram_generator import anagramSolver



class Index(View):
    template_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        word = request.POST['searched_word']
        result = anagramSolver.AnagramSolver(word)
        words_list = result.get_anagram()
        
        return render(request, self.template_name, {'words_list': words_list})

""" def anagram(request):
    word = "cats"
    
    out = anagramSolver.AnagramSolver(word)
    print (out.get_anagram()) """