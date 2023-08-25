from django.contrib import admin
from . models import (
    UserProfile,
    ContactProfile,
    Skill,
    Extracurricular,
    Media
)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

@admin.register(ContactProfile)
class ContactProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'name')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'score')

@admin.register(Extracurricular)
class ExtracurricularAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')