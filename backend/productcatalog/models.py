from django.db import models
import uuid

class JSONProduct(models.Model):
    productId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    productName = models.CharField(max_length=100)
    productOwnerName = models.CharField(max_length=100)
    # Other fields

    # class Meta:
    #     managed = False  # Prevent migrations for this model
    #     db_table = 'your_table_name'  # Set the table name if necessary
    #     using = 'json_db'  # Specify the database connection