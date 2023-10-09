from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import item
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)


class ItemListView(LoginRequiredMixin, ListView):
    model = item
    template_name = 'item_list.html'
    login_url = 'login'


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = item
    template_name = 'item_detail.html'
    login_url = 'login'


class ItemUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = item
    field = ('title', 'description', 'price')
    template_name = 'item_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.seller == self.request.user


class ItemDeleteView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = item
    template_name = 'item_delete.html'
    success_url = reverse_lazy('item_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.seller == self.request.user


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = item
    template_name = 'item_new.html'
    fields = ('title', 'description', 'seller', 'price', 'photo')
    success_url = reverse_lazy('item_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)
