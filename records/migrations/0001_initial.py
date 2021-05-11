# Generated by Django 3.1.4 on 2021-05-09 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamRecordModel',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('score_team1', models.CharField(blank=True, max_length=30)),
                ('score_team2', models.CharField(blank=True, max_length=30)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.teameventlist')),
                ('winner', models.ForeignKey(limit_choices_to={'year': 2021}, on_delete=django.db.models.deletion.CASCADE, related_name='team3', to='registration.teamregistrationmodel')),
            ],
            options={
                'verbose_name_plural': 'Team Records',
            },
        ),
        migrations.CreateModel(
            name='TableTennisModel',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True)),
                ('player1', models.CharField(blank=True, max_length=30)),
                ('player2', models.CharField(blank=True, max_length=30)),
                ('score_p1', models.CharField(blank=True, max_length=30)),
                ('score_p2', models.CharField(blank=True, max_length=30)),
                ('winner', models.CharField(blank=True, max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.categories')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.individualeventslist')),
            ],
            options={
                'verbose_name_plural': 'Table-Tennis Records',
            },
        ),
        migrations.CreateModel(
            name='PowerliftingModel',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True)),
                ('player_name', models.CharField(blank=True, max_length=30)),
                ('idnum', models.IntegerField(blank=True)),
                ('weight', models.CharField(blank=True, max_length=10)),
                ('result', models.CharField(blank=True, max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.categories')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.individualeventslist')),
            ],
            options={
                'verbose_name_plural': 'Powerlifting Records',
            },
        ),
        migrations.CreateModel(
            name='ChessModel',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True)),
                ('player1', models.CharField(blank=True, max_length=30)),
                ('player2', models.CharField(blank=True, max_length=30)),
                ('score_p1', models.CharField(blank=True, max_length=30)),
                ('score_p2', models.CharField(blank=True, max_length=30)),
                ('winner', models.CharField(blank=True, max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.categories')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.individualeventslist')),
            ],
            options={
                'verbose_name_plural': 'Chess Records',
            },
        ),
        migrations.CreateModel(
            name='CarromModel',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True)),
                ('team1_player1', models.CharField(blank=True, max_length=30)),
                ('team1_player2', models.CharField(blank=True, max_length=30)),
                ('team2_player1', models.CharField(blank=True, max_length=30)),
                ('team2_player2', models.CharField(blank=True, max_length=30)),
                ('winner', models.CharField(blank=True, max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.categories')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.individualeventslist')),
            ],
            options={
                'verbose_name_plural': 'Carrom Records',
            },
        ),
        migrations.CreateModel(
            name='BadmintonModel',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True)),
                ('team1_player1', models.CharField(blank=True, max_length=30)),
                ('team1_player2', models.CharField(blank=True, max_length=30)),
                ('team2_player1', models.CharField(blank=True, max_length=30)),
                ('team2_player2', models.CharField(blank=True, max_length=30)),
                ('score', models.CharField(blank=True, max_length=10)),
                ('winner', models.CharField(blank=True, max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.categories')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.individualeventslist')),
            ],
            options={
                'verbose_name_plural': 'Badminton Records',
            },
        ),
        migrations.CreateModel(
            name='AthleticsModel',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True)),
                ('event_name', models.CharField(blank=True, max_length=30)),
                ('player_name', models.CharField(blank=True, max_length=30)),
                ('idnum', models.IntegerField(blank=True)),
                ('result', models.CharField(blank=True, max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.categories')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.individualeventslist')),
            ],
            options={
                'verbose_name_plural': 'Athletics Records',
            },
        ),
    ]
