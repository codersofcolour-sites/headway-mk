from django.contrib import admin

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Menu

@modeladmin_register
class MenuAdmin(ModelAdmin):
    model = Menu
    menu_label = "Navigation Menu"
    menu_icon = "list-ul"
    menu_order = 490
    add_to_settings_menu = False
    exclude_from_explorer = False

