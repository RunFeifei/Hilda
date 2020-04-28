# Create your views here.
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from blog.models import Post
from comments.forms import CommentForm


@require_POST
def comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
        # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
        commentt = form.save(commit=False)
        commentt.post = post
        commentt.save()
        return redirect(post)
    context = {
        'post': post,
        'form': form
    }
