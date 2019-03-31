from django.shortcuts import render, get_object_or_404, redirect
from .forms import RoomForm
from .models import Room



#def main(request):
 #   return render(request, 'office/main.html', {'title':'Главная страница'})

#def list_1(request):
#  return render(request, 'office/list_1.html', {'title':'Лист 1'})


def admin(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            blog_item = form.save(commit=True)
            blog_item.save()
            return redirect('/blog/' + str(blog_item.id) + '/') # < 1
    else:
        form = RoomForm()
    return render(request, 'office/main.html', {'form': form}, {'title':'admin'})

def edit_blog(request, id=None):
    item = get_object_or_404(Room, id=id)
    form = RoomForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/blog/' + str(item.id) + '/') # < 1
    return render(request, 'office/main.html', {'form': form})

def blog(request, id=id):
    blog = Room.objects.get(id=id)
    return render(request, 'barviha/list_1.html', {'blog': blog })

def ind(request):
    return render(request, 'admin/ind.html', {'title':'admintest'})

def room(request):
    return render(request, 'office/room.html', {'title':'room'})