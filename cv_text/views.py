from django.shortcuts import render
from .models import Text, VJText

# Create your views here.
def index(request):
    text=Text.objects.all()
    return render(request, 'cv_text/mainCV.html', {'text':text})

def get_text(request):
    text=Text
    return render(request, 'cv_text/mainCV.html', {'text':text})

def indexvj(request):
    vjtext=VJText.objects.all()
    return render(request, 'cv_text/Viola_Jones.html', {'vjtext':vjtext})
