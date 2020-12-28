from django.shortcuts import render, get_object_or_404
from .models import Grade2blogpost
from .models import Grade3blogpost
from .models import Grade4blogpost


def all_posts(request):
    grade2blogposts = Grade2blogpost.objects.order_by('-date')[:3]
    grade3blogposts = Grade3blogpost.objects.order_by('-date')[:3]
    grade4blogposts = Grade4blogpost.objects.order_by('-date')[:3]

    # This line of code grabs everything out of the database, turns them into Python objects
    # and then puts them inside of a list.
    return render(request, 'blog/all_posts.html', {'grade2blogposts': grade2blogposts,
                                                   'grade3blogposts': grade3blogposts,
                                                   'grade4blogposts': grade4blogposts})


# one grade views
def view_all_grade2(request):
    blogposts = Grade2blogpost.objects.order_by('-date')
    return render(request, 'blog/onegrade_2.html', {'blogposts': blogposts})


def view_all_grade3(request):
    blogposts = Grade3blogpost.objects.order_by('-date')
    return render(request, 'blog/onegrade_3.html', {'blogposts': blogposts})


def view_all_grade4(request):
    blogposts = Grade4blogpost.objects.order_by('-date')
    return render(request, 'blog/onegrade_4.html', {'blogposts': blogposts})


# one blogpost views
def view_one_grade2(request, post_id):
    blogpost = get_object_or_404(Grade2blogpost, pk=post_id)
    return render(request, 'blog/one_post.html', {'blogpost': blogpost})


def view_one_grade3(request, post_id):
    blogpost = get_object_or_404(Grade3blogpost, pk=post_id)
    return render(request, 'blog/one_post.html', {'blogpost': blogpost})


def view_one_grade4(request, post_id):
    blogpost = get_object_or_404(Grade4blogpost, pk=post_id)
    return render(request, 'blog/one_post.html', {'blogpost': blogpost})
