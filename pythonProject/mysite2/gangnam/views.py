from django.shortcuts import render
# Create your views here.
import pandas as pd


def main_view(request):
    df = pd.read_csv(r'C:\Users\Playdata\Downloads\gangnam.csv')
    labels = df['STDR_DE_ID'].values.tolist()
    data = df['TOT_LVPOP_CO'].values.tolist()
    return render(request, 'line-chart.html', {
        'labels': labels,
        'data': data,

    })
