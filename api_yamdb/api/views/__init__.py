from .review import ReviewViewSet
from .comment import CommentViewSet
from .title import TitleViewSet
from .genre import GenreViewSet
from .category import CategoryViewSet
from .registation import RegistrationView
from .customjwttoken import CustomJWTTokenView

__all__ = [
    "CategoryViewSet",
    "GenreViewSet",
    "TitleViewSet",
    "ReviewViewSet",
    "CommentViewSet",
    "RegistrationView",
    "CustomJWTTokenView",
]
