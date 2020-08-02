from django.urls import path

from .views import TextAnalyzerView, textview


urlpatterns = [
    path('', TextAnalyzerView.as_view(), name='text_analyzer'),
]