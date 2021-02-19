from pharaoh.pyramid.models import Transaction, Payment, Agent, Product, Threshold
from datetime import datetime
from django.db.models import Sum, Prefetch, Q, Sum

def calculate_payments_for_agents():
    """Calculates payments"""

    totals = Transaction.objects.all().values("agent").annotate(total=Sum("amount"))

    for total in totals:
        payment = Payment()
        payment.agent = Agent.objects.get(pk=total["agent"])
        payment.amount = total["total"]
        payment.save()

    return totals


