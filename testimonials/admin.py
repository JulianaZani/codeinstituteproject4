from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'approved', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ('title', 'content', 'user__username')
    