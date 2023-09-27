from django.shortcuts import render, HttpResponse
import pandas as pd
import json

# Create your views here.
def Table(request):
    df = pd.read_csv("static/greenhouse_gas_emissions.csv")
  
    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
  
    return render(request, 'table.html', context)       