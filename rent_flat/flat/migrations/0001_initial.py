# Generated by Django 4.2.6 on 2023-11-28 22:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import flat.const
import flat.models
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('fridge', 'Fridge'), ('dishwasher', 'Dishwasher'), ('tv', 'TV'), ('washer', 'Washing machine'), ('furniture', 'Furniture'), ('stove', 'Stove'), ('oven', 'Oven'), ('balcony', 'Balcony'), ('terrace', 'Terrace'), ('elevator', 'elevator'), ('ac', 'Air conditioning')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('price', models.PositiveIntegerField()),
                ('area', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('development_type', models.CharField(choices=[('house', 'Detached house'), ('block', 'Block'), ('tenement', 'Tenement house'), ('rowhouse', 'Rowhouse'), ('semi', 'Semi-detached house'), ('loft', 'Loft'), ('apartment', 'Apartment house')], max_length=10)),
                ('floor', models.CharField(choices=[('zero', 'Ground floor'), ('first', '1 floor'), ('second', '2 floor'), ('third', '3 floor'), ('fourth', '4 floor'), ('fifth', '5 floor'), ('sixth', '6 floor'), ('seventh', '7 floor'), ('eighth', '8 floor'), ('ninth', '9 floor'), ('higher', '> 9 floor')], max_length=10)),
                ('heating', models.CharField(choices=[('district', 'District heating'), ('gas', 'Gas heating'), ('electric', 'Electric heating'), ('boiler', 'Boiler'), ('other', 'Other')], max_length=10)),
                ('year', models.PositiveIntegerField()),
                ('text', models.TextField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Archive', 'Archive')], default=flat.const.Status['Active'], max_length=10)),
                ('equipment', models.ManyToManyField(blank=True, null=True, related_name='flat', to='flat.equip')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='LocationArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(choices=[('LowSilesia', 'Lower Silesia'), ('Kuyavia', 'Kuyavia-Pomerania'), ('Silesia', 'Silesia'), ('Lodzkie', 'Lodzkie'), ('Lublin', 'Lublin'), ('Lubusz', 'Lubusz'), ('LessPoland', 'Lesser Poland'), ('Masovia', 'Masovia'), ('Subcarpathia', 'Subcarpathia'), ('Pomerania', 'Pomerania'), ('WarmMasuria', 'Warmia-Masuria'), ('GreatPoland', 'Greater Poland'), ('WestPomerania', 'West Pomerania')], max_length=20)),
                ('county', models.CharField(choices=[('Warsaw', 'Warsaw'), ('Wroclaw', 'Wroclaw'), ('Cracow', 'Cracow'), ('Gdansk', 'Gdansk'), ('Poznan', 'Poznan'), ('Szczecin', 'Szczecin'), ('Gdynia', 'Gdynia'), ('Czestochowa', 'Czestochowa'), ('Opole', 'Opole'), ('Lodz', 'Lodz'), ('Bialystok', 'Bialystok'), ('Katowice', 'Katowice'), ('Tarnov', 'Tarnov'), ('Krosno', 'Krosno'), ('Rzeszow', 'Rzeszow'), ('Glwice', 'Gliwice'), ('Radom', 'Radom'), ('ZielonGora', 'Zielona Gora'), ('Lublin', 'Lublin'), ('Swinoujscie', 'Swinoujscie'), ('Bydgoszcz', 'Bydgoszcz'), ('JeleniaGora', 'Jelenia Gora'), ('Legnica', 'Legnica'), ('Grudziadz', 'Grudziadz'), ('Torun', 'Torun'), ('Plock', 'Plock'), ('Chorzow', 'Chorzów'), ('Tychy', 'Tychy'), ('Bytom', 'Bytom'), ('Sosnowiec', 'Sosnowiec'), ('Zabrze', 'Zabrze'), ('Kielce', 'Kielce'), ('Olsztyn', 'Olsztyn'), ('Leszno', 'Leszno'), ('Kalisz', 'Kalisz'), ('Koszalin', 'Koszalin')], max_length=20)),
                ('city', models.CharField(choices=[('Warsaw', 'Warsaw'), ('Wroclaw', 'Wroclaw'), ('Cracow', 'Cracow'), ('Gdansk', 'Gdansk'), ('Poznan', 'Poznan'), ('Szczecin', 'Szczecin'), ('Gdynia', 'Gdynia'), ('Czestochowa', 'Czestochowa'), ('Opole', 'Opole'), ('Lodz', 'Lodz'), ('Bialystok', 'Bialystok'), ('Katowice', 'Katowice'), ('Tarnov', 'Tarnov'), ('Krosno', 'Krosno'), ('Rzeszow', 'Rzeszow'), ('Glwice', 'Gliwice'), ('Radom', 'Radom'), ('ZielonGora', 'Zielona Gora'), ('Lublin', 'Lublin'), ('Swinoujscie', 'Swinoujscie'), ('Bydgoszcz', 'Bydgoszcz'), ('JeleniaGora', 'Jelenia Gora'), ('Legnica', 'Legnica'), ('Grudziadz', 'Grudziadz'), ('Torun', 'Torun'), ('Plock', 'Plock'), ('Chorzow', 'Chorzów'), ('Tychy', 'Tychy'), ('Bytom', 'Bytom'), ('Sosnowiec', 'Sosnowiec'), ('Zabrze', 'Zabrze'), ('Kielce', 'Kielce'), ('Olsztyn', 'Olsztyn'), ('Leszno', 'Leszno'), ('Kalisz', 'Kalisz'), ('Koszalin', 'Koszalin')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9'), ('ten', '10'), ('more', 'more than 10')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LocationDistrict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(blank=True, choices=[('Fabryczna', 'Fabryczna'), ('Krzyki', 'Krzyki'), ('PsiePole', 'Psie Pole'), ('Srodmiescie', 'Srodmiescie'), ('Jagodno', 'Jagodno'), ('Nadodrze', 'Nadodrze'), ('Rynek', 'Rynek'), ('StareMiasto', 'Stare Miasto')], max_length=20, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district', to='flat.locationarea')),
            ],
        ),
        migrations.CreateModel(
            name='FlatLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='flat.locationarea')),
                ('district', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='city', chained_model_field='city', on_delete=django.db.models.deletion.CASCADE, to='flat.locationdistrict')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='flat.flat')),
            ],
        ),
        migrations.CreateModel(
            name='FlatImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=flat.models.get_image_filename, verbose_name='Image')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='flat.flat')),
            ],
        ),
        migrations.AddField(
            model_name='flat',
            name='rooms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flat', to='flat.room'),
        ),
        migrations.AddField(
            model_name='flat',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flat', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='flat',
            constraint=models.CheckConstraint(check=models.Q(('area__gte', 0.0)), name='flat_area_range'),
        ),
    ]
