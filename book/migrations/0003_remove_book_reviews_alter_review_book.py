# Generated by Django 5.0 on 2023-12-22 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_reviews_alter_review_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='reviews',
        ),
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Review', to='book.book'),
        ),
    ]
