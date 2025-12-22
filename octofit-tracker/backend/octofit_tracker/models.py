from djongo import models

class Team(models.Model):
    _id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=50)
    distance = models.FloatField()
    def __str__(self):
        return f"{self.user.name} - {self.type}"

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard')
    score = models.IntegerField()
    def __str__(self):
        return f"{self.user.name} - {self.score}"

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    workout = models.CharField(max_length=100)
    reps = models.IntegerField()
    def __str__(self):
        return f"{self.user.name} - {self.workout}"