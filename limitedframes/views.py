from pydoc import pager
from django.shortcuts import render
import re
from limitedframes.models import Lifefourcut,Signature,Photoism
# Create your views here.
def limited(request):
    lifeframeinfo = Lifefourcut.objects.all().order_by('-id')[:4]
    signatureinfo = Signature.objects.all().order_by('-id')[:4]
    photoisminfo = Photoism.objects.all().order_by('-id')[:4]
    context = {
        "lifeframeinfo": lifeframeinfo,
        "signatureinfo": signatureinfo,
        "photoisminfo": photoisminfo,
    }
    return render(request, template_name='limitedframes/limited.html',context=context)

def limitedlife(request):
    # 한 번에 모든 걸 불러오면 효율적이지 않습니다.
    # Django Paginator 도입 권고드립니다.
    lifeframeinfo = Lifefourcut.objects.all().order_by('-id')
    context = {
        "lifeframeinfo": lifeframeinfo,
    }
    return render(request, template_name='limitedframes/limitedlife.html',context=context)

def limitedlifedetail(request,id):
    lifeframeinfo = Lifefourcut.objects.get(id=id)
    context = {
        "lifeframeinfo": lifeframeinfo,
    }
    return render(request, template_name="limitedframes/limitedlifedetail.html",context=context)

def limitedsignature(request):
    signatureinfo = Signature.objects.all().order_by('-id')
    context = {
        "signatureinfo": signatureinfo,
    }
    return render(request, template_name='limitedframes/limitedsignature.html',context=context)

def limitedphotoism(request):
    photoisminfo = Photoism.objects.all().order_by('-id')
    context = {
        "photoisminfo": photoisminfo,
    }
    return render(request, template_name='limitedframes/limitedphotoism.html',context=context)
