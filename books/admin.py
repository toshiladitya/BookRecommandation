from django.contrib import admin
from books.models import *

admin.site.register(Book)
admin.site.register(Recommendation)