from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from shop_app.models import Item
from django.utils import timezone
from seller_app.forms import ItemForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView

# Create your views here.


#

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = "seller/item_create.html"
    form_class = ItemForm
    success_url = reverse_lazy("seller:draft-list")

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = "seller/item_list.html"
    queryset = Item.objects.filter(listed_at__isnull=False)
    context_object_name = "items"


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "seller/item_detail.html"
    context_object_name = "item"

    def get_queryset(self):
        queryset = Item.objects.filter(pk=self.kwargs["pk"], listed_at__isnull=False)
        return queryset


class DraftListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = "seller/draft_list.html"
    queryset = Item.objects.filter(listed_at__isnull=True)
    context_object_name = "items"


class DraftDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "seller/draft_detail.html"
    context_object_name = "item"

    def get_queryset(self):
        queryset = Item.objects.filter(pk=self.kwargs["pk"], listed_at__isnull=True)
        return queryset


class DraftPublishView(LoginRequiredMixin, View):
    def get(self, request, pk):
        item = Item.objects.get(pk=pk, listed_at__isnull=True)
        item.listed_at = timezone.now()
        item.save()
        return redirect("seller:draft-list")


class ItemDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        item.delete()
        return redirect("seller:item-list")


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = "seller/item_create.html"
    form_class = ItemForm

    def get_success_url(self):
        item = self.get_object()  # jun item maile update garna khojdai xu
        if item.listed_at:
            return reverse_lazy("seller:item-detail", kwargs={"pk": item.pk})
        else:
            return reverse_lazy("seller:draft-detail", kwargs={"pk": item.pk})