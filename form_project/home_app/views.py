from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from . import forms_self
from .models import UserInfo

# Create your views here.
def home(request):
    form = forms_self.UserInfoForm()
    if request.is_ajax():
        form = forms_self.UserInfoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return JsonResponse({
                'message': 'success'
            })
    if request.method == 'POST':
        form = forms_self.UserInfoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request, 'home.html', {'form':form})

def user_list(request):
    users = UserInfo.objects.all()
    return render(request, 'list.html', {'users':users})

def delete(request, pk):
    del_user = UserInfo.objects.get(pk=pk)
    del_user.delete()
    users = UserInfo.objects.all()
    return render(request, 'list.html', {'users':users})