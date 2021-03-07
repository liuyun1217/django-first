from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def home(request):
    return render(request, 'liaotian/home.html')


def main(request):
    return render(request, 'liaotian/main.html')
