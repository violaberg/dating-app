from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_update_profile_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='Profile',
            name='relationship_goal',
        ),
        migrations.RemoveField(
            model_name='Profile',
            name='gender_preference',
        ),
        migrations.RemoveField(
            model_name='Profile',
            name='age_preference',
        ),
    ]
