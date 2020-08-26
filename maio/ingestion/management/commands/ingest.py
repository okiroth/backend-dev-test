from django.core.management.base import BaseCommand
from ingestion import ingest


class Command(BaseCommand):

    def handle(self, *args, **options):
        ingest.run()