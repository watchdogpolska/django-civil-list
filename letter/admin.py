from django import forms
from django.contrib import admin

# Register your models here.
from .models import Category, Person, Letter
from ckeditor.widgets import CKEditorWidget


class CategoryAdmin(admin.ModelAdmin):
    list_display = (u'id', 'name')
    search_fields = ('name',)
admin.site.register(Category, CategoryAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = (u'id', 'name', 'email', 'category')
    list_filter = ('category',)
    search_fields = ('name',)
admin.site.register(Person, PersonAdmin)


class LetterAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        fields = ('id', 'name', 'title', 'content', 'category')
        model = Letter


class LetterAdmin(admin.ModelAdmin):
    list_display = (u'id', 'name', 'title', 'content', 'category')
    list_filter = ('category',)
    search_fields = ('name',)
    form = LetterAdminForm
admin.site.register(Letter, LetterAdmin)
