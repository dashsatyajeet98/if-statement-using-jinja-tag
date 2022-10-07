from django.shortcuts import render

# Create your views here.
def condition(request):
    d = {'a':10,'b':15,'c':65}
    return render(request,'condition.html',context=d)