from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import *
from admin_view_permission.admin import AdminViewPermissionAdminSite


class MyAdminSite(AdminViewPermissionAdminSite):
    def get_urls(self):
        urls = super(MyAdminSite, self).get_urls()
        return urls


admin_site = MyAdminSite()
admin_site.register(Group, GroupAdmin)
admin.site.unregister(User)
admin_site.register(User)
