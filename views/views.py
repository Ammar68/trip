from django.shortcuts import render

main_template = "main.html"
contact_template = "contact.html"
about_template = "about.html"

def index(request):
    return render(request, main_template)

def contact(request):
    return render(request, contact_template)

def about(request):
    return render(request, about_template)
