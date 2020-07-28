from django.shortcuts import render,redirect
from .forms import User_Form
from . models import Category,Products,Cart,Order
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

c=Category.objects.all()
p=Products.objects.all()
# Create your views here.
def index(request):
    d={'clist':c,'plist':p}
    return render(request,'index.html',d)

def addUser(request):
    if request.method =="POST":
        f=User_Form(request.POST)
        f.save()
        return redirect('/')
    else:
        f=User_Form()
        b={'form':f}
        return render(request,'form.html',b)

def user_login(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        passcode=request.POST.get('password')
        user=authenticate(request,username=uname,password=passcode)
        if user is not None:
            request.session['user_id1']=uname
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html',{'err_msg':'Incorrect Username or Password'})
    else:
        return render(request,'login.html')

def user_logout(request):
    request.session.flush()
    logout(request)
    return redirect('/')

def getProductByCategory(request):
    id=request.GET.get('id')
    pl=Products.objects.filter(category_id=id)
    d={'clist':c,'plist':pl}
    return render(request,'index.html',d)

def searchProduct(request):
    if request.method  == 'POST':
        pname=request.POST.get('sp')
        pl=Products.objects.filter(pname__icontains = pname)
        a={'clist':c,'plist':pl}
        return render(request,'searchProduct.html',a)
    else:
        d={'clist':c,'plist':p}
        return render(request,'searchProduct.html',d)

def addToCart(request):
    pid=request.GET.get('pid')
    prd=Products.objects.get(id=pid)
    uname=request.session.get('user_id1')
    usr=User.objects.get(username=uname)
    c=Cart()
    c.products=prd
    c.user=usr
    c.save()
    return redirect('/')

def cartList(request):
    u_name=request.session.get('user_id1')
    usr=User.objects.get(username=u_name)
    if request.method=='POST':
        totalBill=request.POST.get("bill")
        order=Order()
        order.totalBill=totalBill
        order.user=usr
        order.save()
        cartlist=Cart.objects.filter(user_id=usr.id)
        for i in cartlist:
            i.delete()
        return redirect("/myOrder")

    else:
        cartlist=Cart.objects.filter(user_id=usr.id)
        totalBill=0
        for i in cartlist:
            totalBill = totalBill + i.products.price

        d={'clist':c,'cartlist':cartlist,'totalBill':totalBill}
        return render(request,'cartList.html',d)

def deleteProduct_userCart(request,id):
    c=Cart.objects.get(id=id)
    c.delete()
    return redirect('/cartList')

def editProfile(request):
    u_name=request.session.get('user_id1')
    usr=User.objects.get(username=u_name)
    if request.method == "POST":
        f=User_Form(request.POST,instance=usr)
        f.save()
        return redirect('/')
    else:
        f=User_Form(instance=usr)
        d={'clist':c,'form':f}
        return render(request,'form.html',d)

def myOrder(request):
    u_name=request.session.get('user_id1')
    usr=User.objects.get(username=u_name)
    orlist=Order.objects.filter(user_id=usr.id)
    d={'catlist':c,'orderlist':orlist}
    return render(request,'myorder.html',d)

from .models import MyImage
from .forms import MyImageForm
def imagedata(request):

    if request.method=='POST':
        f=MyImageForm(request.POST,request.FILES)
        f.save()
        f=MyImageForm
        imagelist=MyImage.objects.all()
        return render(request,'imageaccess.html',{'imagelist':imagelist,'form':f})
    else:
        f=MyImageForm
        imagelist=MyImage.objects.all()
        return render(request,'imageaccess.html',{'imagelist':imagelist,'form':f})

def productList(request):
    d={'p':p}
    return render(request,'productList.html',d)
