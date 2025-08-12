from django.shortcuts import render, get_object_or_404, redirect
from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def advertisement_list(request):
    advertisements = Advertisement.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'advertisement/ad_list.html', {'advertisements': advertisements})


@login_required
def advertisement_create(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.save()
            return redirect('advertisement:ad_list')
    else:
        form = AdvertisementForm()
    return render(request, 'advertisement/ad_form.html', {'form': form})

@login_required
def advertisement_edit(request, pk):
    ad = get_object_or_404(Advertisement, pk=pk)
    if request.user != ad.author and not request.user.is_staff:
        return redirect('advertisement:ad_list')
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('advertisement:ad_list')
    else:
        form = AdvertisementForm(instance=ad)
    return render(request, 'advertisement/ad_form.html', {'form': form})

@staff_member_required
def advertisement_delete(request, pk):
    ad = get_object_or_404(Advertisement, pk=pk)
    ad.delete()
    return redirect('advertisement:ad_list')
