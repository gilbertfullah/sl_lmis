from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic.edit import CreateView
from .form import JobSeekerRegisterForm, CompanyRegisterForm, GovernmentRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, JobSeeker, Employer, Government
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def register(request):
    return render(request, 'register.html')

def JobSeekerRegister(request):
    if request.user.is_authenticated:
        return redirect("login")
    else:
        if request.method == "POST":
            form = JobSeekerRegisterForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f"{user} was successfully registered")
                return redirect("login")
        else:
            form = JobSeekerRegisterForm()
            messages.error(request, "Form is not valid")
            context = {'form':form}
            return render(request, 'jobseeker_register.html', context)

    return render(request, 'jobseeker_register.html', {'form':form})

@login_required
def jobseeker_profile(request):
    you = request.user
    profile = JobSeeker.objects.filter(user=you).first()
    user_skills = Skill.objects.filter(user=you)
    if request.method == 'POST':
        form = NewSkillForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = you
            data.save()
            return redirect('/')
    else:
        form = NewSkillForm()
    context = {
        'u': you,
        'profile': profile,
        'skills': user_skills,
        'form': form,
        'profile_page': "active",
    }
    return render(request, 'profile.html', context)

@login_required
def edit_jobseeker_profile(request):
    you = request.user
    profile = JobSeeker.objects.filter(user=you).first()
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = you
            data.save()
            return redirect('/')
    else:
        form = ProfileUpdateForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'edit_profile.html', context)

@login_required
def jobseeker_profile_view(request, id):
    p = Profile.objects.filter(id=id).first()
    you = p.user
    user_skills = Skill.objects.filter(user=you)
    context = {
        'u': you,
        'profile': p,
        'skills': user_skills,
    }
    return render(request, 'profile.html', context)


def jobseeker_details(request):
    return render(request, 'details.html')

@login_required
@csrf_exempt
def delete_skill(request, pk=None):
    if request.method == 'POST':
        id_list = request.POST.getlist('choices')
        for skill_id in id_list:
            Skill.objects.get(id=skill_id).delete()
        return redirect('profile')


def CompanyRegister(request):
    if request.user.is_authenticated:
        return redirect("login")
    else:
        if request.method == "POST":
            form = CompanyRegisterForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                company_name = form.cleaned_data.get('company_name')
                messages.success(request, f"{company_name} was successfully registered")
                return redirect("login")
        else:
            form = CompanyRegisterForm()
            messages.error(request, "Form is not valid")
            context = {'form':form}
            return render(request, 'company_register.html', context)

    return render(request, 'company_register.html', {'form':form})

    
def GovernmentRegister(request):
    if request.user.is_authenticated:
        return redirect("login")
    else:
        if request.method == "POST":
            form = GovernmentRegisterForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('government_institution_name')
                messages.success(request, f"{user} was successfully registered")
                return redirect("login")
        else:
            form = GovernmentRegisterForm()
            messages.error(request, "Form is not valid")
            context = {'form':form}
            return render(request, 'government_register.html', context)

    return render(request, 'government_register.html', {'form':form})
    

def login_request(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect('/')
                else:
                    messages.error(request,"Invalid username or password")
            else:
                messages.error(request,"Invalid username or password")
    form = AuthenticationForm()
    return render(request, 'signin.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('/')

def dashboard(request):
    return render(request, 'dashboard.html')

def rec_details(request):
    context = {
        'rec_home_page': "active",
        'rec_navbar': 1,
    }
    return render(request, 'details.html', context)
