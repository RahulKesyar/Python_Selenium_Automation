import random
import string
import json
import yaml
from datetime import datetime, timedelta

class Helpers:
    @staticmethod
    def generate_random_string(length=10, chars=string.ascii_letters + string.digits):
        """
        Generate the random string for the specified length.
        :param length: length of the random string
        :param chars: Character set to use for the generation
        :return: Random string.
        """
        return ''.join(random.choice(chars, k=length))

    @staticmethod
    def generate_random_email(domain='example.com'):
        """

        :param domain:
        :return:
        """
        username = Helpers.generate_random_string(8, string.ascii_lowercase + string.digits)
        return f"{username}@{domain}"
    @staticmethod
    def get_current_timestamp(format="%Y-%m-%d %H:%M:%S"):
        """

        :param format: Date and time format
        :return: current timestamp
        """
        return datetime.now().strftime(format)

