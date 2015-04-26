from django.contrib import admin
from hackathon.models import UserProfile, Profile, InstagramProfile, TwitterProfile

# Register your models here.
class TwitterProfileAdmin(admin.ModelAdmin):
	list_display = ('user','twitter_user')

admin.site.register(UserProfile)
admin.site.register(Profile)
admin.site.register(InstagramProfile)
admin.site.register(TwitterProfile, TwitterProfileAdmin)

