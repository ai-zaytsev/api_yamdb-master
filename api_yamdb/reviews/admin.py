from django.contrib import admin

from .models import User, Review, Comment

admin.site.register(User)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "pk", "text", "author",
        "score", "pub_date", "title"
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "pk", "author", "review",
        "text", "pub_date"
    )


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
