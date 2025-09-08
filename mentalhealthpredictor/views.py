import joblib
import numpy as np
from scipy.sparse import hstack
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.http import JsonResponse
from django.contrib.auth import logout
# Load the model and vectorizer
model_path = r"model.pkl"
tfidf_vectorizer_path = r"vectorizer.pkl"
model = joblib.load(model_path)
tfidf_vectorizer = joblib.load(tfidf_vectorizer_path)

from .models import Prediction

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('predict_view')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# # Load the model and vectorizer
# with open("model.pkl", "rb") as model_file:
#     model = pickle.load(model_file)

# with open("vectorizer.pkl", "rb") as vectorizer_file:
#     vectorizer = pickle.load(vectorizer_file)

# @login_required
# def predict(request):
#     if request.method == 'POST':
#         # Get the statement from the POST request
#         statement = request.POST.get('Statement')  # Ensure key matches form field name

#         if statement:
#             # Call the function to predict the mental health status
#             predicted_status = predict_mental_health(model, tfidf_vectorizer, statement)
            
#             # Return the predicted status with the correct key in the response
#             return JsonResponse({'predicted_status': predicted_status})  # Corrected key here
#         else:
#             return JsonResponse({'error': 'Statement is required'}, status=400)
    
#     return render(request, 'predict.html')  # Render the prediction form template

@login_required
def predict(request):
    if request.method == 'POST':
        # Get the statement from the POST request
        statement = request.POST.get('Statement')  # Ensure key matches form field name

        if statement:
            # Call the function to predict the mental health status
            predicted_status = predict_mental_health(model, tfidf_vectorizer, statement)
            
            # Save the data into the database
            prediction = Prediction(
                user=request.user,  # Save the user making the prediction
                statement=statement,  # Save the input statement
                predicted_status=predicted_status  # Save the predicted output
            )
            prediction.save()  # Save the prediction to the database
            
            # Return the predicted status
            return JsonResponse({'predicted_status': predicted_status})
        else:
            return JsonResponse({'error': 'Statement is required'}, status=400)
    
    return render(request, 'predict.html')  # Render the prediction form template

def predict_mental_health(model, vectorizer, inputs):
    """
    Predicts the mental health status of a given statement.
    
    Parameters:
    model (RandomForestClassifier): The trained RandomForest model.
    vectorizer (TfidfVectorizer): The trained TF-IDF vectorizer.
    inputs (str): The statement to classify.
    
    Returns:
    str: The predicted mental health status.
    """
    # Convert the input statement into a TF-IDF feature vector
    inputs_vectorized = vectorizer.transform([inputs]).toarray()
    
    # Predict the mental health status using the model
    predicted_status = model.predict(inputs_vectorized)[0]
    
    return predicted_status


def prediction_history(request):
    # Get all predictions made by the current user
    predictions = Prediction.objects.filter(user=request.user).order_by('-created_at')
    
    return render(request, 'prediction_history.html', {'predictions': predictions})    

def user_logout(request):
    logout(request)
    return redirect('home')
