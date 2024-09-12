from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название товара')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('articul', models.PositiveIntegerField(blank=True, null=True, unique=True, verbose_name='Артикул')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
        ),
    ]
