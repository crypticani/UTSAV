from django.db import models
from main.models import *
from registration.models import *

# Create your models here.
class TeamRecordModel(models.Model):
    record_id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(TeamEventList, on_delete=models.CASCADE)
    score_team1 = models.CharField(blank=True, max_length=30)
    score_team2 = models.CharField(blank=True, max_length=30)
    winner = models.ForeignKey(TeamRegistrationmodel, related_name='team3', on_delete=models.CASCADE, limit_choices_to={'year': datetime.date.today().year})

    class Meta:
        verbose_name_plural = "Team Records"

    def __str__(self):
        return str(self.winner)


class AthleticsModel(models.Model):
    record_id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(IndividualEventsList, on_delete=models.CASCADE)
    date = models.DateField(blank=True)
    # categories = (('Male', 'Male'), ('Female', 'Female'))
    # category = models.CharField(blank=True, max_length=10, choices=categories)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    event_name = models.CharField(blank=True, max_length=30)
    player_name = models.CharField(blank=True, max_length=30)
    idnum = models.IntegerField(blank=True)
    result = models.CharField(blank=True, max_length=10)

    class Meta:
        verbose_name_plural = "Athletics Records"

    def __str__(self):
        return self.event_name


class BadmintonModel(models.Model):
    record_id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(IndividualEventsList, on_delete=models.CASCADE)
    date = models.DateField(blank=True)
    # categories = (('Male', 'Male'), ('Female', 'Female'))
    # category = models.CharField(blank=True, max_length=10, choices=categories)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    team1_player1 = models.CharField(blank=True, max_length=30)
    team1_player2 = models.CharField(blank=True, max_length=30)
    team2_player1 = models.CharField(blank=True, max_length=30)
    team2_player2 = models.CharField(blank=True, max_length=30)
    score = models.CharField(blank=True, max_length=10)
    winner = models.CharField(blank=True, max_length=30)

    class Meta:
        verbose_name_plural = "Badminton Records"

    def __str__(self):
        return self.winner


class CarromModel(models.Model):
    record_id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(IndividualEventsList, on_delete=models.CASCADE)
    date = models.DateField(blank=True)
    # categories = (('Male', 'Male'), ('Female', 'Female'))
    # category = models.CharField(blank=True, max_length=10, choices=categories)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    team1_player1 = models.CharField(blank=True, max_length=30)
    team1_player2 = models.CharField(blank=True, max_length=30)
    team2_player1 = models.CharField(blank=True, max_length=30)
    team2_player2 = models.CharField(blank=True, max_length=30)
    winner = models.CharField(blank=True, max_length=30)

    class Meta:
        verbose_name_plural = "Carrom Records"

    def __str__(self):
        return self.winner


class ChessModel(models.Model):
    record_id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(IndividualEventsList, on_delete=models.CASCADE)
    date = models.DateField(blank=True)
    # categories = (('Male', 'Male'), ('Female', 'Female'))
    # category = models.CharField(blank=True, max_length=10, choices=categories)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    player1 = models.CharField(blank=True, max_length=30)
    player2 = models.CharField(blank=True, max_length=30)
    score_p1 = models.CharField(blank=True, max_length=30)
    score_p2 = models.CharField(blank=True, max_length=30)
    winner = models.CharField(blank=True, max_length=30)

    class Meta:
        verbose_name_plural = "Chess Records"

    def __str__(self):
        return self.winner


class PowerliftingModel(models.Model):
    record_id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(IndividualEventsList, on_delete=models.CASCADE)
    date = models.DateField(blank=True)
    # categories = (('Male', 'Male'), ('Female', 'Female'))
    # category = models.CharField(blank=True, max_length=10, choices=categories)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    player_name = models.CharField(blank=True, max_length=30)
    idnum = models.IntegerField(blank=True)
    weight = models.CharField(blank=True, max_length=10)
    result = models.CharField(blank=True, max_length=10)

    class Meta:
        verbose_name_plural = "Powerlifting Records"

    def __str__(self):
        return self.player_name


class TableTennisModel(models.Model):
    record_id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(IndividualEventsList, on_delete=models.CASCADE)
    date = models.DateField(blank=True)
    # categories = (('Male', 'Male'), ('Female', 'Female'))
    # category = models.CharField(blank=True, max_length=10, choices=categories)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    player1 = models.CharField(blank=True, max_length=30)
    player2 = models.CharField(blank=True, max_length=30)
    score_p1 = models.CharField(blank=True, max_length=30)
    score_p2 = models.CharField(blank=True, max_length=30)
    winner = models.CharField(blank=True, max_length=30)

    class Meta:
        verbose_name_plural = "Table-Tennis Records"

    def __str__(self):
        return self.winner
