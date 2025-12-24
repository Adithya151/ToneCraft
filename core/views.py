from django.shortcuts import render

# Create your views here.
from .utils import generate_suggestions

def home(request):
    context = {}

    if request.method == "POST":
        sentence = request.POST.get("sentence")
        detected, suggestions = generate_suggestions(sentence)

        context = {
            "sentence": sentence,
            "detected": detected,
            "suggestions": suggestions
        }

    return render(request, "index.html", context)

