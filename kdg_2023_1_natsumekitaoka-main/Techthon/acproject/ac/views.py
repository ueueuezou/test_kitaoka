from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    TemplateView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    )
from .models import News, Com, Comment, Link


class ListComView(LoginRequiredMixin, ListView):
    template_name = 'ac/communication.html'
    model = Com

class DetailComView(LoginRequiredMixin, DetailView):
    template_name = 'ac/communication_detail.html'
    model = Com

class CreateComView(LoginRequiredMixin, CreateView):
    template_name = 'ac/communication_create.html'
    model = Com
    fields = ('category', 'title', 'image', 'text')
    success_url = reverse_lazy('communication')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

class DeleteComView(LoginRequiredMixin, DeleteView):
    template_name = 'ac/communication_delete.html'
    model = Com
    success_url = reverse_lazy('communication')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied
        
        return obj

class UpdateComView(LoginRequiredMixin, UpdateView):
    template_name = 'ac/communication_update.html'
    model = Com
    fields = ('category', 'title', 'image', 'text')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied
        
        return obj
    
    def get_success_url(self):
        return reverse('communication_detail', kwargs={'pk': self.object.id})

class CreateCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ('com', 'text')
    template_name = 'ac/comment_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['com'] = Com.objects.get(pk=self.kwargs['com_id'])
        print(context)

        return context

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('communication_detail', kwargs={'pk': self.object.com.id})
    
class ListHomeView(ListView):
    template_name = 'ac/index.html'
    model = News

class TemplateAboutView(TemplateView):
    template_name = 'ac/about.html'

class ListOfficialView(ListView):
    template_name = 'ac/official.html'
    model = Link