# Generated by Django 4.2.3 on 2023-07-31 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_alter_post_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=16, verbose_name="Имя комментатора"),
                ),
                (
                    "text",
                    models.CharField(max_length=300, verbose_name="Текст комментария"),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now=True, verbose_name="Дата создания"),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_comment",
                        to="posts.post",
                        verbose_name="Запись",
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий",
                "verbose_name_plural": "Комментарии",
            },
        ),
    ]
