from django.contrib import admin

from myapp.models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = [ 'id', "name", "dob", "gender",  "gender" , "locality",  "city",  "pin",  "state", "mobile", "email",
    "job_city", "profile_image", "my_file"
    ]
