
from django.shortcuts import render, redirect
from .models import Show

def shows(request):

    context = {
        "shows": Show.objects.all(),
    }

    return render(request, 'shows.html', context)

def add_new(request):

    return render(request, 'new.html')



def submit_new(request):

    show_id = request.POST['show_id']
    Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
    return redirect('/shows/'+show_id)


def show_details(request, show_id):

    context = {
        'show_id': show_id,
        'show': Show.objects.get(id=show_id)
    }

    return render(request, 'show_details.html', context)



def edit_page(request, show_id):

    context = {
        'show_id': show_id,
        'show': Show.objects.get(id=show_id)
    }

    return render(request, 'edit.html', context)


def edit_show(request):

    show_id = request.POST['show_id']
    c = Show.objects.get(id=show_id)
    c.title = request.POST['title']
    c.network = request.POST['network']
    c.release_date = request.POST['release_date']
    c.description = request.POST['description']
    c.save()

    return redirect('/shows/'+show_id)


def delete(request, show_id):

    show_id = show_id
    d = Show.objects.get(id=show_id)
    d.delete()

    return redirect('/shows')
