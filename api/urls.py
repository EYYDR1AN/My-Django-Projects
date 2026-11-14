from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "skills/",
        views.skills,
        name="skills"
    ),

    path(
        "skills/add/",
        views.add_skill,
        name="add_skill"
    ),

    path(
        "skills/edit/<int:id>/",
        views.skill_edit,
        name="skill_edit"
    ),

    path(
        "skills/delete/<int:id>/",
        views.skill_delete,
        name="skill_delete"
    ),

    path(
        "gallery/",
        views.gallery,
        name="gallery"
    ),

    path(
        "contact/",
        views.contact,
        name="contact"
    ),

    path(
        "contact/success/",
        views.contact_success,
        name="contact_success"
    ),

]