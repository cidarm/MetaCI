# Generated by Django 2.2.5 on 2019-10-02 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("build", "0030_build_priority")]

    operations = [migrations.RemoveField(model_name="build", name="priority")]
