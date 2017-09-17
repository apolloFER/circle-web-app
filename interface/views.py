from django.shortcuts import render


# This is just for rendering the main view
def home(request):
    return render(request, "main.html")
