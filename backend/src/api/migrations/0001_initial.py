# Generated by Django 3.2.3 on 2021-06-24 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Gaussian', 'Gaussian')], max_length=10)),
                ('min', models.FloatField()),
                ('max', models.FloatField()),
                ('mean', models.FloatField()),
                ('deviation', models.FloatField()),
                ('value', models.FloatField()),
            ],
            options={
                'verbose_name': 'Distribution',
                'verbose_name_plural': 'Distributions',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('contact_rate', models.DecimalField(decimal_places=3, max_digits=3)),
            ],
            options={
                'verbose_name': 'Measure',
                'verbose_name_plural': 'Measures',
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Probabilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asymp_per_infectious', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='asymp_per_infectious', to='api.distribution')),
                ('carrier_infectability', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='carrier_infectability', to='api.distribution')),
                ('dead_per_icu', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='dead_per_icu', to='api.distribution')),
                ('hospitalized_per_infectious', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='hospitalized_per_infectious', to='api.distribution')),
                ('icu_per_hospitalized', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='icu_per_hospitalized', to='api.distribution')),
                ('infected_from_contact', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='infected_from_contact', to='api.distribution')),
                ('risk_from_symptomatic', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='risk_from_symptomatic', to='api.distribution')),
                ('risk_from_symptotic', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='risk_from_symptotic', to='api.distribution')),
            ],
        ),
        migrations.CreateModel(
            name='Restriction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Restriction',
                'verbose_name_plural': 'Restrictions',
            },
        ),
        migrations.CreateModel(
            name='StageTimes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospitalized_to_icu', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='hospitalized_to_icu', to='api.distribution')),
                ('hospitalized_to_recovered', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='hospitalized_to_recovered', to='api.distribution')),
                ('icu_to_dead', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='icu_to_dead', to='api.distribution')),
                ('icu_to_recovered', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='icu_to_recovered', to='api.distribution')),
                ('incubation', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='incubation', to='api.distribution')),
                ('infectious_asympt', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='infectious_asympt', to='api.distribution')),
                ('infectious_mild', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='infectious_mild', to='api.distribution')),
                ('infectious_to_hospitalized', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='infectious_to_hospitalized', to='api.distribution')),
                ('serial_interval', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='serial_interval', to='api.distribution')),
            ],
        ),
        migrations.CreateModel(
            name='ScenarioNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.group')),
                ('measures', models.ManyToManyField(to='api.Measure')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.node')),
                ('probabilities', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.probabilities')),
                ('stage_times', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.stagetimes')),
            ],
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('simulation_model', models.CharField(max_length=10)),
                ('number_of_groups', models.IntegerField()),
                ('number_of_nodes', models.IntegerField()),
                ('nodes', models.ManyToManyField(to='api.ScenarioNode')),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('dead', models.IntegerField()),
                ('carrier', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='carrier', to='api.distribution')),
                ('exposed', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='exposed', to='api.distribution')),
                ('hospitalized', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='hospitalized', to='api.distribution')),
                ('icu', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='icu', to='api.distribution')),
                ('infectious', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='infectious', to='api.distribution')),
                ('recovered', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='recovered', to='api.distribution')),
            ],
        ),
        migrations.AddField(
            model_name='measure',
            name='restriction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.restriction'),
        ),
        migrations.CreateModel(
            name='SimulationNode',
            fields=[
                ('scenarionode_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.scenarionode')),
                ('population', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.population')),
            ],
            bases=('api.scenarionode',),
        ),
        migrations.CreateModel(
            name='Simulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('start_day', models.DateField()),
                ('number_of_days', models.IntegerField()),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.scenario')),
                ('nodes', models.ManyToManyField(to='api.SimulationNode')),
            ],
        ),
    ]
