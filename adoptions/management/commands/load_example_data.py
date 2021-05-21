from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from adoptions.models import ExampleData
from pytz import UTC


DATETIME_FORMAT = '%Y/%m/%d'


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the example data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from example_data.csv into our Example data mode"

    def handle(self, *args, **options):
        if ExampleData.objects.exists():
            print('Example data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Loading example data for exampledata available for adoption")
        for row in DictReader(open('./example_data.csv')):
            exampledata = ExampleData()
            exampledata.name = row['ExampleData']
            exampledata.position = row['Position']
            exampledata.office = row['Office']
            exampledata.age = row['Age']
            raw_start_date = row['start date']
            exampledata.salary = row['Salary']
            start_date = UTC.localize(
                datetime.strptime(raw_start_date, DATETIME_FORMAT))
            exampledata.start_date = start_date
            exampledata.save()
