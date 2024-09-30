from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'text': 'Wellcome to My Home',
    }
    return  render (request,'home/index.html',context)
