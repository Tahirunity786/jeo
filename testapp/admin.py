from django.contrib import admin
from .models import Video, DownloadItem, Video_Ea, Faq, Payment, HomeVideo
from .forms import VideoForm, HomeVideoForm

class VideoAdmin(admin.ModelAdmin):
    form = VideoForm
    list_display = ('title', 'description')  # Customize this list as needed

admin.site.register(Video, VideoAdmin)

class DownloadItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'file')  # Customize this list as needed

admin.site.register(DownloadItem, DownloadItemAdmin)

class VideoEaAdmin(admin.ModelAdmin):
    form = VideoForm
    list_display = ('title', 'youtube_url')  # Customize this list as needed

admin.site.register(Video_Ea, VideoEaAdmin)
@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')  # Customize this list as needed



class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'transaction_id', 'amount', 'payment_date', 'subscription_expiry')
    list_filter = ['payment_date']
    search_fields = ['user__username', 'transaction_id']
    actions = ['activate_accounts', 'deactivate_accounts']

    def activate_accounts(self, request, queryset):
        for payment in queryset:
            if not payment.user.is_active:
                payment.user.is_active = True
                payment.user.save()

    activate_accounts.short_description = "Activate selected user accounts"

    def deactivate_accounts(self, request, queryset):
        for payment in queryset:
            if payment.user.is_active:
                payment.user.is_active = False
                payment.user.save()

    deactivate_accounts.short_description = "Deactivate selected user accounts"

admin.site.register(Payment, PaymentAdmin)
class HomeVideoAdmin(admin.ModelAdmin):
    form = HomeVideoForm
    list_display = ('title', 'description')  # Customize this list as needed

admin.site.register(HomeVideo, HomeVideoAdmin)
