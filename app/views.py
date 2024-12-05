from django.shortcuts import render

# Create your views here.
def function(request):
    d = {'name':'gani','age':20}
    return render(request,'sesu.html',context=d)