# Mental Health Prediction Application

This is a web application that uses machine learning to predict the mental health status based on user input. It helps users analyze statements related to their mental well-being and receive predictions about their mental health status.

## Features

- **Prediction**: Users can input a statement, and the app will predict their mental health status (e.g., positive, negative, or neutral).
- **Prediction History**: The application keeps a record of all previous predictions, including the input statement, the predicted status, and the time of creation.
- **User Authentication**: Secure login and registration features for users.

## Technologies Used

- **Django**: The backend framework for building web applications.
- **Scikit-learn**: Used for building and training the machine learning model for predicting mental health status.
- **SQLite**: Database for storing user data and prediction history.
- **Bootstrap**: Front-end framework for creating responsive and attractive user interfaces.
- **Python 3.x**: The programming language used for developing the application.

1. Install required dependencies
cd mentalhealthpredictor
pip install -r requirements.txt

2. Set up the database

python manage.py migrate

3. Create a superuser
python manage.py createsuperuser

4. Start the development server
python manage.py runserver

Now, open The  browser and visit http://127.0.0.1:8000/ to access the application.


