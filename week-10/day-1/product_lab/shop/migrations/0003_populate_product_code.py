from django.db import migrations

def populate_code(apps, schema_editor):
    Product = apps.get_model("shop", "Product")
    for p in Product.objects.all():
        p.code = f"P{p.pk}"
        p.save(update_fields=["code"])

class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0002_add_product_code"),
    ]

    operations = [
        migrations.RunPython(populate_code, migrations.RunPython.noop),
    ]