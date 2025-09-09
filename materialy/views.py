from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Material
from .forms import MaterialForm

def material_list(request):
    materials = Material.objects.filter(is_active=True)
    return render(request, "materialy/material_list.html", {"materials": materials})

def material_detail(request, pk):
    mat = get_object_or_404(Material, pk=pk)
    return render(request, "materialy/material_detail.html", {"material": mat})

@login_required
def material_create(request):
    # only staff users (admins/mods) can create — можна змінити логіку під групи
    if not request.user.is_staff:
        messages.error(request, "Доступ заборонено.")
        return redirect("materials:list")
    if request.method == "POST":
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            m = form.save(commit=False)
            m.uploaded_by = request.user
            m.save()
            messages.success(request, "Матеріал створено.")
            return redirect("materials:detail", pk=m.pk)
    else:
        form = MaterialForm()
    return render(request, "materialy/material_form.html", {"form": form, "creating": True})

@login_required
def material_edit(request, pk):
    m = get_object_or_404(Material, pk=pk)
    if not (request.user.is_staff or request.user == m.uploaded_by):
        messages.error(request, "Доступ заборонено.")
        return redirect("materials:detail", pk=pk)
    if request.method == "POST":
        form = MaterialForm(request.POST, request.FILES, instance=m)
        if form.is_valid():
            form.save()
            messages.success(request, "Оновлено.")
            return redirect("materials:detail", pk=m.pk)
    else:
        form = MaterialForm(instance=m)
    return render(request, "y/material_form.html", {"form": form, "creating": False})

@login_required
def material_delete(request, pk):
    m = get_object_or_404(Material, pk=pk)
    if not (request.user.is_staff or request.user == m.uploaded_by):
        messages.error(request, "Доступ заборонено.")
        return redirect("materials:detail", pk=pk)
    if request.method == "POST":
        m.delete()
        messages.success(request, "Видалено.")
        return redirect("materials:list")
    return render(request, "materialy/material_confirm_delete.html", {"material": m})
