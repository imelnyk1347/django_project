from django.shortcuts import render
from django.views.generic import View

from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin
from .forms import TagForm, PostForm


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})
