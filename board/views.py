from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from board.models import Article, Comment
from .form import ArticleForm, CommentForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# 학과 게시판
# C - 학과사람
# R - 누구나
# U - 학과사람
# D - 본인 or 학생회장

# 04. 구현하면서 생각한 내용들.md 파일에 기록한 것들을 적용하면서 진행


def index(request):
    # 게시물 불러와서 댓글수 카운트
    articles = Article.objects.all()

    # 쿼리 호출 됨
    for i in range(len(articles)):
        articles[i].comment_count = len(Comment.objects.filter(article=articles[i]))
    
    # 페이징처리
    articles = Paginator(articles, 20)
    page = request.GET.get('page')
    try:
        articles = articles.page(page)
    except PageNotAnInteger:
        articles = articles.page(1)
    except EmptyPage:
        articles = articles.page(articles.num_pages)

    context = {
        'articles': articles,
    }
    return render(request, 'board/index.html', context)


@login_required
def new(request):
    return render(request, 'board/new.html')


@login_required
def create(request):
    form = ArticleForm(request.POST, request.FILES)
    if form.is_valid():
        article = form.save(commit=False)
        article.user = request.user
        article.save()
    return redirect('board:index')


@login_required
def detail(request, no):
    article = Article.objects.get(id=no)
    comments = article.comment_set.all()
    print(article.image)
    article.comment_count = len(Comment.objects.filter(article=article))
    commentform = CommentForm()
    context = {
        'article': article,
        'commentform': commentform,
        'comments': comments,
    }
    return render(request, 'board/detail.html', context)


@login_required
@require_POST
def delete(request, no):
    Article.objects.get(id=no).delete()
    return redirect('board:index')


@login_required
def update(request, no):
    context = {
        'no': no,
        'title': Article.objects.get(id=no).title,
        'content': Article.objects.get(id=no).content,
    }
    return render(request, 'board/update.html', context)


@login_required
@require_POST
def updated(request):
    no = int(request.POST.get('no'))
    article = Article.objects.get(id=no)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('board:detail', no)


@login_required
@require_POST
def newComment(request, no):
    article = Article.objects.get(id=no)
    Comment.objects.create(
        article=article, content=request.POST.get('content'), user=request.user)
    return redirect('board:detail', no)


@login_required
@require_POST
def deleteComment(request, no):
    comment = Comment.objects.get(id=request.POST.get('commentId'))
    comment.delete()
    return redirect('board:detail', no)


@login_required
@require_POST
def updateComment(request, no):
    comment = Comment.objects.get(id=request.POST.get('commentId'))
    form = CommentForm(request.POST, instance=comment)
    if form.is_valid():
        comment = form.save()
    return redirect('board:detail', no)


@login_required
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    if user in article.like_users.all():
        article.like_users.remove(user)
    else:
        article.like_users.add(user)

    return redirect('board:index')