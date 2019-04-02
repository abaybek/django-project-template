#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import dotenv

if __name__ == "__main__":
    dotenv.read_dotenv()
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', os.getenv('BACKEND_ENV'))

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
