from django.contrib import admin
from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.


class UserProfileInline(admin.StackedInline):  # StackedInline/TabularInline
    model = UserProfileModel
    filter_horizontal = ['hobby']


class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'fullname', 'email',)
    list_display_links = ('username',)
    list_filter = ('username', )
    search_fields = ('username', 'email',)
    readonly_fields = ('join_date',)  # 뒤에 , 있어야 튜플로 지정됨
    # fieldset = (
    #     ("info", {'fields': ('username', 'password', 'email', 'fullname', 'join_date',)}),
    #     ("permissions", {'fields': ('is_admin', 'is_active',)}),)

    fieldsets = (
        ("info", {'fields': ('username', 'password',
         'email', 'fullname', 'join_date',)}),
        ("permissions", {'fields': ('is_admin', 'is_active',)}),)
    
    inlines = (UserProfileInline,)

    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','fullname', 'password', 'password2')
        }),

    )

    filter_horizontal = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('username', 'join_date', )
        else:
            return ('join_date',)

    


admin.site.register(UserModel, UserAdmin)  # 유저모델에 위에 정의내린 UserAdmin 쓰겠다
admin.site.register(UserProfileModel)
admin.site.register(HobbyModel)
