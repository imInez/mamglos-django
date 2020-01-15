from django.shortcuts import render
from .models import Dog, Employee, Article, Partner, Document
from django.views.generic.list import ListView
# from random import sample, shuffle

def home(request):
    context = {
        'articles_main':Article.objects.filter(is_main_article = True),
        'partners': Partner.objects.all(),
        'dog_count': len(Dog.objects.all()),
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'employees': Employee.objects.all(),
        'documents': Document.objects.all()
    }
    return render(request, 'main/about.html', context)

class AdoptedList(ListView):
    model = Dog
    template_name = 'main/adopted.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(was_adopted=True).order_by('-adoption_date')

def contact(request):
    return render(request,'main/contact.html')

class ForAdoptionList(ListView):
    model = Dog
    template_name='main/forAdoption.html'

    def get_queryset(self):
        qs = super().get_queryset()
        # last_id = qs.objects.all[-1]
        # # random_qs = sample(qs, len(qs))
        # # return random_qs.filter(was_adopted=False)
        return qs.filter(was_adopted=False)

    def get_contex_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class NewsList(ListView):
    model = Article
    template_name = 'main/news.html'
    paginate_by = 4

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def partner(request):
    context = {
        'partners': Partner.objects.all(),
        'articles_support': Article.objects.filter(is_support = True)
    }
    return render(request,'main/partner.html', context)

def support(request):
    return render(request,'main/support.html')

def volo(request):
    return render(request,'main/volo.html')

class FoundLostList(ListView):
    model = Article
    template_name = 'main/foundlost.html'
    paginate_by = 4

    def get_queryset(self):
        qs = super().get_queryset()
        qs = (qs.filter(is_found=True)) | (qs.filter(is_lost=True))
        return qs.order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context





