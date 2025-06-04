from django import forms
from .models import Transaction, Card

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['card', 'amount', 'type', 'description']
        widgets = {
            'type': forms.RadioSelect(choices=Transaction.TRANSACTION_TYPES),
        } 