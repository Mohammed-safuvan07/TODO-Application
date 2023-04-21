from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .form import Form
from todoapp.models import todo
from django.views.generic import ListView, DeleteView
from django.views.generic import DetailView,UpdateView


# Create your views here.
def demo(request):
    values = todo.objects.all()
    if request.method == 'POST':
        task = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        table = todo(task=task, priority=priority, date=date)
        table.save()
    return render(request, 'index.html', {'values': values})


def delete(request, id):
    if request.method == 'POST':
        value = todo.objects.get(id=id)
        value.delete()
        return redirect('/')

    return render(request, 'delete.html')


def update(request, id):
    objs = todo.objects.get(id=id)
    form = Form(request.POST or None, instance=objs)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'objs': objs, 'form': form})


class listview(ListView):
    model = todo
    template_name = 'index.html'
    context_object_name = 'values'


class detailview(DetailView):
    model = todo
    template_name = 'details.html'
    context_object_name = 'values'


class updateview(UpdateView):
    model = todo
    template_name = 'update1.html'
    context_object_name = 'values'
    fields = ('task','priority','date')
    success_url = reverse_lazy('cvlist')

class deleteview(DeleteView):
    model = todo
    template_name = 'delete.html'
    success_url = reverse_lazy('cvlist')