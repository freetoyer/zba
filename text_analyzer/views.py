from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

import re

from .forms import TextForm


class TextAnalyzerView(View):
    def get(self, request):
        form = TextForm()
        return render(request, 'text_analyzer.html', {'form': form})
    
    def post(self, request):
        text = request.POST.get('text')
        text = re.sub('.*&text=', '', text)
        return JsonResponse({
            'text': text
            })


    

