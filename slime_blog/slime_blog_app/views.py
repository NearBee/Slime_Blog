from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import PostForm

# Create your views here.


def homepage_view(request):
    posts = Post.objects.all()
    return render(request, "homepage.html", {"posts": posts})


def post_details_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    return render(request, "post_details.html", {"post": post, "comments": comments})


# @login_required
def create_post(request):
    if request.method == "POST":
        # Handle form submission here
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")

        else:
            # TODO: Expand on form errors here
            return render(request, "blog/create_post.html", {"form": form})
    else:
        form = PostForm()
        return render(request, "create_post.html", {"form": form})
