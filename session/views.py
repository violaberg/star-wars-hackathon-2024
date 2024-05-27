from django.shortcuts import redirect, reverse, render
from .forms import SessionForm
from .models import Character


def session_create(request):
    """ 
    A view when user can select a meditation option
    and redirect to meditation page
    """
    star_characters = Character.objects.all()
    character_count = star_characters.count()

    if request.method == "POST":
        session_form = SessionForm(request.POST)
        if session_form.is_valid():
            session = session_form.save(commit=False)
            session.session_user = request.user
            session.character = request.POST.get('name')
            session.medition_selected = ''
            if request.POST.get('meditation_one_name') is None:
                session.medition_selected = request.POST.get('meditation_two_name')
            else:
                session.medition_selected = request.POST.get('meditation_one_name')
            session.save()
            return redirect(reverse('meditation-begins') + f"?level={session.get_level_display()}&character={session.character}&username={session.session_user.username}&med={session.medition_selected}")
    else:
        session_form = SessionForm()
    return render(
        request,
        "session/session_start.html",
        {
            "session_form": session_form,
            "star_characters":star_characters,
        }
    )


def meditation(request):
    """ 
    A view where meditation begins
    """
    character = request.GET.get('character')
    username = request.GET.get('username')
    level = request.GET.get('level')
    meditation = request.GET.get('med')
    context = {
        'character': character,
        'username': username,
        'level':level,
        'meditation':meditation,
    }
    return render(request, "session/meditation_begin.html", context)
