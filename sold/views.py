from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Item
from .forms import ItemForm
from collections import defaultdict
from datetime import datetime
from django.db.models import Sum

def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('sold:index')
    else:
        form = ItemForm(instance=item)
    return render(request, 'sold/edit_item.html', {'form': form, 'item': item})

def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('sold:index')
    return render(request, 'sold/confirm_delete.html', {'item': item})

def index(request):
    items = Item.objects.all().order_by('-date')  # Most recent date first

    # Group items by month and calculate total price
    grouped_items = defaultdict(lambda: {'items': [], 'total_price': 0})
    for item in items:
        month_year = item.date.strftime('%B %Y')  # Group by month and year
        grouped_items[month_year]['items'].append(item)
        grouped_items[month_year]['total_price'] += item.price

    # Sort the grouped items by month
    sorted_grouped_items = sorted(grouped_items.items(), key=lambda x: datetime.strptime(x[0], '%B %Y'), reverse=True)

    # Pagination setup
    paginator = Paginator(sorted_grouped_items, 1)  # Show 1 month per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'sold/index.html', {'page_obj': page_obj})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sold:index')
    else:
        form = ItemForm()
    return render(request, 'sold/add.html', {'form': form})
