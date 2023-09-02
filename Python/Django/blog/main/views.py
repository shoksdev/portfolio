from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Article, ArticleLike, CommentLike
from .form import CommentForm, RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView

class ArticleView(View): #Вывод статей
    def get(self, request):
        articles = Article.objects.all()
        context = {'articles': articles}
        return render(request, 'main/main.html', context)

class ArticleDetail(View): #Страница статьи
    def get(self, request, pk):
        article = Article.objects.get(id=pk)
        context = {'article': article}
        return render(request, 'main/main_detail.html', context)

class AddComment(View): #Добавление комментария
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.article_id = pk
            form.save()
        return redirect(f'/{pk}')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AddArticleLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            ArticleLike.objects.get(ip=ip_client, art_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = ArticleLike()
            new_like.ip = ip_client
            new_like.art_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')

class DelArticleLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            like = ArticleLike.objects.get(ip=ip_client, art_id=pk)
            like.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')

class AddCommentLike(View):
    def get(self, request, pk, comment_pk):
        ip_client = get_client_ip(request)
        try:
            CommentLike.objects.get(ip=ip_client, com_id=comment_pk)
            print(CommentLike.com_id)
            return redirect(f'/{pk}')
        except:
            new_like = CommentLike()
            new_like.ip = ip_client
            new_like.com_id = int(comment_pk)
            new_like.save()
            return redirect(f'/{pk}')

class DelCommentLike(View):
    def get(self, request, pk, comment_pk):
        ip_client = get_client_ip(request)
        try:
            like = CommentLike.objects.get(ip=ip_client, com_id=comment_pk)
            like.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')

@login_required
def profile_view(request):
    return render(request, 'main/profile.html')

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('main:profile')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)