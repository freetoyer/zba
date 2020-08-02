from django.urls import path

from .views import TextAnalyzerView


urlpatterns = [
    path('', TextAnalyzerView.as_view(), name='text_analyzer'),
]