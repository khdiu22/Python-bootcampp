from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_make_code_required_unique"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="stock",
            new_name="quantity",
        ),
    ]