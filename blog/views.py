from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Companies, Post, Comments
from .forms import CompaniesForm
from .forms import PostForm
from .forms import CommentsForm
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth.models import User

# from django views generic import ListViews, DetailView
 



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('companies_list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def companies_list(request):
    companies=Companies.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/companies_list.html', {'companies': companies}) #key:value (предыдущая переменная companies)

def company_detail(request, pk):
    company = get_object_or_404(Companies, pk=pk)
    posts=Post.objects.filter(company=company)
    return render(request, 'blog/company_detail.html', {'company': company, 'posts':posts})

def company_new(request):
    if request.method == "POST":
        form = CompaniesForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            # company.author = request.user
            
            company_owner=request.user
            company.save()

            return redirect('company_detail', pk=company.pk)
    else:
        form = CompaniesForm()
    return render(request, 'blog/company_edit.html', {'form': form})

def company_edit(request, pk):
    company = get_object_or_404(Companies, pk=pk)
    if request.method == "POST":
        form = CompaniesForm(request.POST, request.FILES,  instance=company)
        if form.is_valid():
            company.save()
            return redirect('company_detail', pk=company.pk)
    else:
        form = CompaniesForm(instance=company)
    return render(request, 'blog/company_edit.html', {'form': form})


def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments=Comments.objects.filter(post=post)
    if request.method == "POST":
        form=CommentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentsForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments':comments, 'form':form})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=form.instance.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def comments_list(request):
    comments = Comments.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/comments_list.html', {'comments': comments})

def comments_detail(request, pk):
    comments = get_object_or_404(Comments, pk=pk)
    return render(request, 'blog/comments_detail.html', {'comments': comments})
def comments_new(request):
    if request.method == "POST":
        form = CommentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('comments_detail', pk=form.instance.pk)
    else:
        form = CommentsForm()
    return render(request, 'blog/comments_edit.html', {'form': form})

def comments_edit(request, pk):
    comments = get_object_or_404(Comments, pk=pk)
    if request.method == "POST":
        form = CommentsForm(request.POST, request.FILES, instance=comments)
        if form.is_valid():
            form.save()
            return redirect('comments_detail', pk=form.instance.pk)
    else:
        form = CommentsForm(instance=comments)
    return render(request, 'blog/comments_edit.html', {'form': form})