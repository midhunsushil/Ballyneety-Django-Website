from django.shortcuts import render

# Create your views here.

def manage_content(request):

    return render(request, 'manage_content/manage_content_index.html')

def edit_post(request):

    return render(request, 'manage_content/edit_post.html')
