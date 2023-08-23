from django.urls import path, include# other imports
import blog.views

urlpatterns = [
    # other patterns
    path("", blog.views.index)
]
