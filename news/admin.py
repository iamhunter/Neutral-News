from django.contrib import admin

from .models import Article
from .models import Opinion
from .models import Truth
from .models import Author
from .models import Title



admin.site.register(Article)
admin.site.register(Opinion)
admin.site.register(Truth)
admin.site.register(Author)
admin.site.register(Title)