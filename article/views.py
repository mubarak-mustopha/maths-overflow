from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from activity.utils import create_action
from django.db.models import Q
from .models import Post, Comment
from .forms import PostForm, CommentForm


# utility functions
def _edit(request, record, model_form):
    """Utility function to edit a post or a comment"""
    form = model_form(request.POST, request.FILES, instance=record)
    if form.is_valid():
        edited_post = form.save(commit=False)
        # print(f"photo: {edited_post.photo}")
        # print(form.cleaned_data)
        edited_post.save()
        return edited_post


def _delete(request, pk, db_table):
    record = db_table.objects.get(id=pk)
    if request.method == "POST":
        record.delete()
        return redirect(record)
    return render(request, "article/delete.html", {"obj": record})


# Create your views here.
def post_list(request):
    q = request.GET.get("q") or ""
    print(q == "")
    posts = Post.objects.filter(
        Q(user__username__icontains=q) | Q(text__icontains=q),
    )
    return render(request, "article/posts.html", {"posts": posts, "q": q})


@login_required(login_url="login")
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            create_action(request.user, "made a new post", post)
            return redirect("posts")
        else:
            messages.error("Invalid form data.")
    form = PostForm()
    return render(
        request, "article/form.html", {"form": form, "title": "Create New Post"}
    )


@login_required(login_url="login")
def edit_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        edited_post = _edit(request, post, PostForm)
        create_action(request.user, "edited a post", post)
        return redirect(edited_post)

    # get request
    form = PostForm(instance=post)
    return render(
        request, "article/edit-form.html", {"form": form, "photo": post.photo}
    )


def delete_post(request, pk):
    return _delete(request, pk, Post)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, "article/single-post.html", {"post": post})


@login_required(login_url="login")
def create_comment(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            create_action(request.user, "made a comment", comment)
            return redirect("post-detail", pk)
    form = CommentForm()
    return render(request, "article/form.html", {"form": form, "title": "Add Comment"})


@login_required(login_url="login")
def edit_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.method == "POST":
        edited_comment = _edit(
            request,
            comment,
            CommentForm,
        )
        create_action(request.user, "edited a comment", edited_comment)
        return redirect(edited_comment)

    form = PostForm(instance=comment)
    return render(
        request, "article/edit-form.html", {"form": form, "photo": comment.photo}
    )


def delete_comment(request, pk):
    return _delete(request, pk, Comment)
