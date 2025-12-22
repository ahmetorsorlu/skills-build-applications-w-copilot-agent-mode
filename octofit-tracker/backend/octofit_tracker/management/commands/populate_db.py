from django.core.management.base import BaseCommand
from django.conf import settings

from pymongo import MongoClient, ASCENDING

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Populating octofit_db with test data...'))
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Temizle
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Takımlar
        marvel_team = {'_id': 'marvel', 'name': 'Team Marvel'}
        dc_team = {'_id': 'dc', 'name': 'Team DC'}
        db.teams.insert_many([marvel_team, dc_team])

        # Kullanıcılar
        users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'marvel'},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': 'marvel'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'dc'},
            {'name': 'Superman', 'email': 'superman@dc.com', 'team': 'dc'},
        ]
        db.users.insert_many(users)
        db.users.create_index([('email', ASCENDING)], unique=True)

        # Aktiviteler
        activities = [
            {'user': 'ironman@marvel.com', 'type': 'run', 'distance': 5},
            {'user': 'cap@marvel.com', 'type': 'cycle', 'distance': 20},
            {'user': 'batman@dc.com', 'type': 'swim', 'distance': 2},
            {'user': 'superman@dc.com', 'type': 'fly', 'distance': 100},
        ]
        db.activities.insert_many(activities)

        # Liderlik tablosu
        leaderboard = [
            {'user': 'ironman@marvel.com', 'score': 50},
            {'user': 'cap@marvel.com', 'score': 40},
            {'user': 'batman@dc.com', 'score': 60},
            {'user': 'superman@dc.com', 'score': 100},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Antrenmanlar
        workouts = [
            {'user': 'ironman@marvel.com', 'workout': 'Pushups', 'reps': 100},
            {'user': 'cap@marvel.com', 'workout': 'Situps', 'reps': 80},
            {'user': 'batman@dc.com', 'workout': 'Pullups', 'reps': 50},
            {'user': 'superman@dc.com', 'workout': 'Squats', 'reps': 200},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db test verileri başarıyla yüklendi!'))
