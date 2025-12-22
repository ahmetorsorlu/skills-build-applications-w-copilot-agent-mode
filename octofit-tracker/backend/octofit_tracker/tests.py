from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(_id='test', name='Test Team')
        self.assertEqual(str(team), 'Test Team')
    def test_user_create(self):
        team = Team.objects.create(_id='t', name='T')
        user = User.objects.create(name='Test', email='test@example.com', team=team)
        self.assertEqual(str(user), 'Test')
    def test_activity_create(self):
        team = Team.objects.create(_id='t', name='T')
        user = User.objects.create(name='Test', email='test@example.com', team=team)
        activity = Activity.objects.create(user=user, type='run', distance=5)
        self.assertEqual(str(activity), 'Test - run')
    def test_leaderboard_create(self):
        team = Team.objects.create(_id='t', name='T')
        user = User.objects.create(name='Test', email='test@example.com', team=team)
        lb = Leaderboard.objects.create(user=user, score=10)
        self.assertEqual(str(lb), 'Test - 10')
    def test_workout_create(self):
        team = Team.objects.create(_id='t', name='T')
        user = User.objects.create(name='Test', email='test@example.com', team=team)
        workout = Workout.objects.create(user=user, workout='Pushups', reps=10)
        self.assertEqual(str(workout), 'Test - Pushups')
