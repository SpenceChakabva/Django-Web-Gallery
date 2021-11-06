from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# Import PostForm from forms file
from .forms import PostForm
# Import Post model 
from .models import Post


# Create your views here. 
def home(request):
    # Get all posts from database
    posts = Post.objects.filter(active=True)
    # Get page Id
    page = request.GET.get('page')
    # Set the number of posts per page
    paginator = Paginator(posts, 6)
    # Track posts erros
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    # Send pagination data to the home template
    context = {'posts': posts}
    return render(request, 'base/index.html', context)


# View Function
def post(request, pk):
    # Filter posts using Id
    posts = Post.objects.get(id=pk)
    # Load post data to context
    context ={'post':posts}
    return render(request, 'base/post.html', context)

# Link to the about template
def about(request):
    return render(request, 'base/about.html')

# CRUD VIEWS
@login_required(login_url="home")
def createPost(request):
    form = PostForm()
    # Process request if post or get
    if request.method == 'POST':
        # Assign form to post data
        form = PostForm(request.POST, request.FILES)
        # Validate form data & save
        if form.is_valid():
            form.save()
        return redirect('home')
    # Assign post form context
    context = {'form': form}
    return render(request, 'base/post_form.html', context)

# Update post function 
@login_required(login_url="home")
def updatePost(request, pk):
    # Get post by Id
    post = Post.objects.get(id=pk)
    # Get form instance data
    form = PostForm(instance=post)
    # Check if request is post
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('home')
    # Set context variable to form instance
    context = {'form': form}
    return render(request, 'base/post_form.html', context)


# Delete post function with login required
@login_required(login_url="home")
def deletePost(request, pk):
    # Check if requested post ID is available
    post = Post.objects.get(id=pk)
    # Delete post & returin to home page
    if request.method == "POST":
        post.delete()
        return redirect('home')
    #  Set context variable to post data
    context = {'item': post}
    return render(request, 'base/delete.html', context)

# Email Sender
def sendEmail(request):
    email = EmailMessage(
        request.POST['subject'],
    )