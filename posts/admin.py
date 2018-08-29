"""Users admin classes"""

#Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

#Models
from django.contrib.auth.models import User
from posts.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """admin.site.register(Profile)"""

    list_display = ('pk','user', 'title', 'photo')
    list_display_links = ('pk','user')
    list_editable = ('title',)

    search_fields = (
        'user__username', 
        'title', 
    )
'''
    list_filter = ('created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )

    fieldsets = (
        ('Profile', {
            'fields': (
                ('user','picture'),
                ),
        }),
        ('Extra Info',{
            'fields':(
                ('phone_number','website'),
                ('biography'),
            )
        }),
        ('Metadata',{
            'fields': (
                ('created', 'modified'),)

        }),
    )'''


