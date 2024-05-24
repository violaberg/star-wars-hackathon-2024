from django.shortcuts import redirect, reverse, render
from .forms import SessionForm

def session_create(request):
    if request.method == "POST":
        session_form = SessionForm(request.POST)
        if session_form.is_valid():
            session = session_form.save(commit=False)
            session.session_user = request.user
            session.save()
            return redirect(reverse('meditation-begins') + f"?session_name={session.session_name}&level={session.get_level_display()}&character={session.get_character_display()}&username={session.session_user.username}")
    else:
        session_form = SessionForm()
    return render(
        request,
        "session/session_start.html",
        {
            "session_form": session_form,
        }
    )

def meditation(request):
    session_name = request.GET.get('session_name')
    character = request.GET.get('character')
    username = request.GET.get('username')
    level = request.GET.get('level')
    context = {
        'session_name': session_name,
        'character': character,
        'username': username,
        'level':level,
    }
    return render(request, "session/meditation_begin.html", context)
