from django.db import models
from django.conf import settings
import boto3
from io import StringIO
import pandas as pd
from myapp.models.employee import Employee


# Create your models here.
class SyncEmployee(models.Model):
    first_name = models.CharField(max_length=20, default="", blank=False)
    last_name = models.CharField(max_length=20, default="", blank=False)

    class Meta:
        managed = False

    @staticmethod
    def execute():
        print("sync_csv")

        s3 = boto3.resource(
            "s3",
            endpoint_url=settings.S3_URL,
            aws_access_key_id=settings.IAM_ACCESS_KEY,
            aws_secret_access_key=settings.IAM_SECRET_KEY,
        )

        obj = s3.Object(
            bucket_name=settings.SYNC_DATA_BUCKET, key="sync_data/syncdata.csv"
        )
        res = obj.get()
        body = res["Body"].read().decode("utf-8")

        data = pd.read_csv(StringIO(body), chunksize=settings.SYNC_CHUNK_SIZE)
        print(data)
        for d in data:
            syncEmployees = [
                SyncEmployee(first_name=row.first_name, last_name=row.last_name)
                for index, row in d.iterrows()
            ]
            print(syncEmployees)

            employees = [
                Employee(first_name=sync.first_name, last_name=sync.last_name)
                for sync in syncEmployees
            ]

            print(len(employees))
            for employee in employees:
                print(
                    "_".join(
                        [
                            str(employee.employee_id),
                            employee.first_name,
                            employee.last_name,
                        ]
                    )
                )
            Employee.objects.bulk_create(employees, settings.SYNC_BATCH_SIZE)
            print("bulk_create")