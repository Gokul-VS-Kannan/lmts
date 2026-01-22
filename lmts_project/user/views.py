from django.shortcuts import render,redirect
from owner.models import Customuser
from.models import Userdetails,Orderdetails
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.



def user_reg(request):
    return render(request,'user_reg.html')

def user_login(request):
    return render(request,'user_login.html')

def reguser(request):
    if request.method == "POST":
        full_name=request.POST['name']
        profile_pic =request.FILES['Image']
        user_name=request.POST['uname']
        password=request.POST['pwd']
        age=request.POST['age']
        phone_number=request.POST['phnnum']
        email =request.POST['email']
        address =request.POST['address']

        # Check if 'Image' key is present in request.FILES
        # if 'Image' in request.FILES:
            # profile_pic = request.FILES['Image']
        # else:
            # pass

        user=Customuser.objects.create_user(
            username=user_name,
            password=password,
            is_admin=False,
            is_driver=False,
            is_mechanic=False,
            is_user=True,
            )
        
        userdetail=Userdetails(
            fullname=full_name,
            profilepic=profile_pic,
            username=user,
            age=age,
            mobile=phone_number,
            email=email,
            address=address,
            )

        user.save()
        userdetail.save()
        
        return render(request,'user_login.html')
    else:
        return render(request,'user_reg.html')
    

def userlogin(request):
    username=request.POST['uname']
    pswd=request.POST['pwd']
    user=authenticate(request,username=username,password=pswd)
    if user is not None and user.is_user:
        login(request,user)
        return render(request,'user_dash.html')
    else:
        return render(request,"user_login.html")


def userlogout(request):
    logout(request)
    return redirect('home')

@login_required
def usercon(request):
    return render(request,'user_contact.html')

@login_required
def userabt(request):
    return render(request,'user_about.html')

@login_required
def user_dash(request):
    return render(request,'user_dash.html')

@login_required
def viewprofile(request):
    profile=Userdetails.objects.get(username=request.user)
    return render(request,'user_profile.html',{'profile':profile})

@login_required
def editprofile(request):
    return render(request,'user_profile_edit.html')

@login_required
def edituser(request):
    if request.method == 'POST':
        # Get the updated values from the POST request
        
        fullname = request.POST.get('name')
        age = request.POST.get('age')
        mobile = request.POST.get('phnnum')
        email = request.POST.get('email')
        address = request.POST.get('address')
        profilepic = request.FILES.get('Image')
        
        user=Userdetails.objects.get(username=request.user)

        # Get the old values
        old_fullname = user.fullname
        old_age = user.age
        old_mobile = user.mobile
        old_email = user.email
        old_address = user.address
        old_profilepic = user.profilepic

        # Update the user object with the new values
        user.fullname = fullname if fullname else old_fullname
        user.age = age if age else old_age
        user.mobile = mobile if mobile else old_mobile
        user.email = email if email else old_email
        user.address = address if address else old_address
        user.profilepic = profilepic if profilepic else old_profilepic
       
        #save updated user object   
        user.save(update_fields=['fullname','age','mobile','email','address','profilepic'])

        
        return redirect('user:viewprofile')
    else:
        return render(request,'user_dash.html') 


@login_required
def placeorder(request):
    return render(request,'order_placing.html') 

@login_required
def orderplacing(request):
    if request.method == "POST":
        user=request.user
        # material = request.POST.get('item')
        # weight = request.POST.get('quantity')
        # ship_from = request.POST.get('fromaddress')
        # ship_to = request.POST.get('toaddress')
        # pick_date = request.POST.get('orderdate')
        # deldate = request.POST.get('deldate')
        material=request.POST['item']
        weight=request.POST['quantity']
        ship_from=request.POST['fromaddress']
        ship_to=request.POST['toaddress']
        pick_date=request.POST['orderdate']
        deldate=request.POST['deldate']

        order=Orderdetails(
            username=user,
            material=material,
            weight=weight,
            shipfrom=ship_from,
            shipto=ship_to,
            pickdate=pick_date,
            deliverydate=deldate,
        )
          
        order.save()

        return render(request,'order_sucess.html')     

@login_required
def orderstatus(request):
    order=Orderdetails.objects.filter(username=request.user)
    return render(request,'order_status.html',{'order':order})

@login_required    
def orderhistory(request):
    order_history = Orderdetails.objects.filter(username=request.user)
    return render(request, 'order_history.html', {'order_history': order_history}) 

@login_required
def editusername(request):
    return render(request,'user_login_edit.html')

@login_required
def editlogin(request):
    if request.method == "POST":
        new_username=request.POST['uname']
        new_password=request.POST['pwd']

        if not new_username:
            return redirect('user:editusername')

        try:
            # Get the current user
            user = Customuser.objects.get(username=request.user)

            # Update the username in the Customuser model
            user.username = new_username
            user.save()

            # Check if the password is not empty
            if new_password:
                # Update the password
                user.set_password(new_password)
                user.save()
                return render(request,'user_login.html')
            
            return render(request,'user_login.html')
        
        except Exception as e:
            print(e)
            return render(request,'user_login_edit.html')  
    return render(request, 'user_login.html') 

@login_required
def userdelete(request):
    if request.method == "POST":
        user=request.user

        try:
            # Retrive the associated user details
            user_detail=Userdetails.objects.get(username=user)

            # Retrive the associated order details
            orders=Orderdetails.objects.filter(username=user)

            # delete action
            user_detail.delete()

            orders.delete()

            # deleting the account
            user.delete()
            
            # logout after deletion
            return redirect('home')
        
        except Exception as e:
            print(e)
            return render(request,'user_dash.html')
