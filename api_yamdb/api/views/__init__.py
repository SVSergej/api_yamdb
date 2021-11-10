from .review import ReviewViewSet
from .comment import CommentViewSet
from .title import TitleViewSet
from .genre import GenreViewSet
from .category import CategoryViewSet

__all__ = [
    "CategoryViewSet",
    "GenreViewSet",
    "TitleViewSet",
    "ReviewViewSet",
    "CommentViewSet",
]
