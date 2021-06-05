from django.shortcuts import render
from adminapp.models import Category,Package,Places
from userapp.models import User, Login, Order
from datetime import date
from warnings import catch_warnings
from django.http import HttpResponse

# Create your views here.
def index(request):
    categories = Category.objects.all().filter(status=1)
    packages=Package.objects.all()[:10]
    bestsellers = Package.objects.order_by('-sold_package')[:10]
    return render(request,"user/index.html",context={'categories':categories,'packages':packages,'bestsellers':bestsellers})

def index2(request):
    categories = Category.objects.all().filter(status=1)
    packages=Package.objects.all()[:10]
    bestsellers = Package.objects.order_by('-sold_package')[:10]
    return render(request,"user/index2.html",context={'categories':categories,'packages':packages,'bestsellers':bestsellers})

def profile(request):
    categories = Category.objects.all().filter(status=1)
    packages = Package.objects.all()[:10]
    bestsellers = Package.objects.order_by('-sold_package')[:10]
    user = Login.objects.get(id=request.session['userid'])
    client = User.objects.get(loginid_id=request.session['userid'])
    return render(request, "user/profile.html",context={'categories': categories, 'packages': packages, 'bestsellers': bestsellers,'user':user,'client':client})

def profile2(request):
    categories = Category.objects.all().filter(status=1)
    packages = Package.objects.all()[:10]
    bestsellers = Package.objects.order_by('-sold_package')[:10]
    user = Login.objects.get(id=request.session['userid'])
    client = User.objects.get(loginid_id=request.session['userid'])
    return render(request, "user/profile2.html",context={'categories': categories, 'packages': packages, 'bestsellers': bestsellers,'user':user,'client':client})

def editprofile(request):
    categories = Category.objects.all().filter(status=1)
    packages = Package.objects.all()[:10]
    bestsellers = Package.objects.order_by('-sold_package')[:10]
    user = Login.objects.get(id=request.session['userid'])
    client = User.objects.get(loginid_id=request.session['userid'])
    if request.method=='POST':
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        user.uname = uname
        user.password=password
        client.name = name
        client.mobile = mobile
        client.email = email
        client.save()
        user.save()
        return render(request, "user/editprofile.html",context={'categories': categories, 'packages': packages, 'bestsellers': bestsellers, 'user': user,'client': client})
    return render(request, "user/editprofile.html",context={'categories': categories, 'packages': packages, 'bestsellers': bestsellers, 'user': user,'client': client})

def editprofile2(request):
    categories = Category.objects.all().filter(status=1)
    packages = Package.objects.all()[:10]
    bestsellers = Package.objects.order_by('-sold_package')[:10]
    user = Login.objects.get(id=request.session['userid'])
    client = User.objects.get(loginid_id=request.session['userid'])
    if request.method=='POST':
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        user.uname = uname
        user.password=password
        client.name = name
        client.mobile = mobile
        client.email = email
        client.save()
        user.save()
        return render(request, "user/editprofile2.html",context={'categories': categories, 'packages': packages, 'bestsellers': bestsellers, 'user': user,'client': client})
    return render(request, "user/editprofile2.html",context={'categories': categories, 'packages': packages, 'bestsellers': bestsellers, 'user':user,'client': client})
def index3(request):
    categories = Category.objects.all().filter(status=1)
    packages=Package.objects.all()[:10]
    bestsellers = Package.objects.order_by('-sold_package')[:10]
    return render(request,"user/index3.html",context={'categories':categories,'packages':packages,'bestsellers':bestsellers})

def bestpackage(request,id):
    categories = Category.objects.all().filter(status=1)
    packages = Package.objects.all()[:10]
    bestsellers = Package.objects.order_by('-sold_package')[:10]
    package = Package.objects.get(id=id)
    return render(request,"user/bestpackage.html",context={'categories':categories,'packages':packages,'bestsellers':bestsellers,'package':package})

def bestpackage2(request,id):
    categories = Category.objects.all().filter(status=1)
    packages = Package.objects.all()[:10]
    bestsellers = Package.objects.order_by('-sold_package')[:10]
    package = Package.objects.get(id=id)
    return render(request,"user/bestpackage2.html",context={'categories':categories,'packages':packages,'bestsellers':bestsellers,'package':package})

def login(request):
    if request.method=='POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        if Login.objects.filter(username=uname,password=pwd).exists():
            loginobj = Login.objects.get(username=uname,password=pwd)
            request.session['userid']=loginobj.id
            role=loginobj.role
            if role==0:
                return render(request,"admin/adminhome.html")
            if role==1:
                categories = Category.objects.all().filter(status=1)
                packages = Package.objects.all()[:10]
                bestsellers = Package.objects.order_by('-sold_package')[:10]
                user = Login.objects.get(id=request.session['userid'])
                return render(request,"user/index3.html",{'categories': categories, 'packages': packages, 'bestsellers': bestsellers,'user':user})
            elif role == 2:
                categories = Category.objects.all().filter(status=1)
                packages = Package.objects.all()[:10]
                bestsellers = Package.objects.order_by('-sold_package')[:10]
                user = Login.objects.get(id=request.session['userid'])
                client = User.objects.get(loginid_id=request.session['userid'])
                return render(request, "user/profile.html",{'categories': categories, 'packages': packages, 'bestsellers': bestsellers,'user':user,'client':client})
            else:
                return render(request, "user/index.html")

        return render(request, "user/login.html", context={'error': 'Login failed'})
    categories = Category.objects.all().filter(status=1)
    bestsellers = Package.objects.order_by('-sold_package')[:10]
    return render(request, "user/login.html", context={'categories': categories, 'bestsellers': bestsellers})


def register(request):
    if request.method=='POST':
        loginobj = Login()
        loginobj.username = request.POST.get('uname')
        loginobj.password = request.POST.get('pwd')
        loginobj.save()
        if Login.objects.filter(username=request.POST.get('uname')).exists():
            user = User()
            user.name = request.POST.get('name')
            user.dob = request.POST.get('dob')
            user.email = request.POST.get('email')
            user.mobile=request.POST.get('mob')
            user.loginid=loginobj
            user.save()
            if User.objects.filter(loginid = loginobj).exists():
                categories = Category.objects.all().filter(status=1)
                packages = Package.objects.all()[:10]
                bestsellers = Package.objects.order_by('-sold_package')[:10]
                return render(request,"user/login.html", context={'categories':categories,'bestsellers':bestsellers,'packages':packages})
        return render(request,"user/register.html",context={'error':'Registration failed'})
    categories = Category.objects.all().filter(status=1)
    bestsellers = Package.objects.order_by('-sold_package')[:10]
    return render(request, "user/register.html", context={'categories': categories, 'bestsellers': bestsellers})

def cat_packages(request,id):
    categories=Category.objects.all().filter(status=1)
    bestsellers = Package.objects.order_by('-sold_package')[:10]
    if Package.objects.filter(category_id = id).exists():
        packages= Package.objects.filter(category_id = id)
        return  render(request,"user/catpackage.html",{'packages':packages,'categories':categories,'bestsellers':bestsellers})
    else:
        return render(request, "user/catpackage.html",{'packagemess':'No Packages in the selected category','categories':categories,'bestsellers':bestsellers})

def cat_packages2(request,id):
    categories=Category.objects.all().filter(status=1)
    bestsellers = Package.objects.order_by('-sold_package')[:10]
    if Package.objects.filter(category_id = id).exists():
        packages= Package.objects.filter(category_id = id)
        return  render(request,"user/catpackage2.html",{'packages':packages,'categories':categories,'bestsellers':bestsellers})
    else:
        return render(request, "user/catpackage2.html",{'packagemess':'No Packages in the selected category','categories':categories,'bestsellers':bestsellers})

def payment(request,id):
    categories = Category.objects.all().filter(status=1)
    bestsellers = Package.objects.order_by('-sold_package')[:10]
    if 'userid' not in request.session:
        return render(request, "user/login.html", context={'categories': categories, 'bestsellers': bestsellers})
    if request.method=='POST':
        package = Package.objects.get(id=id)
        user = Login.objects.get(id = request.session['userid'])
        cardnum = request.POST.get("cardnumber")
        cvv=request.POST.get('cvv')
        exp = request.POST.get('exp')
        c_date = date.today()
        amount = request.POST.get('amount')
        copies=request.POST.get('copies')
        booking_date=request.POST.get('booking_date')
        slots=request.POST.get('slots')
        order = Order()
        order.package=package
        order.user=user
        order.card_num=cardnum
        order.cvv=cvv
        order.expiry=exp
        order.order_date=c_date
        order.amount=amount
        order.copies=copies
        order.booking_date=booking_date
        order.slots=slots
        order.status=1
        order.save()

        if Order.objects.filter(package_id=id).exists():
            package_copies = package.no_packages
            package.copies = package_copies-int(copies)
            package.sold_package = package.sold_package
            package.sold_package = package.sold_package+int(copies)
            package.save()
            categories = Category.objects.all()
            packages = Package.objects.all()[:10]
            return render(request, "user/index2.html", context={'categories': categories, 'bestsellers': bestsellers, 'packages': packages,'message':'Payment Successful'})
        else:
            package = Package.objects.get(id=id)
            return render(request, "user/payment.html", {'categories': categories, 'bestsellers': bestsellers,'package': package,'message':'payment failed'})
    else:
        package = Package.objects.get(id=id)
        return render(request, "user/payment.html",{'package':package,'categories': categories, 'bestsellers': bestsellers})

def logout(request):
    print("called logout")
    del request.session['userid']
    categories = Category.objects.all().filter(status=1)
    bestsellers = Package.objects.order_by('-sold_package')[:10]
    return render(request, "user/login.html", context={'categories': categories, 'bestsellers': bestsellers})

def vieworders(request):
    categories = Category.objects.all().filter(status=1)
    bestsellers = Package.objects.order_by('-sold_package')[:10]
    if 'userid' not in request.session:
       return render(request, "user/login.html",context={'categories':categories,'bestsellers':bestsellers})
    userid = request.session['userid']
    if Order.objects.filter(user_id=userid).exists():
        orders = Order.objects.order_by('-order_date','-id').filter(user_id=userid)
        return render(request,"user/vieworders.html",{'orders':orders,'categories':categories,'bestsellers':bestsellers})
    else:
        return render(request, "user/vieworders.html", {'ordermess':'No order history','categories':categories,'bestsellers':bestsellers})

def cancelorder(request,id):
    if 'userid' not in request.session:
        categories = Category.objects.all().filter(status=1)
        bestsellers = Package.objects.order_by('-sold_package')[:10]
        return render(request, "user/login.html", context={'categories': categories, 'bestsellers': bestsellers})
    order = Order.objects.get(id = id)
    order.status=2
    order.save()
    package = Package.objects.get(id = order.package.id)
    copies = package.no_packages + order.copies
    package.copies = copies
    package.save()
    userid = request.session['userid']
    if Order.objects.filter(user_id=userid).exists():
        orders = Order.objects.order_by('-order_date').filter(user_id=userid)
        return render(request, "user/vieworders.html", {'orders': orders})
    else:
        return render(request, "user/vieworders.html", {'ordermess': 'No order history'})
