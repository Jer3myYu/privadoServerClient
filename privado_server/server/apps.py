import os

from django.apps import AppConfig


class ServerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server'

    def ready(self):
        """Initialize the thread handler."""
        if os.environ.get('RUN_MAIN', None) == 'true':
            from server.threading import Thread_Pool

            self.threads = Thread_Pool()
