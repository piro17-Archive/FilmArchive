from itertools import count
from django.shortcuts import render, redirect
from requests import delete
from .models import User, Keyword, Frame
from .froms import PostFrame
from django.contrib import messages
from django.db.models import Count, When,Case
from datetime import date,timedelta
from datetime import datetime
import _strptime 
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
 
# Create your views here.
def date_range(start, end):
    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")
    dates = [(start + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
    return dates

def frame(request):
    today = date.today()
    dates = date_range(str(today-timedelta(weeks=1)+ timedelta(days=1)), str(today))
    frameinfo = Frame.objects.all()
    for weeklikecount in frameinfo:
        count = 0
        if weeklikecount.framelikedate != None:
            datesplit = weeklikecount.framelikedate.split('/')
        else:
            continue
        for day in dates:
            for pic in datesplit:
                if day in pic:
                    count += 1
        weeklikecount.frameweeklike = count
        weeklikecount.save()
    frameweekinfo = frameinfo.order_by('?').order_by('-frameweeklike','?')[:4]
    print(frameweekinfo)
    
    sort = request.GET.get('sort',None)
    if sort == '1':
        frameinfo = frameinfo.annotate(like_count= Count('framelikeuser')).order_by('-like_count')
        print(frameinfo)
    elif sort == '2':
        frameinfo = Frame.objects.all().order_by('-id')
        
    if request.user.is_authenticated:
        like = request.user.likeMany.all()
        save = request.user.saveMany.all()
    else:
        like = None
        save = None
    keywordinfo = Keyword.objects.all()

    query = request.GET.get('title', None)
    if query:
        frameinfo = Frame.objects.filter(frametitle__contains=query)
        
    likereq = request.GET.get('like',None)
    savereq = request.GET.get('save',None)
    querykeyword = request.GET.get('sortkeyword',"None")
    if querykeyword != "None":
        frameinfo = Frame.objects.filter(framekeyword__id__contains=querykeyword)
        querykeyword = int(querykeyword)
    if likereq != None:
        sltframe = Frame.objects.get(id = likereq)
        if request.user in sltframe.framelikeuser.all():
            sltframe.framelikeuser.remove(request.user)
            likedates = sltframe.framelikedate.split('/')

            for likedate in likedates:
                if str(request.user) in likedate:
                    likedates.remove(likedate)
                    break
            sltframe.framelikedate = '/'.join(likedates)

        else:
            sltframe.framelikeuser.add(request.user)
            sltframe.framelikedate = sltframe.framelikedate+str(request.user)+str(today)+'/'
            sltframe.save()
        sltframe.save()

    if savereq != None:
        sltframe = Frame.objects.get(id = savereq)
        if request.user in sltframe.framesaveuser.all():
            sltframe.framesaveuser.remove(request.user)
        else:
            sltframe.framesaveuser.add(request.user)
        sltframe.save()
    context = {
        "frameinfo": frameinfo,
        "like": like,
        "save": save,
        "keywordinfo": keywordinfo,
        "querykeyword": querykeyword,
        "frameweekinfo": frameweekinfo,
    }

    return render(request, template_name='framesharings/frame.html',context=context)


def framedetail(request,id):
    today = date.today()
    dates = date_range(str(today-timedelta(weeks=1)+ timedelta(days=1)), str(today))
    frameinfo = Frame.objects.get(id =id)
    keywordinfo = Keyword.objects.all()
    like = request.user.likeMany.all()
    save = request.user.saveMany.all()
    likereq = request.GET.get('like',None)
    savereq = request.GET.get('save',None)
    if likereq != None:
        sltframe = Frame.objects.get(id = likereq)
        if request.user in sltframe.framelikeuser.all():
            sltframe.framelikeuser.remove(request.user)
            likedates = sltframe.framelikedate.split('/')

            for likedate in likedates:
                if str(request.user) in likedate:
                    likedates.remove(likedate)
                    break
            sltframe.framelikedate = '/'.join(likedates)

        else:
            sltframe.framelikeuser.add(request.user)
            sltframe.framelikedate = sltframe.framelikedate+str(request.user)+str(today)+'/'
            sltframe.save()
        sltframe.save()

    if savereq != None:
        sltframe = Frame.objects.filter(id = savereq)
        if request.user in sltframe[0].framesaveuser.all():
            sltframe[0].framesaveuser.remove(request.user)
        else:
            sltframe[0].framesaveuser.add(request.user)
        sltframe[0].save()

    context = {
        "frameinfo": frameinfo,
        "keywordinfo": keywordinfo,
        "like": like,
        "save": save,
    }
    return render(request, template_name="framesharings/framedetail.html", context=context)

def framecreate(request):
    keywordinfo = Keyword.objects.all()
    # form = PostFrame()

    if request.method == "POST":
        
        framephoto = request.FILES.get("framephoto")
        if framephoto == None:
            messages.warning(request, '사진은 필수입니다.')
            return redirect("framesharings:framecreate")
        
        frametitle = request.POST["frametitle"]
        frameexample = request.FILES.get("frameexamle")
        framememo = request.POST["framememo"]
        framepublic = request.POST.get("framepublic")
        userid = User.objects.get(id = request.user.id)
        if framepublic == "False":
            Frame.objects.create(framememo=framememo,framephoto=framephoto, frametitle=frametitle,frameexample=frameexample,userid=userid,framepublic=False)
        else:
            Frame.objects.create(framememo=framememo,framephoto=framephoto, frametitle=frametitle,frameexample=frameexample,userid=userid,framepublic=True)
        a = Frame.objects.all()
        keywordoj = a.last()
        for i in range(1,len(keywordinfo)+1):
            keywordap = request.POST.get(str(i))
            if keywordap:
                keywordoj.framekeyword.add(Keyword.objects.filter(id = i)[0])
        keywordoj.save()
            
        
        return redirect(f"/framedetail/{a.last().id}")
        
    context = {
        "keywordinfo": keywordinfo,
        # "form": form
    }
    return render(request, template_name="framesharings/framecreate.html",context=context)

def frameupdate(request,id):
    keywordinfo = Keyword.objects.all()
    if request.method == "POST":
        framephoto = request.FILES.get("framephoto")
        frametitle = request.POST["frametitle"]
        frameexample = request.FILES.get("frameexamle")
        framememo = request.POST["framememo"]
        framepublic = request.POST.get("framepublic")
        if framepublic == "False":
            decision = False
        else:
            decision = True
        userid = User.objects.get(id = request.user.id)
        clearphoto = request.POST.get("clearphoto")
        clearexample = request.POST.get("clearexample")

        if framephoto == None and frameexample == None:
            if clearphoto == 'clearphoto' and clearexample == 'clearexample':
                Frame.objects.create(userid = userid, framephoto = None,frametitle=frametitle,frameexample=None,framememo=framememo,framepublic=decision,)

            elif clearphoto != 'clearphoto' and clearexample == 'clearexample':
                Frame.objects.create(userid = userid, framephoto = Frame.objects.filter(id = id)[0].framephoto,frametitle=frametitle,frameexample=None,framememo=framememo,framepublic=decision,)

            elif clearphoto == 'clearphoto' and clearexample != 'clearexample':
                Frame.objects.create(userid = userid, framephoto = None,frametitle=frametitle,frameexample=Frame.objects.filter(id = id)[0].frameexample,framememo=framememo,framepublic=decision,)

            else :
                Frame.objects.create(userid = userid, framephoto = Frame.objects.filter(id = id)[0].framephoto,frametitle=frametitle,frameexample=Frame.objects.filter(id = id)[0].frameexample,framememo=framememo,framepublic=decision,)


        elif framephoto and frameexample == None:
            if clearphoto == 'clearphoto' and clearexample == 'clearexample':
                Frame.objects.create(userid = userid, framephoto = framephoto,frametitle=frametitle,frameexample=None,framememo=framememo,framepublic=decision,)

            elif clearphoto != 'clearphoto' and clearexample == 'clearexample':
                Frame.objects.create(userid = userid, framephoto = framephoto,frametitle=frametitle,frameexample=None,framememo=framememo,framepublic=decision,)

            elif clearphoto == 'clearphoto' and clearexample != 'clearexample':
                Frame.objects.create(userid = userid, framephoto = framephoto,frametitle=frametitle,frameexample=Frame.objects.filter(id = id)[0].frameexample,framememo=framememo,framepublic=decision,)

            else :
                Frame.objects.create(userid = userid, framephoto = framephoto,frametitle=frametitle,frameexample=Frame.objects.filter(id = id)[0].frameexample,framememo=framememo,framepublic=decision,)


        elif framephoto == None and frameexample:
            if clearphoto == 'clearphoto' and clearexample == 'clearexample':
                Frame.objects.create(userid = userid, framephoto = None,frametitle=frametitle,frameexample=frameexample,framememo=framememo,framepublic=decision,)

            elif clearphoto != 'clearphoto' and clearexample == 'clearexample':
                Frame.objects.create(userid = userid, framephoto = Frame.objects.filter(id = id)[0].framephoto,frametitle=frametitle,frameexample=frameexample,framememo=framememo,framepublic=decision,)

            elif clearphoto == 'clearphoto' and clearexample != 'clearexample':
                Frame.objects.create(userid = userid, framephoto = None,frametitle=frametitle,frameexample=frameexample,framememo=framememo,framepublic=decision,)
            else :
                Frame.objects.create(userid = userid, framephoto = Frame.objects.filter(id = id)[0].framephoto,frametitle=frametitle,frameexample=frameexample,framememo=framememo,framepublic=decision,)
        else:
            Frame.objects.create(userid = userid, framephoto = framephoto,frametitle=frametitle,frameexample=frameexample,framememo=framememo,framepublic=decision,)


        




        Frame.objects.filter(id=id).delete()
        a = Frame.objects.all()
        keywordoj = a.last()
        for i in range(1,len(keywordinfo)+1):
            keywordap = request.POST.get(str(i))
            if keywordap:
                keywordoj.framekeyword.add(Keyword.objects.filter(id = i)[0])
        keywordoj.save()
            
        
        return redirect(f"/framedetail/{a.last().id}")

    frameinfo = Frame.objects.get(id = id)
    context = {
        "frameinfo": frameinfo,
        "keywordinfo": keywordinfo,
    }
    return render(request, template_name="framesharings/frameupdate.html", context=context)

def framedelete(request,id):
    if request.method == "POST":
        Frame.objects.filter(id=id).delete()
        return redirect("/frame")

@csrf_exempt
def like_ajax(request):
    print(1)
    today = date.today()
    req = json.loads(request.body)
    comment_id = req['id']
    button_type = req['type']

    sltframe = Frame.objects.get(id = comment_id)
    if button_type == 'like':
        button_type = 'dislike'
        sltframe.framelikeuser.remove(request.user)
        likedates = sltframe.framelikedate.split('/')

        for likedate in likedates:
            if str(request.user) in likedate:
                likedates.remove(likedate)
                break
        sltframe.framelikedate = '/'.join(likedates)

    else:
        button_type = 'like'
        sltframe.framelikeuser.add(request.user)
        sltframe.framelikedate = sltframe.framelikedate+str(request.user)+str(today)+'/'
        sltframe.save()
    sltframe.save()

    return JsonResponse({'id': comment_id, 'type': button_type})


@csrf_exempt
def save_ajax(request):
    req = json.loads(request.body)
    comment_id = req['id']
    button_type = req['type']

    sltframe = Frame.objects.get(id = comment_id)
    if button_type == 'save':
        button_type = 'notsave'
        sltframe.framesaveuser.remove(request.user)

    else:
        button_type = 'save'
        sltframe.framesaveuser.add(request.user)
    sltframe.save()
    return JsonResponse({'id': comment_id, 'type': button_type})