# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponse, Http404
from .models import DebateTopic, Friend, Point
from django.template import loader
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from .forms import RegistrationForm, EditProfileForm, UserProfileRegForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse
from haystack.query import SearchQuerySet
from django.contrib.auth.models import User
from friendship.models import Friend, Follow

#Generic view classes
class IndexView(generic.ListView):
    template_name = "debate/index.html"

    def get_queryset(self):
        return DebateTopic.objects.all()

class FindFriends(generic.ListView):
    template_name = "debate/find_friends.html"

    def get_queryset(self):
        return User.objects.all().exclude(username=self.request.user.username)

class DetailView(generic.DetailView):
    model = DebateTopic
    template_name = "debate/detail.html"

#DebateTopic view classes
class DebateTopicCreate(CreateView):
    model = DebateTopic
    fields = ['topic', 'description', 'article_URL', 'photo', 'tags']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DebateTopicCreate, self).form_valid(form)

class DebateTopicEdit(UpdateView):
    model = DebateTopic
    fields = ['topic', 'description']

class DebateTopicDelete(DeleteView):
    model = DebateTopic
    success_url = reverse_lazy('debate:index')

#register view func
class Register(View):
    template_name = 'debate/reg_form.html'
    form_class = RegistrationForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            user.set_password(password)
            user.save()


            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/debate/register/user_profile/')
        return render(request, self.template_name, {'form':form})

class RegisterUserProfile(View):
    template_name = 'debate/profile_reg_form.html'
    form_class = UserProfileRegForm

    def get(self, request):
        user = request.user
        userprofile = request.user.profile
        form = self.form_class(request.POST, instance=userprofile)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()

            return redirect('/debate')
        return render(request, self.template_name, {'form': form})




#debate view func
class ProfileView(generic.TemplateView):
    template_name = "debate/profile.html"

    def get(self, request, **kwargs):
        task_id = self.kwargs.get('pk', None)
        if task_id:
            user = User.objects.get(pk=task_id)
        else:
            user = request.user
        user_debates = user.debatetopic_set.all()
        # friend = Friend.objects.get(current_user=request.user)
        # friends = friend.users.all().order_by('first_name', 'last_name')
        get_friends = Friend.objects.friends(request.user)
        args = {'user' : user,  'user_debates': user_debates, "get_friends" : get_friends}
        return render(request, self.template_name, args)


def add_comment_to_post(request, pk):
    debate = get_object_or_404(DebateTopic, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.debate = debate
            comment.author = request.user
            comment.save()
            return redirect('debate:detail', pk=debate.pk)
    else:
        form = CommentForm()
    return render_to_response('debate/create_comment.html', {'form': form}, request)



def profile_edit(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/debate/profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'debate/profile_edit.html', args)

def change_friends(request, operation, pk):
    new_friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, new_friend)
    elif operation == 'remove':
        Friend.remove_friend(request.user, new_friend)
    return redirect('debate:profile')

def search_titles(request):
    debate_names = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))

    return render_to_response('debate/ajax_search.html', {'debate_names' : debate_names})








