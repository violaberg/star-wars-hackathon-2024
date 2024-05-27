from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, UserMeditationSession
from .forms import UserProfileForm, UserForm


@login_required
def profile(request):
    user_profile = request.user.userprofile
    meditation_sessions = UserMeditationSession.objects.filter(user=request.user)
    return render(request, 'userprofile/profile.html', {
        'user_profile': user_profile,
        'meditation_sessions': meditation_sessions
    })


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'userprofile/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
