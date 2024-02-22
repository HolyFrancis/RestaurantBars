from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList

from app.models import Table, Place


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = "__all__"
        
    def __init__(self,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["short_description"].widget.attrs.update({"class": "form-control"})
        
class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = "__all__"
        
    def __init__(self,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["capacity"].widget.attrs.update({"class": "form-control"})
        self.fields["place"].widget.attrs.update({"class": "form-select"})
        self.fields["image"].widget.attrs.update({"class": "form-control" })