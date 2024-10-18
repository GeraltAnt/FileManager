from django.shortcuts import render, get_object_or_404
from .models import Site, Item, BusinessProcess, ProcessFile
from .forms import ProcessFileForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def site_list(request):
    sites = Site.objects.all()
    return render(request, 'cms_app/site_list.html', {'sites': sites})

def item_list(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    items = Item.objects.filter(site=site)
    return render(request, 'cms_app/item_list.html', {'site': site, 'items': items})

def process_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    processes = BusinessProcess.objects.all()
    if request.method == 'POST':
        form = ProcessFileForm(request.POST, request.FILES)
        if form.is_valid():
            process_file = form.save(commit=False)
            process_file.item = item
            process_file.save()
            return HttpResponseRedirect(reverse('process_detail', args=[item_id]))
    else:
        form = ProcessFileForm()
    process_files = ProcessFile.objects.filter(item=item)
    return render(request, 'cms_app/process_detail.html', {
        'item': item,
        'processes': processes,
        'process_files': process_files,
        'form': form
    })
