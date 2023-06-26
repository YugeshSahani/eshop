from shop_app.models import Item, Category, Brand


def navigation(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    # recent_items = Item.objects.all()
    # tags = Tag.objects.all()[:10]

    return {
        # "recent_items": recent_items,
        "categories": categories,
        "brands": brands,
    }
