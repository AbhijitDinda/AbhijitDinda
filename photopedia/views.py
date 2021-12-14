from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.
from .models import *
from .forms import *

# account varification by email, password


def authenticate(request, email, password):
    try:
        account = Account.objects.get(active=True, email=email)
    except Account.DoesNotExist:
        account = None

    if account:
        if check_password(password, account.password) and check_password(password, account.password_confirm):
            request.session['account_id'] = account.id
        else:
            account = None

    return account


def AuthUser(id=0, active=True):
    try:
        user = Account.objects.get(id=id, active=active)
    except Account.DoesNotExist:
        user = None

    return user


def is_authenticated(request):
    if request.session.has_key('account_id'):
        return True
    return False

# ------------ Auth ------------


def signup(request):
    if request.session.has_key('account_id'):
        redirect('home')

    if request.method == 'POST':
        signupForm = SignUpForm(request.POST)
        if signupForm.is_valid():
            email = request.POST.get('email').strip()
            password = request.POST.get('password').strip()
            password_confirm = request.POST.get('password_confirm').strip()

            try:
                account = Account.objects.get(email=email)
            except Account.DoesNotExist:
                account = None

            if account is None:
                hash_password = make_password(password_confirm)
                hash_password_confirm = make_password(password_confirm)
                if check_password(password, hash_password):
                    signupForm = signupForm.save(commit=False)
                    signupForm.password = hash_password
                    signupForm.password_confirm = hash_password_confirm
                    signupForm.save()
                    messages.success(request, 'Account Created for ' + email)
                    return redirect('login')
                else:
                    messages.error(request, 'Password mismatch')
            else:
                messages.error(request, 'Account already exists')
        else:
            messages.error(request, 'Form is Not Valid')
    else:
        signupForm = SignUpForm(None)

    context = {'form': signupForm}
    return render(request, 'auth/signup.html', context)


def login(request):
    if request.session.has_key('account_id'):
        redirect('home')

    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            email = request.POST.get('email').strip()
            password = request.POST.get('password').strip()
            account = authenticate(request, email=email, password=password)
            if account is not None:
                return redirect('home')
        else:
            messages.error(request, 'Email or Password is incorrect')
    else:
        loginForm = LoginForm(None)

    context = {'form': loginForm}
    return render(request, "auth/login.html", context)


def logout(request):
    try:
        del request.session['account_id']
    except:
        pass
    return redirect('login')


def forgotpassword(request):
    if request.session.has_key('account_id'):
        redirect('home')

    return render(request, "auth/forgotpassword.html")


# ------------ common ------------


def index(request):
    account_id = 0
    if request.session.has_key('account_id'):
        account_id = request.session['account_id']

    account = AuthUser(account_id)

    try:
        pins = Pin.objects.filter(active=True, is_deleted=False)
    except Pin.DoesNotExist:
        pins = None

    context = {
        'is_authenticated': is_authenticated(request),
        'account': account,
        "pins": pins,
        "categories": pin_category
    }
    return render(request, "index.html", context)


def search(request, action):
    account_id = 0
    if request.session.has_key('account_id'):
        account_id = request.session['account_id']

    account = AuthUser(account_id)

    query = ""
    if ('q' in request.GET) and request.GET['q'].strip():
        query = request.GET.get('q', None)

    try:
        if query and action == "category":
            pins = Pin.objects.filter(active=True, is_deleted=False, category=query)
        elif query and action == "top":
            pins = Pin.objects.filter(active=True, is_deleted=False, title=query)
        else:
            pins = Pin.objects.filter(active=True, is_deleted=False)
    except Pin.DoesNotExist:
        pins = None

    context = {
        'is_authenticated': is_authenticated(request),
        'account': account,
        "pins": pins,
        "categories": pin_category
    }
    return render(request, "index.html", context)



# ------------ profile ------------


def profile(request, pk):

    try:
        pins = Pin.objects.filter(active=True, account_id=pk)
        account = AuthUser(pk)
    except Pin.DoesNotExist:
        account = None
        pins = None

    context = {
        'is_authenticated': is_authenticated(request),
        'account': account,
        'pins': pins
    }
    return render(request, "profile.html", context)


def setting(request):
    if not request.session.has_key('account_id'):
        return redirect('login')

    account_id = request.session['account_id']
    account = AuthUser(account_id)

    if request.method == "POST":
        form = ProfileFrom(request.POST, request.FILES, instance=account)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.account = account
            profile.save()
            messages.success(
                request, 'You have successfully updated your profile,')
            return redirect('setting')
        else:
            messages.error(request, 'Form is Not Valid')
    else:
        form = ProfileFrom(instance=account)

    context = {
        'is_authenticated': is_authenticated(request),
        'account': account,
        'form': form
    }
    return render(request, "setting.html", context)


# ------------ Pin ------------


def pin_new(request):
    if not request.session.has_key('account_id'):
        return redirect('login')

    account_id = request.session['account_id']
    account = AuthUser(account_id)

    if request.method == "POST":
        form = PinForm(request.POST, request.FILES)
        if form.is_valid():
            pin = form.save(commit=False)
            pin.account = account
            pin.save()
            form = PinForm(None)
            messages.success(request, 'You have successfully created a pin')
        else:
            messages.error(request, 'Form is Not Valid')
    else:
        form = PinForm(None)

    context = {
        'is_authenticated': is_authenticated(request),
        'account': account,
        'form': form,
        'pin': None
    }
    return render(request, "pin/pin.html", context)


def pin_edit(request, pk):
    if not request.session.has_key('account_id'):
        return redirect('login')

    account_id = request.session['account_id']
    account = AuthUser(account_id)

    pin = get_object_or_404(Pin, pk=pk, is_deleted=False)
    if request.method == "POST":
        form = PinForm(request.POST, request.FILES, instance=pin)
        if form.is_valid():
            pin = form.save(commit=False)
            pin.account = account
            pin.save()
            messages.success(request, 'You have successfully updated your pin')
            return redirect('pin_edit', pk=pk)
        else:
            messages.error(request, 'Form is Not Valid')
    else:
        form = PinForm(instance=pin)

    context = {
        'is_authenticated': is_authenticated(request),
        'account': account,
        'form': form,
        'pin': pin
    }
    return render(request, "pin/pin.html", context)


def pin_view(request, pk):
    if not request.session.has_key('account_id'):
        return redirect('login')

    account_id = request.session['account_id']
    account = AuthUser(account_id)

    pin = get_object_or_404(Pin, pk=pk, is_deleted=False)

    context = {
        'is_authenticated': is_authenticated(request),
        'account': account,
        'pin': pin
    }
    return render(request, "pin/pin_view.html", context)


def pin_remove(request, pk):
    if not request.session.has_key('account_id'):
        return redirect('login')

    account_id = request.session['account_id']
    account = AuthUser(account_id)

    if account is not None:
        try:
            pin = Pin.objects.get(pk=pk, account_id=account_id)
        except Pin.DoesNotExist:
            pin = None

        if pin is not None:
            pin.is_deleted = True
            pin.save()

    return redirect('home')
