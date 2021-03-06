# Generated by Django 3.0.5 on 2020-04-29 19:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_users_modification_donor"),
    ]

    operations = [
        migrations.RenameField(
            model_name="hospitalprofile",
            old_name="mci_registeration_number",
            new_name="mci_registration_number",
        ),
        migrations.AddField(
            model_name="hospitalprofile",
            name="contact_person_mobile_number",
            field=models.CharField(
                blank=True,
                max_length=15,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the format: '+91xxxxxxxxxx'. Up to 9-10 digits allowed.",
                        regex="^\\+?91?\\d{9,10}$",
                    )
                ],
                verbose_name="Contact Number (+91xxxxxxxxxx)",
            ),
        ),
        migrations.AddField(
            model_name="hospitalprofile",
            name="contact_person_name",
            field=models.CharField(
                blank=True,
                max_length=100,
                null=True,
                verbose_name="Contact Person Name",
            ),
        ),
    ]
