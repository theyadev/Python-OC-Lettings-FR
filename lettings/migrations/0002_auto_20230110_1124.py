# Generated by Django 3.0 on 2023-01-10 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO lettings_address (
                number,
                street,
                city,
                state,
                zip_code,
                country_iso_code
            )
            SELECT
                number,
                street,
                city,
                state,
                zip_code,
                country_iso_code
            FROM
                oc_lettings_site_address;
            INSERT INTO lettings_letting (
                title,
                address_id
            )
            SELECT
                title,
                address_id
            FROM
                oc_lettings_site_letting;
        """)
    ]
