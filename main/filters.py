import django_filters
from .models import ImageGallery


class GalleryFilter(django_filters.FilterSet):
    class Meta:
        model = ImageGallery
        fields = {'image_name': ['icontains']
        }
