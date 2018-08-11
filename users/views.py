from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    logout(request)
    return redirect('blog:post_list')


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'users/register.html', context)
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(
                username=new_user.username,
                password=request.POST['password1']
            )
            login(request, authenticated_user)
            return redirect('blog:post_list')
