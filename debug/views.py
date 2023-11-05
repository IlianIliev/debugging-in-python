from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')


def start(request):
    response = render(request, 'start.html')
    request.session['started'] = True

    return response


def start_over(request):
    request.session.clear()

    return redirect('home')
