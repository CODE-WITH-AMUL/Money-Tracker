from django.shortcuts import render, redirect
from .models import Card, Transaction, Notification
from .forms import TransactionForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request , 'index.html')
# Create your views here.


@login_required
def dashboard(request):
    cards = Card.objects.all()
    transactions = Transaction.objects.order_by('-date')[:10]
    notifications = Notification.objects.order_by('-created_at')[:5]
    total_balance = sum(card.balance for card in cards)
    total_income = sum(t.amount for t in Transaction.objects.filter(type='income'))
    total_expense = sum(t.amount for t in Transaction.objects.filter(type='expense'))

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            # Update card balance
            if transaction.type == 'income':
                transaction.card.balance += transaction.amount
            else:
                transaction.card.balance -= transaction.amount
            transaction.card.save()
            # Smart notification if low balance
            if transaction.card.balance < 100:  # You can adjust this threshold
                Notification.objects.create(
                    message=f"Warning: Your card '{transaction.card.name}' is low on balance!",
                )
            return redirect('dashboard')
    else:
        form = TransactionForm()

    context = {
        'cards': cards,
        'transactions': transactions,
        'notifications': notifications,
        'total_balance': total_balance,
        'total_income': total_income,
        'total_expense': total_expense,
        'form': form,
    }
    return render(request, 'dashboard.html', context)
