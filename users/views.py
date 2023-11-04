from django.shortcuts import render, redirect
from django.contrib import messages

from users.forms import RegisterUserForm


def register_view(request):

    if request.method == 'POST':
        form = RegisterUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо за регистрацию.')
            return redirect('login')
        else:
            return redirect('register')
    else:
        form = RegisterUserForm()

    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)
