from django.contrib import admin
from .models import Dog, Employee, Article, ArticlePicture, Partner, Document

#admin.site.register(Dog)
admin.site.register(Employee)
# admin.site.register(Article)
admin.site.register(Partner)
admin.site.register(Document)

class ArticlePictureInline(admin.TabularInline):
    model = ArticlePicture
    fields=['image',]

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticlePictureInline,]

class DogAdmin(admin.ModelAdmin):
    list_display = ('dog_name', 'was_adopted', 'added')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Dog, DogAdmin)