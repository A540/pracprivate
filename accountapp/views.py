from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello_world(request):
    if request.method == 'POST':
        return render(request, 'accountapp/helloworld.html', context={'text': 'POST MEHTOD!!!'})
    else:
        return render(request, 'accountapp/helloworld.html', context={'text': 'GET MEHTOD!!!'})
