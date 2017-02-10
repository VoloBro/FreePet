from django.shortcuts import render


def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request, 'personal/contact.html', {'contact': ['If you want to contact me, please email me', 'blabla@gmail.com']})
