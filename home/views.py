from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .models import Character
from .forms import HeroForm


class Home(View):
    def get(self, request):
        characters = Character.objects.all()
        ctx = {'characters': characters}
        return render(request, 'home/index.html', ctx)


class Watch(View):
    def get(self, request):
        characters = Character.objects.all()
        ctx = {'characters': characters}
        return render(request, 'home/show_char.html', ctx)


class HeroCreateView(LoginRequiredMixin, CreateView):
    model = Character
    form_class = HeroForm
    success_url = reverse_lazy('watcher:watch')

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs


class HeroUpdateView(LoginRequiredMixin, UpdateView):
    model = Character
    form_class = HeroForm
    success_url = reverse_lazy('watcher:watch')


class HeroDetailView(LoginRequiredMixin, DetailView):
    model = Character
