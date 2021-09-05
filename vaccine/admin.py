from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

# リソース
class BookResource(resources.ModelResource):
    class Meta:
        model = Hospital

# 管理
class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource

# 登録
admin.site.register(Hospital, BookAdmin)