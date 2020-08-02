from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse
from django.views import View

import re

from .forms import TextForm


class TextAnalyzerView(View):
    def get(self, request):
        form = TextForm()
        return render(request, 'text_analyzer.html', {'form': form})
    
    def post(self, request):
        # form = TextForm(request.POST)
        # if form.is_valid():
        #     text = form.cleaned_data
        #     return HttpResponseRedirect(reverse('text', args=(text,)))
        text = request.POST.get('text')
        text = re.sub('.*&text=', '', text)
        return JsonResponse({
            'text': text
            })
        
        
def textview(request, text):
    return render(request, 'text.html')

    

