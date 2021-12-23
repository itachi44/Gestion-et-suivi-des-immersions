# Generated by Django 2.2.8 on 2021-12-23 16:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import djongo.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_activite', models.CharField(max_length=100)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField(blank=True, null=True)),
                ('cadre', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField()),
                ('cout', models.CharField(blank=True, max_length=100, null=True)),
                ('ressources', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_entreprise', models.CharField(max_length=100)),
                ('localisation', models.CharField(max_length=100)),
                ('domaine_expertise', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifiant', models.CharField(max_length=100)),
                ('mot_de_passe', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Destinataire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Alternance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('convention', models.FileField(blank=True, null=True, storage=djongo.storage.GridFSStorage(base_url='http://127.0.0.1:8000/media/conventions/', collection='media/conventions'), upload_to='media/conventions')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_evaluation', models.FloatField()),
                ('appreciation', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('intitule', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=100)),
                ('destinataires', models.ManyToManyField(to='eptGSI.Destinataire')),
            ],
        ),
        migrations.CreateModel(
            name='Formateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='GrilleEvaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MaitreStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entreprise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='MaitreStage', to='eptGSI.Entreprise')),
            ],
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telephone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='le numero de telephone est invalide!', regex='^(\\+221)?[- ]?(77|70|76|78)[- ]?([0-9]{3})[- ]?([0-9]{2}[- ]?){2}$')])),
                ('compte', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Membre', to='eptGSI.Compte')),
            ],
        ),
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='StagiairePedagogique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niveau_etude', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=100)),
                ('cv', models.FileField(blank=True, null=True, storage=djongo.storage.GridFSStorage(base_url='http://127.0.0.1:8000/media/cvs/', collection='media/cvs'), upload_to='media/cvs')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StagiairePedagogique', to='eptGSI.Membre')),
            ],
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=100)),
                ('activite', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Tache', to='eptGSI.Activite')),
                ('stagiaire_pedagogique', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Tache', to='eptGSI.StagiairePedagogique')),
            ],
        ),
        migrations.CreateModel(
            name='SousTache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_tache', models.CharField(max_length=100)),
                ('echeance', models.DateField(blank=True, null=True)),
                ('date_debut', models.DateField(blank=True, null=True)),
                ('date_fin', models.DateField(blank=True, null=True)),
                ('descriptif', models.TextField(blank=True, null=True)),
                ('commentaire', models.TextField(blank=True, null=True)),
                ('etat', models.BooleanField(default=False)),
                ('technologies', models.TextField(blank=True, null=True)),
                ('langages', models.TextField(blank=True, null=True)),
                ('tache', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SousTache', to='eptGSI.Tache')),
            ],
        ),
        migrations.CreateModel(
            name='ResponsableImmersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ResponsableImmersion', to='eptGSI.Formateur')),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_projet', models.CharField(max_length=100)),
                ('descriptif_projet', models.TextField(blank=True, null=True)),
                ('etat', models.CharField(blank=True, max_length=100, null=True)),
                ('budget', models.CharField(blank=True, max_length=100, null=True)),
                ('duree', models.CharField(blank=True, max_length=100, null=True)),
                ('planning', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Projet', to='eptGSI.Planning')),
                ('responsables_projet', models.ManyToManyField(to='eptGSI.MaitreStage')),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.CharField(max_length=100)),
                ('maitre_stage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Programme', to='eptGSI.MaitreStage')),
                ('projets', models.ManyToManyField(to='eptGSI.Projet')),
                ('stagiaire_pedagogique', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Programme', to='eptGSI.StagiairePedagogique')),
            ],
        ),
        migrations.CreateModel(
            name='PieceJointe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fichier', models.FileField(storage=djongo.storage.GridFSStorage(base_url='http://127.0.0.1:8000/pjs/', collection='media/pjs'), upload_to='pjs')),
                ('evenement', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='PieceJointe', to='eptGSI.Evenement')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=100)),
                ('contenu', models.TextField()),
                ('date_envoi', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('stagiaire_pedagogique', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Message', to='eptGSI.StagiairePedagogique')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maitre_stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Manager', to='eptGSI.MaitreStage')),
            ],
        ),
        migrations.AddField(
            model_name='maitrestage',
            name='membre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MaitreStage', to='eptGSI.Membre'),
        ),
        migrations.CreateModel(
            name='Immersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.CharField(max_length=100)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('rapport_stage', models.FileField(blank=True, null=True, storage=djongo.storage.GridFSStorage(base_url='http://127.0.0.1:8000/rapports/', collection='media/rapports'), upload_to='rapports')),
                ('alternance', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Immersion', to='eptGSI.Alternance')),
                ('stagiaire_pedagogique', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Immersion', to='eptGSI.StagiairePedagogique')),
            ],
        ),
        migrations.AddField(
            model_name='formateur',
            name='membre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Formateur', to='eptGSI.Membre'),
        ),
        migrations.CreateModel(
            name='EvaluationPartielle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EvaluationPartielle', to='eptGSI.Evaluation')),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='EvaluationPartielle', to='eptGSI.Projet')),
                ('stagiaire_pedagogique', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='EvaluationPartielle', to='eptGSI.StagiairePedagogique')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationFinale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EvaluationFinale', to='eptGSI.Evaluation')),
                ('immersion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='EvaluationFinale', to='eptGSI.Immersion')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationApprentissage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grille', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='EvaluationApprentissage', to='eptGSI.GrilleEvaluation')),
                ('immersion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='EvaluationApprentissage', to='eptGSI.Immersion')),
                ('stagiaire_pedagogique', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='EvaluationApprentissage', to='eptGSI.StagiairePedagogique')),
            ],
        ),
        migrations.AddField(
            model_name='evaluation',
            name='grille',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Evaluation', to='eptGSI.GrilleEvaluation'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='maitre_stage',
            field=models.ManyToManyField(to='eptGSI.MaitreStage'),
        ),
        migrations.CreateModel(
            name='Critere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_critere', models.CharField(max_length=100)),
                ('pourcentage', models.CharField(max_length=100)),
                ('grille', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Critere', to='eptGSI.GrilleEvaluation')),
            ],
        ),
        migrations.CreateModel(
            name='Conge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('motif', models.TextField()),
                ('stagiaire_pedagogique', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Conge', to='eptGSI.StagiairePedagogique')),
            ],
        ),
        migrations.AddField(
            model_name='alternance',
            name='entreprise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Alternance', to='eptGSI.Entreprise'),
        ),
        migrations.AddField(
            model_name='alternance',
            name='planning',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Alternance', to='eptGSI.Planning'),
        ),
        migrations.AddField(
            model_name='activite',
            name='projet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Activite', to='eptGSI.Projet'),
        ),
    ]