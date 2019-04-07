# Generated by Django 2.0.2 on 2018-02-24 21:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0006_auto_20180211_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='date_published',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='from_passage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_choices', to='story.Passage'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='to_passage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_choices', to='story.Passage'),
        ),
    ]