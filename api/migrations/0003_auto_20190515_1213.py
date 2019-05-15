# Generated by Django 2.2.1 on 2019-05-15 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190515_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bares',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Bartender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('bar_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Bares')),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('state', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_De_Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_detalleOrden', models.DateField()),
                ('estado_DDO', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ordenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_order', models.DateField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Clientes')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto_name', models.CharField(default='', max_length=30)),
                ('estado_producto', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Promociones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Productos')),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AddField(
            model_name='ordenes',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Productos'),
        ),
        migrations.AddField(
            model_name='detalle_de_orden',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Ordenes'),
        ),
    ]
