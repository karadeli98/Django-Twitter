import re
from time import process_time_ns
from django.shortcuts import render, redirect
import hashlib
from .models import User, Post, friendShip
from django.contrib.auth.models import User as auth
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.


        

def loginPage(request):
    
    if(request.method == "POST"):
        name = request.POST['username']
        password =  hashlib.sha256(request.POST['password'].encode('utf-8')).hexdigest()

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/homepage')
        else:
            return render(request, "login.html", {'error': True})
            
    return render(request, "login.html")


def signup(request):

    isUsed = False

    if(request.method == "POST"):
        error = ""
        fullname = request.POST['fullName']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        try:
            firstName, lastName = fullname.split(" ")
        except:
            firstName = fullname
            lastName = ""

        try:
            userNames = (User.objects.get(userName = username))
        except:
            userNames = None
        if(userNames != None):
            error = "Bu kullanıcı adı daha önce alınmış"
            isUsed = True
            return render(request, "signup.html", {'isUsed': isUsed, 'error': error})

        if(len(password) < 8):
            error = "Şifre 8 karakterden küçük olamaz"
            isUsed = True
            return render(request, "signup.html", {'isUsed': isUsed, 'error': error})

        if(len(fullname) < 4):
            error = "İsim 4 karakterden küçük olamaz"
            isUsed = True
            return render(request, "signup.html", {'isUsed': isUsed, 'error': error})

        if(len(username) < 4):
            error = "Kullanıcı adı 4 karakterden küçük olamaz"
            isUsed = True
            return render(request, "signup.html", {'isUsed': isUsed, 'error': error})

        if(len(email) < 11):
            error = "Kullanılabilir bir mail giriniz!!"
            isUsed = True
            return render(request, "signup.html", {'isUsed': isUsed, 'error': error})


        new_user = User(name= firstName, surname = lastName,userName = username,password = hashed_password, email = email)
        authuser = auth.objects.create_user(username, email, hashed_password)
        authuser.save()
        new_user.save()
        return redirect('/')
        
    return render(request, "signup.html",{'isUsed': isUsed})

def homepage(request):

    user = request.user
    userObj = User.objects.get(userName = user)

    followsList = []
    follows = friendShip.objects.filter(user1 = user)
    if len(follows) == 0:
        pass
    else:
        for i in range(len(follows)):
            followsList.append(follows[i].user2)

    if(request.method == "POST"):
        try:
            context = request.POST['context'] 
            if(len(context) > 0 and len(context) < 240) :      
                post = Post(context = context, ownerUsername = userObj.userName)
                post.save()
                
        except:
            pass

    followsPost = Post.objects.filter(ownerUsername__in = followsList) | Post.objects.filter(ownerUsername = user)
    

    return render(request,'homepage.html', {'posts': followsPost})



def profile(request, pk):
    try:
        user = User.objects.get(userName = pk)
    except: 
        user = None
    
    if(user == None and pk != "admin"):
        return render(request, '404.html')
    ownProfile = False
    if(str(request.user) == pk):
        ownProfile = True

    active_user = request.user
    isFriend = False

    friendObj = friendShip.objects.filter(user1 = active_user, user2 = pk)

    if len(friendObj) != 0:
        isFriend = True
    if(request.method == "POST"):

        if(isFriend == False):

            profile_owner = User.objects.get(userName = pk).userName
            friends = friendShip(user1 = active_user, user2 = profile_owner)
            friends.save()
            isFriend = True
        else:

            friendObj.delete()
            isFriend = False

    

            
    posts = Post.objects.filter(ownerUsername = pk)
    context = {'posts': posts, 'isFriend' : isFriend, 'ownProfile': ownProfile}
    return render(request, 'profile.html', context)


def logOut(request):
    logout(request)
    return redirect('/')



def search(request,pk):
    users = User.objects.filter(userName__contains = pk).exclude(userName = request.user)
    return render(request, 'search.html', {'users': users})
