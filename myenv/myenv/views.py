from django.shortcuts import render, HttpResponse
from .forms import student

def forms(request):
    data = {}
    d= student()
    try: 
        data = {

            'f': d
        }
    except:
        pass
    return render(request, 'forms.html',data)

def home(request):
    return render(request, 'index.html')

def port(request):
    return render(request, 'portfolio.html')

def about(request):
    return render(request, 'about.html')

def ser(request):
    return render(request, 'services.html')

def contact(request):
    try:
        n1 = request.POST.get('name')
        n2 = request.POST.get('email')
        n3 = request.POST.get('subject')
        n4 = request.POST.get('message')
        dic ={
            'a': n1,
            'b': n2,
            'c': n3,
            'd': n4
        }
    except:
        pass
    return render(request, 'contact.html', dic)

# def port(request):
#     return render(request, 'portfolio.html')

# def port(request):
#     return render(request, 'portfolio.html')

    # try:
    #     n1 = request.POST.get['fname']
    #     n2 = request.POST.get['lname']
    #     data = {
    #         'a': n1,
    #         'b': n2,
    #         'f': d
    #     }
    # except:
    #     pass





    # n1 = request.GET.get('name')
    # n2 = request.GET.get('email')
    # n3 = request.GET.get('subject')
    # n4 = request.GET.get('message')
    # print(n1)
    # print(n2)
    # dic ={
    #     'a': n1,
    #     'b': n2,
    #     'c': n3,
    #     'd': n4
    #  }


    # return render(request, 'forms.html', {'d':d})