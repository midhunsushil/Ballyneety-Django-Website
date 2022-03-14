from django.shortcuts import render
from manage_content.models import Post, Page
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

# Create your views here.

def index(request):

    return render(request, "index.html")

def about_us(request):

    error = ""
    try:
        post = Post.objects.get(page=Page.objects.get(title="About"))
    except MultipleObjectsReturned :
        error = "More than one Post for 'About' page found. Keep only one !"
        print("More than one Post for 'About' page found. Keep only one !")
    except ObjectDoesNotExist:
        error = "'About' Post not defined!"
        print("'About' Post not defined!")

    if error:
        data = {
                'error': error
        }
    else:
        data = {
                'post': post,
                'error': error,
        }
    return render(request, "about_us.html", context=data)

def mares(request):

    error = ""

    try:
        post = Post.objects.get(page=Page.objects.get(title="Our Mares"))
    except MultipleObjectsReturned :
        error = "More than one Post for 'OUR MARES' page found. Keep only one !"
        print("More than one Post for 'OUR MARES' page found. Keep only one !")
    except ObjectDoesNotExist:
        error = "'OUR MARES' Post not defined!"
        print("'OUR MARES' Post not defined!")

    if error:
        data = {
                'error': error
        }
    else:
        data = {
                'post': post,
                'error': error,
        }
    return render(request, "mares.html", context=data)

def stallions(request):

    posts = Post.objects.filter(page=Page.objects.get(title="Stallions"))
    data = {
            'posts' : posts,
    }
    return render(request, 'stallions.html', context=data)

def progeny(request):

    error = ""

    try:
        post = Post.objects.get(page=Page.objects.get(title="Our Mares"))
    except MultipleObjectsReturned :
        error = "More than one Post for 'FOR SALE' page found. Keep only one !"
        print("More than one Post for 'FOR SALE' page found. Keep only one !")
    except ObjectDoesNotExist:
        error = "'FOR SALE' Post not defined!"
        print("'FOR SALE' Post not defined!")

    if error:
        data = {
                'error': error
        }
    else:
        data = {
                'post': post,
                'error': error,
        }
    return render(request, 'progeny.html', context=data)

def for_sale(request):

    error = ""

    try:
        post = Post.objects.get(page=Page.objects.get(title="For Sale"))
    except MultipleObjectsReturned :
        error = "More than one Post for 'FOR SALE' page found. Keep only one !"
        print("More than one Post for 'FOR SALE' page found. Keep only one !")
    except ObjectDoesNotExist:
        error = "'FOR SALE' Post not defined!"
        print("'FOR SALE' Post not defined!")

    if error:
        data = {
                'error': error
        }
    else:
        data = {
                'post': post,
                'error': error,
        }
    return render(request, 'for_sale.html', context=data)

def contact_us(request):

    return render(request, 'contact_us.html')
