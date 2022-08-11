from django.shortcuts import render, redirect
from .models import Recommend, Keyword, User

def recommends(request):
    keywordinfo = Keyword.objects.all()
    query = request.GET.get('title', None)
    if query:
        recommends = Recommend.objects.filter(title__contains=query)
    else:
        recommends = Recommend.objects.all()

    # recommends 정의가 비효율적입니다.
    # 위에서 recommend가 정의되는데, 아래 코드에서 다시 DB 호출해서 recommend를 수정합니다.
    # 수정이 필요해보입니다.
    querykeyword = request.GET.get('sortkeyword',"None")
    if querykeyword != "None":
        recommends = Recommend.objects.filter(recKeyword__id__contains=querykeyword)
        querykeyword = int(querykeyword)
    else:
        recommends = Recommend.objects.all()

    context = {
        "recommends":recommends,
        "keywordinfo": keywordinfo,
        "querykeyword": querykeyword,
    }
    return render(request, template_name="recommends/rec_main.html", context=context)


def rec_create(request):
    keywordinfo = Keyword.objects.all()

    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        recImage = request.FILES["recImage"]
        postUser = User.objects.get(id=request.user.id)
        Recommend.objects.create(title= title, content=content, recImage=recImage, postUser=postUser)

        # now get keywords

        a = Recommend.objects.all()
        # 마지막 포스트(현재)를 가져오는거...i think?
        keywordoj = a.last()
        for i in range(1, len(keywordinfo)+1):
            # 키워드 하나하나
            keywordap = request.POST.get(str(i))
            if keywordap:
                keywordoj.recKeyword.add(Keyword.objects.filter(id = i)[0])
        keywordoj.save()
        return redirect(f"recommends/{a.last().id}") #recommends/{a.last().id}

    context = {
        "keywordinfo" : keywordinfo
    }

    return render(request, template_name="recommends/rec_create.html", context=context)


def rec_detail(request, id):
    recommend = Recommend.objects.get(id=id)
    keywordinfo = Keyword.objects.all()
    context = {
        "recommend": recommend,
        "keywordinfo": keywordinfo,
    }
    return render(request, template_name="recommends/rec_detail.html", context=context)


def rec_update(request, id):
    keywordinfo = Keyword.objects.all()
    if request.method == "POST":
        # title, content가 null인 경우 업데이트 문제 발생
        # form으로 validation 필요해보임
        title = request.POST["title"]
        content = request.POST["content"]
        Recommend.objects.filter(id=id).update(title=title, content=content)

        keywordoj = Recommend.objects.filter(id=id)[0]
        for i in range(1,len(keywordinfo)+1):
            keywordap = request.POST.get(str(i))
            if keywordap:
                keywordoj.recKeyword.add(Keyword.objects.filter(id = i)[0])
        keywordoj.save()

        return redirect(f"/recommends/{id}")


    elif request.method == "GET":
            recommend = Recommend.objects.get(id=id)
            context = {
                "recommend":recommend,
                "keywordinfo":keywordinfo,
            }
            return render(request, template_name="recommends/rec_update.html", context=context)

def rec_delete(request, id):
    if request.method == "POST":
        Recommend.objects.filter(id=id).delete()
        return redirect(f"/recommends/")
