from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    object_article = Article.objects.all().order_by(ordering)
    context = {'object_list': object_article}
    return render(request, template, context)
