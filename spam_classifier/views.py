from django.shortcuts import render
import joblib

model = joblib.load('spam_classifier_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def index(request):
    prediction = None
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            vect_msg = vectorizer.transform([message])
            result = model.predict(vect_msg)[0]
            prediction = "Spam" if result == 1 else "Not Spam"

    return render(request, 'index.html', {'prediction': prediction})
