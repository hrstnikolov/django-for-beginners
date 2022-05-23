from typing import Optional
from django.views.generic import ListView
from.models import Post


class HomePageView(ListView):
    model = Post
    template_name: str = 'home.html'
    context_object_name: Optional[str] = 'all_posts_list'

