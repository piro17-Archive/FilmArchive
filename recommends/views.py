from django.shortcuts import render, redirect
from .models import Recommend

def recommends(request):
    query = request.GET.get('title', None)
    if query:
        recommends = Recommend.objects.filter(title__contains=query)
    else:
        recommends = Recommend.objects.all()

    context = {
        "recommends":recommends
    }
    return render(request, template_name="recommends/rec_main.html", context=context)


def rec_create(request):
    if request.method == "POST":
        print(request.POST)
        title = request.POST["title"]
        content = request.POST["content"]
        keyword = request.POST["keyword"]
        
        Recommend.objects.create(title= title, content=content, keyword=keyword)
        
        #TODO: redirect url is wrong i think because page not found error occurs
        return redirect(f"recommends/")

    context = {}

    return render(request, template_name="recommends/rec_create.html", context=context)

def rec_detail(request, id):
    recommend = Recommend.objects.get(id=id)
    context = {
        "recommend": recommend
    }
    return render(request, template_name="recommends/rec_detail.html", context=context)

def rec_update(request, id):
        if request.method == "POST":
            title = request.POST["title"]
            content = request.POST["content"]
            keyword = request.POST["keyword"]
            Recommend.objects.filter(id=id).update(title= title, content=content, keyword=keyword)
            return redirect(f"/recommends/{id}")
            
    
        elif request.method == "GET":
            recommend = Recommend.objects.get(id=id)
            context = {
                "recommend":recommend
            }
            return render(request, template_name="recommends/rec_update.html", context=context)

def rec_delete(request, id):
    if request.method == "POST":
        Recommend.objects.filter(id=id).delete()
        return redirect(f"/recommends/")