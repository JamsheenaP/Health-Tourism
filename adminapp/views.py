from django.http import JsonResponse
from django.shortcuts import render
from adminapp.models import Places, District, Package
from userapp.models import Order, User, Login
from adminapp.models import Category

def home1(request):
    return render(request, "admin/adminhome.html")

def category(request):
    if request.method=='POST':
        cat_name=request.POST.get('category')
        cat_obj = Category()
        cat_obj.category=cat_name
        cat_obj.save()
    categories= Category.objects.all().filter(status=1)
    discat = Category.objects.all().filter(status=0)
    return render(request,"admin/category.html",{'categories':categories,'discat':discat})

def disablecat(request,id):
    cat_obj = Category.objects.get(id=id)
    cat_obj.status=0
    cat_obj.save()
    categories = Category.objects.all().filter(status=1)
    discat = Category.objects.all().filter(status=0)
    return render(request, "admin/category.html", {'categories': categories,'discat':discat})

def enablecat(request,id):
    cat_obj = Category.objects.get(id=id)
    cat_obj.status=1
    cat_obj.save()
    categories = Category.objects.all().filter(status=1)
    discat = Category.objects.all().filter(status=0)
    return render(request, "admin/category.html", {'categories': categories,'discat':discat})

def district(request):
    if request.method=='POST':
        d_name=request.POST.get('district')
        d_obj = District()
        d_obj.district_name=d_name
        d_obj.save()
    dist = District.objects.all().filter(status=1)
    disdistrict = District.objects.all().filter(status=0)
    return render(request, "admin/district.html", {'dist': dist, 'disdistrict': disdistrict})

def disabledistrict(request,id):
    d_obj = District.objects.get(id=id)
    d_obj.status=0
    d_obj.save()
    dist = District.objects.all().filter(status=1)
    disdistrict = District.objects.all().filter(status=0)
    return render(request, "admin/district.html", {'dist': dist,'disdistrict':disdistrict})

def enabledistrict(request,id):
    d_obj = District.objects.get(id=id)
    d_obj.status=1
    d_obj.save()
    dist = District.objects.all().filter(status=1)
    disdistrict = District.objects.all().filter(status=0)
    return render(request, "admin/district.html",  {'dist':dist,'disdistrict':disdistrict})

def place(request):
    if request.method=='POST':
        plac=request.POST.get('place')
        plac_obj = Places()
        plac_obj.place=plac
        plac_obj.save()
    places= Places.objects.all().filter(status=1)
    displac = Places.objects.all().filter(status=0)
    return render(request,"admin/places.html",{'places':places,'displac':displac})

def disablePlaces(request,id):
    p_obj = Places.objects.get(id=id)
    p_obj.status=0
    p_obj.save()
    places = Places.objects.all().filter(status=1)
    displac = Places.objects.all().filter(status=0)
    return render(request,"admin/places.html",{'places':places,'displac':displac})

def enablePlaces(request,id):
    p_obj = Places.objects.get(id=id)
    p_obj.status=1
    p_obj.save()
    places = Places.objects.all().filter(status=1)
    displac = Places.objects.all().filter(status=0)
    return render(request,"admin/places.html",{'places':places,'displac':displac})

def geteditPackage(request):
    if request.method=='POST':
        title = request.POST.get('title')
        package = Package.objects.get(title__iexact=title)
        district = District.objects.all().filter(status=1)
        plac = Places.objects.all().filter(status=1)
        cats = Category.objects.all().filter(status=1)
        return render(request,"admin/geteditPackage.html",{'package':package,'district':district,'plac':plac,'cats':cats})
    return render(request, "admin/geteditPackage.html")

def updatePackage(request):
    if request.method=='POST':
        package = Package.objects.get(id=request.POST.get('id'))
        package.title = request.POST.get('title1')
        package.district = District.objects.get(id=request.POST.get("district"))
        package.place = Places.objects.get(id=request.POST.get("place"))
        package.category= Category.objects.get(id=request.POST.get("category"))
        package.description = request.POST.get("desc")
        package.itin = request.POST.get('itin')
        package.price = request.POST.get("price")
        if len(request.FILES)!=0:
            package.image = request.FILES['image']
        package.save()
        district = District.objects.all().filter(status=1)
        plac = Places.objects.all().filter(status=1)
        cats = Category.objects.all().filter(status=1)
        return render(request,"admin/geteditPackage.html",{'package':package,'district':district,'plac':plac,'cats':cats})
    return render(request, "admin/geteditPackage.html")

def logout(request):
    del request.session['userid']
    categories = Category.objects.all().filter(status=1)
    bestsellers = Package.objects.order_by('-sold_package')[:10]
    return render(request, "user/login.html", context={'categories': categories, 'bestsellers': bestsellers})


def addPackage(request):
    if request.method=='POST':
        package=Package()
        package.title=request.POST.get('title')
        package.district=District.objects.get(id=request.POST.get('district'))
        package.category = Category.objects.get(id=request.POST.get('category'))
        package.place = Places.objects.get(id=request.POST.get('place'))
        package.price=request.POST.get('price')
        package.description=request.POST.get('desc')
        package.itin=request.POST.get('itin')
        package.no_packages = request.POST.get('copy')
        if len(request.FILES)!=0:
            package.image = request.FILES['image']
        package.save()
    district=District.objects.all().filter(status=1)
    plac = Places.objects.all().filter(status=1)
    cats = Category.objects.all().filter(status=1)
    return render(request,"admin/addPackage.html",{'district':district,'cats':cats,'plac':plac,})

def gettitles(request):
    id=request.GET.get('district')
    print("called gettitles")
    package = Package.objects.all().filter(district_id = id)
    json_res = []
    for record in package:
        json_obj = dict(
            title=record.title,
            id=record.id,
        )
        json_res.append(json_obj)
        print(json_res)
    return JsonResponse(json_res, safe=False)

def editstock(request):
    id=request.POST.get('title2')
    package=Package.objects.get(id=id)
    package.save()
    districts = District.objects.all().filter(status=1)
    plac = Places.objects.all().filter(status=1)
    cats = Category.objects.all().filter(status=1)
    return render(request, "admin/addPackage.html", {'districts': districts, 'cats': cats, 'plac': plac})

def latestorders(request):
    orders = Order.objects.all()
    return render(request,"admin/latestorders.html",{'orders':orders})

def enableusers(request):
    users = Login.objects.all().filter(role=1)
    return render(request,"admin/enableusers.html",{'users':users})

def enableUser(request,id):
    user = Login.objects.get(id=id)
    user.role=2
    user.save()
    users = Login.objects.all().filter(role=1)
    return render(request, "admin/enableusers.html", {'users': users})

def viewusers(request):
    users = User.objects.all()
    return render(request,"admin/allusers.html",{'users':users})
