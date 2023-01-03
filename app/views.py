from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':0,'b':11,'c':99}
    return render(request,'operations.html',d)
    
