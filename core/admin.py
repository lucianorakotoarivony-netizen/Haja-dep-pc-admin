from django.contrib import admin
from django.http.request import HttpRequest
from .models import Home, Contact, About, SocialNetwork, User, Service, Review, Software, Hardware

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    def has_add_permission(self, request: HttpRequest, obj = None) -> bool:
        return not Home.objects.exists()
    def has_delete_permission(self, request: HttpRequest, obj = None) -> bool:
        return False
    fieldsets =(
        ('Informations générales', {
            'fields': ('site_name', 'owner_name')
        }),
        ('Apparence', {
            'fields': ('primary_color',),
            'classes': ('collapse',),  # Plié par défaut
        }),
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request: HttpRequest, obj=None) -> bool:
        return not Contact.objects.exists()
    
    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
    
    fieldsets = (
        ('Coordonnées', {
            'fields': ('phone', 'email')
        }),
    )

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request: HttpRequest, obj = None) -> bool:
        return not About.objects.exists()

    def has_delete_permission(self, request: HttpRequest, obj = None) -> bool:
        return False
    
    fieldsets=((None,{
        "fields": ("title","content","image","image_url")
    }),)

@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ["name", "link", "icon", "is_active", "order"]
    list_editable = ["order", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["name"]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields =['username', 'email', 'password']
    list_display =['username', 'email', 'password', 'is_active']
    list_editable =["is_active"]
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=["name","price","order","is_active"]
    list_editable=["order", "is_active"]
    list_filter=["is_active"]
    search_fields=["name","description"]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'rating', 'core_status', 'created_at', 'is_active']
    list_filter = ['core_status', 'rating', 'is_active', 'created_at']
    search_fields = ['content', 'user__username']
    readonly_fields = ['content', 'rating', 'user', 'created_at']
    fields = ['user', 'content', 'rating', 'core_status', 'is_active', 'created_at']
    
    # Pas de création manuelle (NestJS s'en charge)
    def has_add_permission(self, request):
        return False
@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'price', 'order', 'version', 'is_active']
    list_editable=["order", "is_active"]
    list_filter = ['is_active', 'version']
    search_fields = ['name']

@admin.register(Hardware)
class AdminHardware(admin.ModelAdmin):
    list_display = [ 'name', 'price', 'order', 'warranty', 'is_active']
    list_editable=["order", "is_active"]
    list_filter = ['is_active', 'warranty']
    search_fields = ['name']