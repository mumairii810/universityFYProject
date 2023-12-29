from django.contrib import admin
from .models import SendMessage,ContactForm
# admin.site.register(SendMessage)
# admin.site.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('password', 'email')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',"subject","message")

admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(SendMessage, MessageAdmin)