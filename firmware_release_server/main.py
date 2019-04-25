import os
import subprocess
import sys

import django

# setup django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firmware_release_server.settings")
django.setup()

from django.core.management import call_command

try:
    production = sys.argv[1] == "production"
except IndexError:
    production = False

if production:
    import gunicorn.app.wsgiapp as wsgi

    call_command("migrate")
    call_command("collectstatic", "--noinput")

    subprocess.call(["nginx"])

    # This is just a simple way to supply args to gunicorn
    sys.argv = [
        ".",
        f"--bind unix:/home/firmware_release_server.sock",
        "firmware_release_server.wsgi",
    ]
    wsgi.run()
else:
    call_command("runserver")
