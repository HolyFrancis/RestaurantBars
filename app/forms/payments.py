from django.forms import ModelForm

from app.models import Order, Cart, Payment


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        
    def __init__(self,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["table"].widget.attrs.update({"class": "form-select"})
        self.fields["waiter"].widget.attrs.update({"class": "form-select"})
        self.fields["to_pay"].widget.attrs.update({"class": "form-control"})
        self.fields["ordered"].widget.attrs.update({"class": "form-check-input"})
        self.fields["delivered"].widget.attrs.update({"class": "form-check-input"})
        self.fields["ready"].widget.attrs.update({"class": "form-check-input"})


class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = "__all__"
        
    def __init__(self,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["recipe"].widget.attrs.update({"class": "form-select"})
        self.fields["ready"].widget.attrs.update({"class": "form-check-input"})
        self.fields["quantity"].widget.attrs.update({"class": "form-control"})
        self.fields["total"].widget.attrs.update({"class": "form-control"})
        

class PaymenyForm(ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
    
    def __init__(self,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["order"].widget.attrs.update({"class": "form-select"})
        self.fields["total_amount"].widget.attrs.update({"class": "form-control"})
        
        