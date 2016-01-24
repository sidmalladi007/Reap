from django.shortcuts import render
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from .models import User, Reward, Business, Customer, Transaction 

# Create your views here.

def index(request):
    if request.user.is_authenticated():
        context = {'logged_in': True}
    else:
        context = {'logged_in': False}
    return render(request, 'reap/index.html', context)

def account(request):
    context = {}
    return render(request, 'reap/account.html', context)

def username_exists(username):
    return User.objects.filter(username=username).count()

def email_exists(email):
    return User.objects.filter(email=email).count()

def create_account(request):
    if request.method == "GET":
        return render(request, 'reap/account.html')
    if request.method == "POST":
        fName = request.POST.get('firstname', '')
        lName = request.POST.get('lastname', '')
        userEmail = request.POST.get('email', '')
        uName = request.POST.get('username', '')
        uPwd = request.POST.get('password', '')
        uPwdConfirm = request.POST.get('confirm-password', '')
        business_name = request.POST.get('business_name', '')
        mid = request.POST.get('mid', '')
        phone = request.POST.get('phone', '')
    if username_exists(uName):
        context = {'error_usernameTaken': True}
        return render(request, 'reap/account.html', context)
    if email_exists(userEmail):
        context = {'error_emailExists': True}
        return render(request, 'reap/account.html', context)
    if (fName == '' or lName == '' or userEmail == '' or uName == '' or 
        uPwd == '' or uPwdConfirm == ''):
        context = {'incomplete_fields': True}
        return render(request, 'reap/account.html', context)
    if (uPwd) != (uPwdConfirm):
        context = {'password_mismatch': True}
        return render(request, 'reap/account.html', context)
    print(uName, userEmail, uPwd, fName, lName)
    new_user = User.objects.create_user(username=uName, email=userEmail, 
        password=uPwd, first_name=fName, last_name=lName)
    new_business = Business(info=new_user, name=business_name, phone=phone, mid=mid)
    new_business.save()
    # Customize login screen to include user information (i.e. full name).
    context = {'new_user': True}
    return render(request, 'reap/account.html', context)

def myrewards(request):
    if not request.user.is_authenticated():
        # Never crashes if there is no POST data. Will revert to empty string.
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        print(username)
        print(password)
        if user is not None:
            if user.is_active:
                # Creates a user session.
                login(request, user)
                # Create context to customize profile with welcome text using 
                #the user's information (i.e. full name).
                user = User.objects.get(username=username)
                rewards = user.business.reward_set.all()
                context = {'rewards': rewards}
                context['just_logged_in'] = True
                return render(request, 'reap/myrewards.html', context)
            else:
                # Create provision for disabled accounts that violated terms of 
                # use.
                context = {'disabled': True}
                return render(request, 'reap/account.html', context)
        else:
            # Redirect back to the login page if username and/or password
            # credentials are incorrect.
            context = {'incorrect_creds': True}
            return render(request, 'reap/account.html', context)
    # If the user is already logged in, allow him/her to access the profile
    # page directly without further authentication processes.
    else:
        rewards = request.user.business.reward_set.all()
        context = {'rewards': rewards}
        return render(request, 'reap/myrewards.html', context)

def new_reward(request):
    context = {}
    return render(request, 'reap/new-reward.html', context)

def add_reward(request):
    if request.method == "POST":
        reward_name = request.POST.get('rewardname', '')
        unlock_theshold = request.POST.get('unlock', '')
        if "$" in unlock_theshold:
            unlock_theshold = float(unlock_theshold[1:])
        else:
            unlock_theshold = float(unlock_theshold)
        discount_value = request.POST.get('discount', '')
        if "$" in discount_value:
            discount_value = float(discount_value[1:])
        else:
            discount_value = float(discount_value)
        start_time = request.POST.get('starting', '')
        end_time = request.POST.get('ending', '')
        description = request.POST.get('details', '')
    business = request.user.business
    new_reward = Reward(business=business, title=reward_name, amount_spent=unlock_theshold, 
        discount_dollars=discount_value, start_date=start_time, end_date=end_time, details=description)
    new_reward.save()
    rewards = request.user.business.reward_set.all()
    context = {'rewards': rewards}
    return render(request, 'reap/myrewards.html', context)

def remove(request, reward_id):
    curr_reward = Reward.objects.get(id=reward_id)
    curr_reward.delete()
    rewards = Reward.objects.all()
    context = {'deleted': True, 'rewards': rewards}
    return render(request, 'reap/myrewards.html', context)

def settings(request):
    current_radius = request.user.business.radius
    discounts = 29
    discount_price = 4.5
    total = 29*4.5
    context = {'radius': current_radius, 'discounts': discounts, 'discount_price': discount_price, 'total': total}
    return render(request, 'reap/settings.html', context)

def update_radius(request):
    radius = request.user.business.radius
    new_radius = request.POST.get('radius', '')
    if new_radius == '':
        new_radius = 99999.0
    radius = float(new_radius)
    request.user.business.radius = radius
    request.user.business.save()
    discounts = 29
    discount_price = 4.5
    total = 1.05*29*4.5
    context = {'radius': radius, 'discounts': discounts, 'discount_price': discount_price, 'total': total}
    return render(request, 'reap/settings.html', context)

def detail(request, reward_id):
    reward = Reward.objects.get(id=reward_id)
    context = {'reward': reward}
    return render(request, 'reap/details.html', context)

def signout(request):
    logout(request)
    context = {}
    return render(request, 'reap/index.html', context)

