from datetime import timedelta, datetime
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.views.generic import ListView, TemplateView, View, DetailView
from django.contrib.auth.views import LoginView
from cart.models import CartItems, Cart
from shop_app.models import Item, Category, Brand
from shop_app.forms import NewsletterForm
from django.http import JsonResponse


# from django.views.generic.base import View


# Create your views here.
from django.db.models import Q

class Home(ListView):
    model = Item
    template_name = "eshop/index.html"
    context_object_name = "items"
    queryset = Item.objects.filter(status="in stock", listed_at__isnull=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

 
        context["on_sales"] = Item.objects.filter(listed_at__isnull=False).order_by("-discont_percent")[:4]
        context["recent_items"] = Item.objects.filter(listed_at__isnull=False).order_by("-listed_at")[:4]
        context["top_price"] = Item.objects.filter(listed_at__isnull=False).order_by("-price")[:4]
        context["mens_trending_itmes"] = Item.objects.filter(target_customer=1).order_by("-listed_at")[:4]
        context["womens_trending_itmes"] = Item.objects.filter(target_customer=2).order_by("-listed_at")[:4]

        return context
    


class UserLoginView(LoginView):
    template_name = "registration/user_login.html"
    # Customize any other settings or behavior as needed for user login


class SellerLoginView(LoginView):
    template_name = "registration/seller_login .html"

    def get_success_url(self):
        return reverse("seller:item-list")


class Contact(TemplateView):
    template_name = "eshop/contact.html"


class About(TemplateView):
    template_name = "eshop/about.html"


from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from .models import Item
from cart.models import  Cart, CartItems

class ProductDetail(DetailView):
    template_name = "eshop/product_detail.html"
    model = Item
    context_object_name = "item"

    def get_queryset(self):
        queryset = Item.objects.filter(pk=self.kwargs["pk"], listed_at__isnull=False)
        return queryset

    def post(self, request, *args, **kwargs):
        item = self.get_object()
        quantity = int(request.POST.get('quantity', 1))

        # Get or create the user's cart
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Create a new cart item
        cart_item = CartItems.objects.create(
            cart=cart,
            user=request.user,
            item=item,
            price=item.price,
            quantity=quantity
        )

        # Optionally, you can perform additional logic or redirect to the cart page
        return redirect('cart')  # Replace 'cart' with the URL name of your cart page



class ShopGrid(ListView):
    template_name = "eshop/shop_grid.html"
    model = Item
    context_object_name = "items"
    queryset = Item.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

 
        context["brands"] = Brand.objects.all()[:6]
        context["categories"] = Category.objects.all()

        return context


# class Cart(TemplateView):
#     template_name = "eshop/cart.html"

class CartListView(ListView):
    model = CartItems
    template_name = "eshop/cart.html"
    queryset = CartItems.objects.all()
    context_object_name = "cart_items"

class CartItemUpdateView(View):
    def post(self, request, pk):
        item = get_object_or_404(CartItems, pk=pk)
        quantity = int(request.POST.get(f'quantity{pk}', 1))

        # Update the quantity of the cart item
        item.quantity = quantity
        item.save()

        return redirect('cart')
    
class CartItemDeleteView(View):
    def get(self, request, pk):
        item = get_object_or_404(CartItems, pk=pk)
        item.delete()
        return redirect('cart')


class Checkout(TemplateView):
    template_name = "eshop/checkout.html"


class UserRegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registration/register.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(
                "home"
            )  # Replace 'home' with the URL name of your home page
        return render(request, "registration/register.html", {"form": form})


###########################################


class NewsletterView(View):
    def post(self, request, *args, **kwargs):
        is_ajax = request.headers.get("x-requested-with")
        if is_ajax == "XMLHttpRequest":
            form = NewsletterForm(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse(
                    {
                        "success": True,
                        "message": "Successfully subscribed to our newsletter.",
                    },
                    status=201,
                )
            else:
                return JsonResponse(
                    {
                        "success": False,
                        "message": "Form is not valid. Must be an AJAX XMLHttpRequest",
                    },
                    status=400,
                )
        else:
            return JsonResponse(
                {
                    "success": False,
                    "message": "Cannot process request. Must be an AJAX XMLHttpRequest",
                },
                status=400,
            )


from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger


class SearchItemView(View):
    template_name = "eshop/search_item.html"


    def get(self, request, *args, **kwargs):
        query = request.GET["query"]
        item_list = Item.objects.filter(
            (Q(name__icontains=query) | Q(detail__icontains=query))
            & (
                Q(
                    listed_at__isnull=False,
                )
            )
        ).order_by("-listed_at")

        # pagination start
        page = request.GET.get("page", 1)
        paginate_by = 2
        paginator = Paginator(item_list, paginate_by)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        # pagination end

        return render(
            request,
            self.template_name,
            {"page_obj": items, "query": query},
        )
