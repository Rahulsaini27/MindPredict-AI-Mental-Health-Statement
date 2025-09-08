from django.db import models
from django.contrib.auth.models import User
class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to user
    statement = models.TextField()  # Store the input statement
    predicted_status = models.CharField(max_length=255)  # Store the predicted status
    created_at = models.DateTimeField(auto_now_add=True)  # Track when it was created

    def __str__(self):
        return f"Prediction for {self.user.username} - {self.predicted_status}"