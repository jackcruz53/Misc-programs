
import csv
from django.core.management.base import BaseCommmand
from django.http import HttpResponse
from django.db import models
import datetime

class Exportcommand(BaseCommand):
    help = "Allows for the exporting of event/task data in CSV format"
    def __init__(self)
    
    def task_export
        from django.models import task
        csv_met = {
                'file': '/tmp/{event}-export'datetime.datetime.now() ,
                'class': task,
                'attributes': ('summary', 'description','time_estimate_minutes'}
        self._format_csv(csv_met)
        def _format_csv(self, csv_met):
            f = open(csv_met['file'], 'w')
            writer = csv.writer(f,
            writer.writerow(csv_met['Task Name', 'Task Description', 'Time Estimate'])
            for obj in csv_met['class'].objects.all():
                row = getattr(obj,field) for field in csv_met['attributes']
                writer.writerow(row)
            f.close
