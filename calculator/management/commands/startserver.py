import os
import subprocess

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Runs both the Django server and the tailwind service."

    def handle(self, *args, **options):
        # Start the tailwind service but discard its output
        tailwind_command = ["python3", "-m", "manage", "tailwind", "start"]
        with open("nul" if os.name == "nt" else "/dev/null", "w") as fnull:
            tailwind_process = subprocess.Popen(tailwind_command, stdout=fnull, stderr=fnull)
            # collect static
            subprocess.Popen(["python3", "manage.py", "collectstatic", "--no-input"])
            subprocess.Popen(["python3", "manage.py", "tailwind", "build"])
        call_command("runserver")

        # If the runserver command finishes, terminate the Tailwind process
        tailwind_process.terminate()
