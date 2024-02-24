from django.forms import ModelForm

from app.models import Category, Ingredients, Recipe


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        
    def __init__(self,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        

class IngredientsForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = "__all__"
        
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["product"].widget.attrs.update({"class": "form-select"})
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["quantity"].widget.attrs.update({"class": "form-control"})
        

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["category"].widget.attrs.update({"class": "form-select"})
        self.fields["ingredient"].widget.attrs.updaate({"class": "form-select"})
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["price"].widget.attrs.update({"class": "form-control"})
        self.fields["avaibility"].widget.update({"class": "form-check-input"})
        self.fields["image"].widget.update({"class": "form-control"})
        self.fields["description"].widget.update({"class": "form-control"})