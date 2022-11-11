from django.shortcuts import render

posts = [
    {
        'author': 'Candice',
        'title': 'Blog Post 1',
        'content': 'First Post!',
        'date_posted': 'November 10th, 2022'
    },
    {
        'author': 'The Dude',
        'title': 'The Dude Abides',
        'content': 'I\'m abiding!',
        'date_posted': 'November 10th, 2022'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})