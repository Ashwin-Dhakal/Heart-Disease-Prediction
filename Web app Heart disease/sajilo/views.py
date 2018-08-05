from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

def index(request):
    return render(request,'sajilo/index.html')

def searchlist(request):
    age= request.GET.get('q1')
    sex= request.GET.get('q2')
    if sex == 'M':
        sex = 1
    else:
        sex = 0
    chest_pain= request.GET.get('q3')
    blood_pressure= request.GET.get('q4')
    serum_cholestoral= request.GET.get('q5')
    fasting_blood_sugar= request.GET.get('q6')
    electrocardiographic= request.GET.get('q7')
    max_heart_rate= request.GET.get('q8')
    induced_angina= request.GET.get('q9')
    ST_depression= request.GET.get('q10')
    slope= request.GET.get('q11')
    vessels= request.GET.get('q12')
    thal= request.GET.get('q13')


    # Importing the libraries
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    # loading ANN mode

    from keras.models import load_model
    model = load_model('ANNmodel.h5')

    # creating a array
    data = np.array(
        [[age, sex, chest_pain, blood_pressure, serum_cholestoral, fasting_blood_sugar, electrocardiographic,
          max_heart_rate, induced_angina, ST_depression, slope, vessels, thal]])

    diagonis = np.around(model.predict(data), 0)

    context = {
        "diagonis" : diagonis,

    }
    return render(request, 'sajilo/searchlist.html', context)





