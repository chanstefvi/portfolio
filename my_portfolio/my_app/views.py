from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'my_app/index.html')


def about(request):
    return render(request,'my_app/about.html')


def contact(request):
    return render(request,'my_app/contact.html')


def relative(request):
    return render(request,'my_app/relative.html')