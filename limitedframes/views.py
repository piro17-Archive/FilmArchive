from pydoc import pager
from django.shortcuts import render

from limitedframes.models import Lifefourcut
from django.core.paginator import Paginator

# Create your views here.

def limited(request):
    lifeframeinfo = Lifefourcut.objects.all().order_by('-id')[:4]
    context = {
        "lifeframeinfo": lifeframeinfo,
    }
    return render(request, template_name='limitedframes/limited.html',context=context)

def limitedlife(request):
    lifeframeinfo = Lifefourcut.objects.all().order_by('-id')
    paginator = Paginator(lifeframeinfo, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    posts_cnt = lifeframeinfo.count()
    context = {
        "lifeframeinfo": lifeframeinfo,
        "posts": posts,
        "posts_cnt": posts_cnt,
    }
    return render(request, template_name='limitedframes/limitedlife.html',context=context)

def limitedlifedetail(request,id):
    lifeframeinfo = Lifefourcut.objects.get(id=id)
    context = {
        "lifeframeinfo": lifeframeinfo,
    }
    return render(request, template_name="limitedframes/limitedlifedetail.html",context=context)
