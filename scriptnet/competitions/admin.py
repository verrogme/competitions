from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Competition, Individual, Affiliation, Submission, Track, Subtrack
from .models import Benchmark, SubmissionStatus

class IndividualInline(admin.StackedInline):
    model = Individual
    can_delete = False
    filter_horizontal = ('affiliations', )    

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (IndividualInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Individual)
admin.site.register(Affiliation)
admin.site.register(Competition)
admin.site.register(Track)
admin.site.register(Subtrack)
admin.site.register(Submission)
admin.site.register(Benchmark)
admin.site.register(SubmissionStatus)
