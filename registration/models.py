from django.db import models
import datetime

# Create your models here.
class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=10, default="Male")

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.category


class Events(models.Model):
    tevent_id = models.AutoField(primary_key=True)
    events = models.CharField(blank=True, max_length=20)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    types = (('T', 'Team'), ('I', 'Individual'))
    type = models.CharField(choices=types, max_length=10)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Events"

    def __str__(self):
        return str('{} {}'.format(self.events, self.category))


class IndividualRegistration(models.Model):
    reg_id = models.AutoField(primary_key=True)
    idnum = models.IntegerField()
    year = models.IntegerField(default=datetime.date.today().year)
    name = models.CharField(max_length=100, blank=True)
    # category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE, limit_choices_to={'type':'I'})
    course = models.CharField(max_length=100, blank=True)
    mobile = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name_plural = "Individual Registrations"

    def __str__(self):
        return self.name


class PermanentTeam(models.Model):
    id = models.IntegerField(primary_key=True)
    event_name = models.ForeignKey(Events, on_delete=models.CASCADE, limit_choices_to={'type':'T'})
    team_name = models.CharField(max_length=30)
    captain = models.CharField(max_length=30)
    vice_captain = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Permanent Teams"

    def __str__(self):
        return str('{} {}'.format(self.team_name, self.event_name))


class TeamPlayers(models.Model):
    player_id = models.AutoField(primary_key=True)
    team_id = models.ForeignKey(PermanentTeam, on_delete=models.CASCADE)
    player_name = models.CharField(max_length=30)
    id_number = models.CharField(max_length=6, default=000000)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Team Players"
    
    def __str__(self):
        return self.player_name


class TeamRegistrationmodel(models.Model):
    reg_id = models.AutoField(primary_key=True)
    year = models.IntegerField(default=datetime.date.today().year)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    team_name = models.ForeignKey(PermanentTeam, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Team Registration"

    def __str__(self):
        return str(self.team_name)


class Rules(models.Model):
    id=models.AutoField(primary_key=True)
    rule = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Rules"
    
    def __str__(self):
        return self.rule
