from django.contrib import admin

# from htmlwebsite.models import ContactUs
from htmlwebsite.models import Choice, ContactUs, Question, Votes


# Register your models here.

admin.site.register(Question)
admin.site.register(ContactUs)
admin.site.register(Choice)
admin.site.register(Votes)

