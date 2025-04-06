from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def calculator(request):
    if request.method == 'POST':
        income = float(request.POST.get('income', 0))
        tax = income * 0.14  # 14% vergi
        return render(request, 'calculator.html', {
            'income': income,
            'tax': tax,
            'road_km': round(tax / 50000, 2)  # 1 km yol = 50k AZN
        })
    return render(request, 'calculator.html')
