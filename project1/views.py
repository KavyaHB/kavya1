from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>well come to html  home page</h1>")
    