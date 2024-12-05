from django.shortcuts import render, get_object_or_404, redirect
from .models import Groups


def home(request):
    return render(request, 'index.html')


def group_name(request):
    groups = Groups.objects.all()
    ctx = {'groups': groups}
    return render(request, 'groups/groups-list.html', ctx)


def group_type(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        group_type = request.POST.get('group_type')
        if group_name and group_type:
            Groups.objects.create(
                group_name=group_name,
                group_type=group_type
            )
            return redirect('groups:group_list')
    return render(request, 'groups/groups-form.html')


def group_detail(request, pk):
    groups = get_object_or_404(Groups, pk=pk)
    ctx = {'groups': groups}
    return render(request, 'groups/groups-detail.html', ctx)


def group_delete(request, pk):
    groups = get_object_or_404(Groups, pk=pk)
    groups.delete()
    return redirect('groups:group_list')
