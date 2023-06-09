# Generated by Django 3.0.7 on 2023-04-04 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=100)),
                ('result', models.TextField()),
                ('notes', models.TextField(blank=True)),
                ('ordering_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referred_doctor', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Patient')),
                ('referring_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.CharField(max_length=200)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_company_name', models.CharField(max_length=100)),
                ('policy_number', models.CharField(max_length=50)),
                ('group_number', models.CharField(blank=True, max_length=50)),
                ('policy_holder_name', models.CharField(blank=True, max_length=100)),
                ('policy_holder_relationship', models.CharField(blank=True, max_length=50)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Immunization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_type', models.CharField(max_length=100)),
                ('date_administered', models.DateField()),
                ('notes', models.TextField(blank=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=100)),
                ('relative', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=50)),
                ('notes', models.TextField(blank=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergen', models.CharField(max_length=100)),
                ('severity', models.CharField(max_length=20)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Patient')),
            ],
        ),
    ]
