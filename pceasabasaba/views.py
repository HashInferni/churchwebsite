from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pceasabasaba/index.html')

def about(request):
    return render(request, 'pceasabasaba/about.html')

def services(request):
    return render(request, 'pceasabasaba/property-grid.html')

def projects(request):
    return render(request, 'pceasabasaba/blog-grid.html')

def church_school(request):
    return render(request, 'pceasabasaba/property-single.html')

def brigade(request):
    return render(request, 'pceasabasaba/property-single.html')

def youth_fellowship(request):
    return render(request, 'pceasabasaba/property-single.html')

def womans_guild(request):
    return render(request, 'pceasabasaba/property-single.html')

def pcmf(request):
    return render(request, 'pceasabasaba/property-single.html')

def choirs(request):
    return render(request, 'pceasabasaba/property-single.html')


def contact(request):
    return render(request, 'pceasabasaba/contact.html')