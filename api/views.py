from django.shortcuts import render, redirect, get_object_or_404

from .forms import ContactForm, SkillForm
from .models import Skill


def home(request):
    return render(request, "home.html")


def skills(request):
    skills = Skill.objects.all().order_by("skill_name")

    return render(request, "skills.html", {
        "skills": skills
    })


def skill_edit(request, id):
    skill = get_object_or_404(Skill, id=id)

    if request.method == "POST":
        skill.skill_name = request.POST.get("skill_name")
        skill.category = request.POST.get("category")
        skill.description = request.POST.get("description")

        skill.save()

        return redirect("skills")

    return render(request, "edit_skill.html", {
        "skill": skill
    })


def skill_delete(request, id):
    skill = get_object_or_404(Skill, id=id)

    if request.method == "POST":
        skill.delete()

        return redirect("skills")

    return render(request, "delete_skill.html", {
        "skill": skill
    })


def add_skill(request):
    if request.method == "POST":
        form = SkillForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("skills")

    else:
        form = SkillForm()

    return render(request, "add_skill.html", {
        "form": form
    })


def gallery(request):
    return render(request, "gallery.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("contact_success")

    else:
        form = ContactForm()

    return render(request, "contact.html", {
        "form": form
    })


def contact_success(request):
    return render(request, "contact_success.html")