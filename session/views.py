from django.shortcuts import render

# Create your views here.
def session_create(request):
    return render(
        request,
        "session/session_start.html"
    )