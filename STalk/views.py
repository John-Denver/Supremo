from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from . forms import *

from django.shortcuts import render, get_object_or_404, redirect
from . models import *

# Create your views here.


"""def iindex(request):

    events = Events.objects.all()

    ethnic = Ethnic.objects.all()

    deejay = Deejay.objects.all()

    hype = Hype.objects.all()

    planner = Planner.objects.all()

    speakers = Speakers.objects.all()

    mc = Mc.objects.all()

    context = {
    'deejay': deejay,

    'planner': planner,

    'hype': hype,

    'mc': mc,


    }

    return render(request, 'STalk/index.html', context) """


def index(request):
    deejays = Deejay.objects.all()

    context = {
        'deejays': deejays,

    }
    return render(request, 'STalk/index.html', context)


def index2(request):
    deejays = Deejay.objects.all()

    context = {
        'deejays': deejays,

    }
    return render(request, 'STalk/index2.html', context)


def logins(request):
    return render(request, 'STalk/logins.html')


def registrations(request):
    return render(request, 'STalk/registrations.html')


def detail(request, deejay_id):
    deejay = get_object_or_404(Deejay, pk=deejay_id)
    return render(request, 'STalk/detail.html', {'deejay': deejay})


@login_required(login_url='STalk:login_deejay')
def deejay(request):
    form = DjForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        deejay = form.save(commit=False)
        """deejay.picture = request.POST['picture']
        deejay.age = request.POST['age']
        deejay.contact = request.POST['contact']
        deejay.email = request.POST['email']"""
        deejay.user = request.user
        deejay.save()
        return render(request, 'STalk/detail.html', {'deejay': deejay})
    form = DjForm()
    return render(request, 'STalk/deejay.html', {'form': form})


def mc_index(request):
    mc = Mc.objects.all()

    context = {
        'mc': mc,
    }
    return render(request, 'STalk/mcs.html', context)


def detailmc(request, m_id):
    mc = get_object_or_404(Mc, pk=m_id)
    return render(request, 'STalk/detailmc.html', {'mc': mc})


@login_required(login_url='STalk:login_mc')
def mc(request):
    form = McForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        mcs = form.save(commit=False)
        mcs.picture = request.FILES['picture']
        mcs.age = request.POST['age']
        mcs.Mc_name = request.POST['Mc_name']
        #mc.ethnic = request.POST['ethnic']
        mcs.user = request.user
        mcs.save()
        mc = Mc.objects.all()
        return render(request, 'STalk/mcs.html', {'mc': mc})
    form = McForm()
    return render(request, 'STalk/mc_sign.html', {'form': form})


def event_index(request):
    eve = Planner.objects.all()

    context = {
        'eve': eve,
    }
    return render(request, 'STalk/planner.html', context)


def detailevent(request, plan_id):
    event = get_object_or_404(Planner, pk=plan_id)
    return render(request, 'STalk/detailevent.html', {'event': event})


@login_required(login_url='STalk:login_event')
def event(request):
    form = PlanForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        event = form.save(commit=False)
        event.picture = request.FILES['picture']
        event.Age = request.POST['Age']
        event.name = request.POST['name']
        event.user = request.user
        event.save()
        eve = Planner.objects.all()
        return render(request, 'STalk/planner.html', {'eve': eve})
    form = PlanForm()
    return render(request, 'STalk/plan_sign.html', {'form': form})


def delete_event(request, event_id):
    event = Planner.objects.get(pk=event_id)
    event.user = request.user
    event.delete()
    event = Speakers.objects.all()
    return render(request, 'STalk/planner.html', {'event': event})


def speaker_index(request):
    sys = Speakers.objects.all()

    context = {
        'sys': sys,
    }
    return render(request, 'STalk/speakers.html', context)


def detail2(request, speaker_id):
    speak = get_object_or_404(Speakers, pk=speaker_id)
    return render(request, 'STalk/detail2.html', {'speak': speak})


@login_required(login_url='STalk:login_speaker')
def speaker(request):
    form = SpeakerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        speak = form.save(commit=False)
        speak.picture = request.FILES['picture']
        speak.owner = request.POST['owner']
        speak.desc = request.POST['desc']
        speak.user = request.user
        speak.save()
        sys = Speakers.objects.all()
        return render(request, 'STalk/speakers.html', {'sys': sys})
    form = SpeakerForm()
    return render(request, 'STalk/speak_sign.html', {'form': form})


def delete_speaker(request, speaker_id):
    speaker = Speakers.objects.get(pk=speaker_id)
    speaker.user = request.user
    speaker.delete()
    speaker = Speakers.objects.all()
    return render(request, 'STalk/speakers.html', {'speaker': speaker})


def hype_index(request):
    hype = Hype.objects.all()

    context = {
        'hype': hype,
    }
    return render(request, 'STalk/hype_person.html', context)


def detailhype(request, hype_id):
    hype = get_object_or_404(Hype, pk=hype_id)
    return render(request, 'STalk/detailhype.html', {'hype': hype})


@login_required(login_url='STalk:login_hyper')
def hype(request):
    form = HypeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        hyper = form.save(commit=False)
        hyper.picture = request.FILES['picture']
        hyper.name = request.POST['name']
        hyper.user = request.user
        hyper.save()
        hype = Hype.objects.all()
        return render(request, 'STalk/hype_person.html', {'hype': hype})
    form = HypeForm()
    return render(request, 'STalk/hype_sign.html', {'form': form})


def delete_hype(request, hype_id):
    hyper = Hype.objects.get(pk=hype_id)
    hyper.user = request.user
    hyper.delete()
    hyper = Hype.objects.all()
    return render(request, 'STalk/hype_person.html', {'hyper': hyper})


@login_required(login_url='STalk:login_deejay')
def delete_deejay(request, deejay_id):
    deejay = Deejay.objects.get(pk=deejay_id)
    deejay.user = request.user
    deejay.delete()
    deejay = Deejay.objects.all()
    return render(request, 'STalk/index.html', {'deejay': deejay})


def delete_mc(request, mc_id):
    mc = Mc.objects.get(pk=mc_id)
    mc.user = request.user
    mc.delete()
    mc = Mc.objects.all()
    return render(request, 'STalk/mcs.html', {'mc': mc})


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('STalk:login_deejay')
    return render(request, 'STalk/dj_register.html', {'form': form})


def login_deejay(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('STalk:index2')

    return render(request, 'STalk/dj_login.html')


def logout_deejay(request):
    logout(request)
    return redirect('STalk:login_deejay')


def mc_register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('STalk:login_mc')
    return render(request, 'STalk/mc_register.html', {'form': form})


def login_mc(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('STalk:mc_index')
    return render(request, 'STalk/mc_login.html')


def logout_mc(request):
    logout(request)
    return redirect('STalk:login_mc')


def speaker_register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('STalk:login_speaker')
    return render(request, 'STalk/speaker_register.html', {'form': form})


def login_speaker(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('STalk:speaker_index')
    return render(request, 'STalk/speaker_login.html')


def logout_speaker(request):
    logout(request)
    return redirect('STalk:login_speaker')


def event_register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('STalk:login_event')
    return render(request, 'STalk/event_register.html', {'form': form})


def login_event(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('STalk:event_index')
    return render(request, 'STalk/event_login.html')


def logout_event(request):
    logout(request)
    return redirect('STalk:login_event')


def hyper_register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('STalk:login_hyper')
    return render(request, 'STalk/hyper_register.html', {'form': form})


def login_hyper(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('STalk:hype_index')
    return render(request, 'STalk/hyper_login.html')


def logout_hyper(request):
    logout(request)
    return redirect('STalk:login_hyper')



