from django.forms import ModelForm

from app.models import Provider, Product, ProductProvider


class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = "__all__"
        
    def __init__(self,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["tel"].widget.attrs.update({"class": "form-control"})
        self.fields["adress"].widget.attrs.update({"class": "form-control"})
    
        
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        
    def __init__(self,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["price"].widget.attrs.update({"class": "form-control"})


class ProductProviderForm(ModelForm):
    class Meta:
        model = ProductProvider
        fields = "__all__"
        
    def __init__(self,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["provider"].widget.attrs.update({"class": "form-select"})
        self.fields["product"].widget.attrs.update({"class": "form-select"})
        self.fields["is_active"].widget.attrs.update({"class": "form-check-input"})
        self.fields["expiration_date"].widget.attrs.update({"class": "form-control"})
        self.fields["quantity"].widget.attrs.update({"class": "form-control"})
        