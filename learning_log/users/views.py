from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)
