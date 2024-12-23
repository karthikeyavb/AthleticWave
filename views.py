# main/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    return render(request, 'main/home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Check the length of the username to determine the role
        if len(username) == 4:
            role = 'Admin'
        elif len(username) == 5:
            role = 'Coach'
        elif len(username) == 6:
            role = 'Viewer'
        else:
            messages.error(request, 'Invalid username length. Must be 4, 5, or 6 digits.')
            return render(request, 'main/login.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if role == 'Admin':
                return render(request, 'main/admin_dashboard.html')
            elif role == 'Coach':
                return render(request, 'main/coach_dashboard.html')
            elif role == 'Viewer':
                return render(request, 'main/viewer_dashboard.html')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'main/login.html')

# main/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        # Check the length of the username to determine the role
        if len(username) == 4:
            role = 'Admin'
        elif len(username) == 5:
            role = 'Coach'
        elif len(username) == 6:
            role = 'Viewer'
        else:
            messages.error(request, 'Invalid username length. Must be 4, 5, or 6 digits.')
            return render(request, 'main/register.html')

        if password == password_confirm:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Assign user to the appropriate group based on role
                group = Group.objects.get(name=role)
                user.groups.add(group)

                messages.success(request, 'Registration successful! You can now log in.')

                # Redirect to the respective dashboard based on the role
                if role == 'Admin':
                    return render('admin_dashboard')
                elif role == 'Coach':
                    return redirect('coach_dashboard')
                elif role == 'Viewer':
                    return redirect('viewer_dashboard')
            except Exception as e:
                messages.error(request, 'Error creating account: ' + str(e))
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'main/register.html')

def admin_dashboard(request):
    return render(request, 'main/admin_dashboard.html')

def coach_dashboard(request):
    return render(request, 'main/coach_dashboard.html')

def viewer_dashboard(request):
    return render(request, 'main/viewer_dashboard.html')

def know_more(request):
    return render(request, 'main/know_more.html')

# sports_event_management/main/views.py
from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm

def add_event(request):
       if request.method == 'POST':
           form = EventForm(request.POST)
           if form.is_valid():
               form.save()  # Save the event to the database
               return redirect('event_list')  # Redirect to the event list page after saving
       else:
           form = EventForm()  # Create a new form instance for GET requests

       # Fetch existing events to display in the list
       events = Event.objects.all()
       return render(request, 'main/add_event.html', {'form': form, 'events': events})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'main/event_list.html', {'events': events})

def chatbot_view(request):
    return render(request, 'main/chatbot.html')