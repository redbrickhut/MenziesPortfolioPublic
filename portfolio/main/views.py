from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .text import *
from .images import *

# Create your views here.
base_context = {
    "menu_icon": "menu.png",
    "int_links": [
        InternalLink("Home", "index"),
        InternalLink("About Me", "about"),
        InternalLink("My Projects", "projects"),
        InternalLink("Media", "media"),
        InternalLink("Blog", "blog")

    ],
    "ext_links": [
        ExternalLink('github.png', 'https://github.com/redbrickhut'),
        ExternalLink('instagram.png', 'https://www.instagram.com/redbrickhut/'),
        ExternalLink('linkedin.png', 'https://www.linkedin.com/in/james-menzies-24ab3a184/'),
        ExternalLink('mail.png', 'mailto:james.r.menzies@gmail.com'),
    ]
}


def index(request):
    context = base_context
    context['title'] = "Home"
    context['page_wrapper'] = True
    context['welcome_message'] = welcome_message
    context['directories'] = [
        Directory("The Person", tso_headshot, 'about', person_directory_prompt),
        Directory("The Coder", computer_shot, 'projects', coder_directory_prompt),
        Directory("The Musician", musician_shot, 'media', musician_directory_prompt),
    ]

    return render(request, 'main/index.html', context)


def about(request):
    context = base_context
    context['title'] = "About"
    context['details'] = {
        "Name": "James Menzies",
        "Phone": "0432 801 574",
        "Email": "james.r.menzies@gmail.com",
        "Location": "Hobart, Tasmania, Australia",
    }
    context["skills"] = [
        "Python",
        "Java",
        "JavaFX",
        "Hibernate",
        "Git",
        "Github",
        "HTML",
        "CSS",
    ]
    context["sales_pitch"] = sales_pitch
    context["biography"] = biography

    return render(request, 'main/about.html', context)

def projects(request):
    return HttpResponse("My Projects")


def media(request):
    return HttpResponse("Media")


def blog(request):

    context = base_context
    context['title'] = "Blogs"
    context['blog_intro'] = blog_intro
    context["posts"] = BlogPost.objects.all()
    return render(request, 'main/blog.html', context)


def blogposts(request, post_id):

    post = BlogPost.objects.get(pk=post_id)
    context = base_context
    context['title'] = post.title
    context['post'] = post
    return render(request, 'main/blogpost.html', context)
