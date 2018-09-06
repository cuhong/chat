from django import forms
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

class NickNameForm(forms.Form):
    nickname = forms.CharField()

class Chat_setusername(View):
    def get(self, request, *args, **kwargs):
        form = NickNameForm()
        return render(request, 'set_username.html', context=dict(form=form))

    def post(self, request, *args, **kwargs):
        form = NickNameForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            request.session['nickname'] = nickname
            return redirect(reverse('chat'))
        else:
            return render(request, reverse('main'))

class Chat(View):
    def get(self, request, *args, **kwargs):
        if request.session['nickname'] is None:
            return render(request, reverse('main'))
        else:
            nickname = request.session['nickname']
            return render(request, template_name='chat.html', context=dict(nickname=nickname))