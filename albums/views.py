from django.shortcuts import render, redirect
from requests import delete
from .models import User, Album,Type
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.contrib import messages

# Create your views here.


def album(request,id):
    userinfo = User.objects.get(id=id)
    allalbum = userinfo.userFor.all()
    sort = request.GET.get('sort',None)
    # 1, 2로 주고받는 게 의미 파악이 어렵습니다.
    # 따로 문자열이나, 변수를 정의해주는 게 좋습니다.
    # sort == 'albumdate'
    # or
    # SORT_ALBUMDATE = 1
    # sort == SORT
    if sort == '1':
        allalbum = userinfo.userFor.all().order_by('albumdate')
    elif sort == '2':
        allalbum = userinfo.userFor.all().order_by('-id')

    query = request.GET.get('title', None)
    if query:
        allalbum = userinfo.userFor.filter(albummemo__contains=query)

    context = {
        "allalbum": allalbum,
        "sort": sort,
    }
    return render(request, template_name='albums/album.html',context=context)

def albumcreate(request):
    typeinfo = Type.objects.all()
    today = DateFormat(datetime.now()).format('Y-m-d')

    if request.method == "POST":
        # useridname = request.POST["useridname"]
        # 인자가 비는 경우가 있어, 에러 발생 가능성이 있습니다.
        # form 활용을 권장드립니다.
        albumphoto = request.FILES.get("albumphoto")
        if albumphoto == None:
            messages.warning(request, '사진은 필수입니다.')
            return redirect("albums:albumcreate")
        albumvideo = request.FILES.get("albumvideo")
        albummemo = request.POST["albummemo"]
        albumtypename = request.POST["albumtypename"]
        albumlocation = request.POST["albumlocation"]
        albumdate = request.POST["albumdate"]
        albumtype = Type.objects.get(id = albumtypename)
        userid = User.objects.get(id = request.user.id)
        # 불규칙적인 띄어쓰기 불편하게 느껴집니다.
        Album.objects.create(userid = userid ,albumphoto =albumphoto, albumvideo=albumvideo,albummemo=albummemo,albumlocation=albumlocation,albumdate=albumdate,albumtype=albumtype)
        a = Album.objects.all()
        return redirect(f"albumdetail/{a.last().id}")
    context = {
        "typeinfo": typeinfo,
        'today': today,
        
    }
    return render(request, template_name="albums/albumcreate.html",context = context)

def albumdetail(request,id):
    albuminfo = Album.objects.get(id = id)
    context = {
        'albuminfo': albuminfo,

    }
    return render(request, template_name="albums/albumdetail.html",context =context)

def albumupdate(request,id):
    typeinfo = Type.objects.all()
    if request.method == "POST":
        albumphoto = request.FILES.get("albumphoto")
        print(albumphoto)
        albumvideo = request.FILES.get("albumvideo")
        albummemo = request.POST["albummemo"]
        albumtypename = request.POST["albumtypename"]
        albumlocation = request.POST["albumlocation"]
        albumdate = request.POST["albumdate"]
        albumtype = Type.objects.get(id = albumtypename)
        clearphoto = request.POST.get("clearphoto")
        clearvideo = request.POST.get("clearvideo")
        userid = User.objects.get(id = request.user.id)
        print("post")
        print(clearphoto,clearvideo)
        if albumphoto == None and albumvideo == None:

        #추가 경우의수 있을수있음
                if clearphoto == 'clearphoto' and clearvideo == 'clearvideo':
                    Album.objects.create(userid = userid, albumphoto=None,albumvideo=None,albummemo=albummemo,albumlocation=albumlocation,albumdate=albumdate,albumtype=albumtype)
                    Album.objects.filter(id=id).delete()
                    a = Album.objects.all()
                    return redirect(f"/albumdetail/{a.last().id}")
                elif clearphoto == 'clearphoto' and clearvideo != 'clearvideo':
                    Album.objects.create(userid = userid, albumphoto=None,albumvideo=Album.objects.filter(id=id)[0].albumvideo,albummemo=albummemo,albumlocation=albumlocation,albumdate=albumdate,albumtype=albumtype)
                    Album.objects.filter(id=id).delete()
                    a = Album.objects.all()
                    return redirect(f"/albumdetail/{a.last().id}")
                elif clearphoto != 'clearphoto' and clearvideo == 'clearvideo':
                    Album.objects.create(userid = userid, albumphoto=Album.objects.filter(id=id)[0].albumphoto,albumvideo=None,albummemo=albummemo,albumlocation=albumlocation,albumdate=albumdate,albumtype=albumtype)
                    Album.objects.filter(id=id).delete()
                    a = Album.objects.all()
                    return redirect(f"/albumdetail/{a.last().id}")
                else:
                    Album.objects.create(userid = userid, albumphoto=Album.objects.filter(id=id)[0].albumphoto,albumvideo=Album.objects.filter(id=id)[0].albumvideo,albummemo=albummemo,albumlocation=albumlocation,albumdate=albumdate,albumtype=albumtype)
                    Album.objects.filter(id=id).delete()
                    a = Album.objects.all()
                    return redirect(f"/albumdetail/{a.last().id}")


        elif albumphoto and albumvideo == None:

                if clearphoto == 'clearphoto' and clearvideo == 'clearvideo':
                    Album.objects.create(userid = userid, albumphoto=albumphoto,albumvideo=None,albummemo=albummemo,albumlocation=albumlocation,albumdate=albumdate,albumtype=albumtype)
                    Album.objects.filter(id=id).delete()
                    a = Album.objects.all()
                    return redirect(f"/albumdetail/{a.last().id}")
                elif clearphoto == 'clearphoto' and clearvideo != 'clearvideo':
                    Album.objects.create(userid = userid, albumphoto=albumphoto,albumvideo=Album.objects.filter(id=id)[0].albumvideo,albummemo=albummemo,albumlocation=albumlocation,albumdate=albumdate,albumtype=albumtype)
                    Album.objects.filter(id=id).delete()
                    a = Album.objects.all()
                    return redirect(f"/albumdetail/{a.last().id}")
                elif clearphoto != 'clearphoto' and clearvideo == 'clearvideo':
                    Album.objects.create(userid = userid, albumphoto=albumphoto,albumvideo=None,albummemo=albummemo,albumlocation=albumlocation,albumdate=albumdate,albumtype=albumtype)
                    Album.objects.filter(id=id).delete()
                    a = Album.objects.all()
                    return redirect(f"/albumdetail/{a.last().id}")
                else:
                    Album.objects.create(userid = userid, albumphoto=albumphoto,albumvideo=Album.objects.filter(id=id)[0].albumvideo,albummemo=albummemo,albumlocation=albumlocation,albumdate=albumdate,albumtype=albumtype)
                    Album.objects.filter(id=id).delete()
                    a = Album.objects.all()
                return redirect(f"/albumdetail/{a.last().id}")
        elif albumphoto == None and albumvideo:
                if clearphoto == 'clearphoto' and clearvideo == 'clearvideo':
                    Album.objects.create(userid = userid, albumphoto=None,albumvideo=albumvideo,albummemo=albummemo,albumlocation=albumlocation,albumdate=albumdate,albumtype=albumtype)
                    Album.objects.filter(id=id).delete()
                    a = Album.objects.all()
                    return redirect(f"/albumdetail/{a.last().id}")
                elif clearphoto == 'clearphoto' and clearvideo != 'clearvideo':
                    Album.objects.create(userid = userid, albumphoto=None,albumvideo=albumvideo,albummemo=albummemo,albumlocation=albumlocation,albumdate=albumdate,albumtype=albumtype)
                    Album.objects.filter(id=id).delete()
                    a = Album.objects.all()
                    return redirect(f"/albumdetail/{a.last().id}")
                elif clearphoto != 'clearphoto' and clearvideo == 'clearvideo':
                    Album.objects.create(userid = userid, albumphoto=Album.objects.filter(id=id)[0].albumphoto,albumvideo=albumvideo,albummemo=albummemo,albumlocation=albumlocation,albumdate=albumdate,albumtype=albumtype)
                    Album.objects.filter(id=id).delete()
                    a = Album.objects.all()
                    return redirect(f"/albumdetail/{a.last().id}")
                else:
                    Album.objects.create(userid = userid, albumphoto=Album.objects.filter(id=id)[0].albumphoto,albumvideo=albumvideo,albummemo=albummemo,albumlocation=albumlocation,albumdate=albumdate,albumtype=albumtype)
                    Album.objects.filter(id=id).delete()
                    a = Album.objects.all()
                return redirect(f"/albumdetail/{a.last().id}")

        else:
            Album.objects.create(userid = userid, albumphoto=albumphoto,albumvideo=albumvideo,albummemo=albummemo,albumlocation=albumlocation,albumdate=albumdate,albumtype=albumtype)
            Album.objects.filter(id=id).delete()
            a = Album.objects.all()
            return redirect(f"/albumdetail/{a.last().id}")


    albuminfo = Album.objects.get(id=id)
    context = {
        'typeinfo': typeinfo,
        'albuminfo': albuminfo,
    }
    return render(request, template_name="albums/albumupdate.html", context=context)

def albumdelete(request,id):
    # 다른 메소드로 왔을 때 아무런 응답 없음.
    # 이러면 요청 처리 결과가 대기로 뜨나요, 에러가 뜨나요?
    if request.method == "POST":
        Album.objects.filter(id=id).delete()
        userid = User.objects.get(id = request.user.id)
        return redirect(f"/album/{userid.id}")

def albumcalendar(request,id):
    userinfo = User.objects.get(id=id)
    allalbum = userinfo.userFor.all()
    context = {
        "allalbum": allalbum,
    }
    return render(request, template_name='albums/albumcalendar.html',context=context)
