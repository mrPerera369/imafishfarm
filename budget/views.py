from django.shortcuts import render
from decimal import Decimal
from bought.models import Item as BoughtItem
from sold.models import Item as SoldItem
from maintenance.models import Item as MaintenanceItem
from collections import defaultdict

def index(request):
    bought_items = BoughtItem.objects.all()
    sold_items = SoldItem.objects.all()
    maintenance_items = MaintenanceItem.objects.all()
    
    # Group items by month
    monthly_totals = defaultdict(Decimal)
    sold_totals = defaultdict(Decimal)
    maintenance_totals = defaultdict(Decimal)
    
    for item in bought_items:
        month_year = item.date.strftime('%B %Y')
        monthly_totals[month_year] += item.price  # item.price should be a Decimal
    
    for item in sold_items:
        month_year = item.date.strftime('%B %Y')
        sold_totals[month_year] += item.price  # item.price should be a Decimal
    
    for item in maintenance_items:
        month_year = item.date.strftime('%B %Y')
        maintenance_totals[month_year] += item.price  # item.price should be a Decimal
    
    final_totals = {}
    for month_year in monthly_totals:
        final_totals[month_year] = sold_totals[month_year] - (monthly_totals[month_year] + maintenance_totals[month_year])
    
    total_price = sum(final_totals.values())
    
    context = {
        'final_totals': dict(final_totals),  # Convert defaultdict to dict
        'total_price': total_price
    }
    
    return render(request, 'budget/index.html', context)
