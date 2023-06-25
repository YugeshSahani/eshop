from shop_app.models import Item, Category, TrendingItemCategory, Brand


def navigation(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    # recent_items = Item.objects.all()
    # tags = Tag.objects.all()[:10]

    return {
        # "recent_items": recent_items,
        # "tags": tags,
        "categories": categories,
        "brands": brands,
        
        # "recently_lunched_items": recently_lunched_items,
    }
