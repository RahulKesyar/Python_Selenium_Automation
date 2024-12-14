import random
import string
import json
import yaml
from datetime import datetime, timedelta


class Helpers:
    @staticmethod
    def generate_random_string(length=10, chars=string.ascii_letters + string.digits):
        """
        Generate a random string of the specified length.
        :param length: Length of the random string
        :param chars: Character set to use for generation
        :return: Random string
        """
        return ''.join(random.choices(chars, k=length))

    @staticmethod
    def generate_random_email(domain="example.com"):
        """
        Generate a random email address.
        :param domain: Domain for the email address
        :return: Random email string
        """
        username = Helpers.generate_random_string(8, string.ascii_lowercase + string.digits)
        return f"{username}@{domain}"

    @staticmethod
    def get_current_timestamp(format="%Y-%m-%d %H:%M:%S"):
        """
        Get the current timestamp in the specified format.
        :param format: Format of the timestamp
        :return: Current timestamp as a string
        """
        return datetime.now().strftime(format)

    @staticmethod
    def add_days_to_date(date_str, days, format="%Y-%m-%d"):
        """
        Add days to a given date.
        :param date_str: Input date as a string
        :param days: Number of days to add
        :param format: Format of the input and output date
        :return: Updated date as a string
        """
        date_obj = datetime.strptime(date_str, format)
        updated_date = date_obj + timedelta(days=days)
        return updated_date.strftime(format)

    @staticmethod
    def read_json(file_path):
        """
        Read and parse a JSON file.
        :param file_path: Path to the JSON file
        :return: Parsed JSON data
        """
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def read_yaml(file_path):
        """
        Read and parse a YAML file.
        :param file_path: Path to the YAML file
        :return: Parsed YAML data
        """
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    @staticmethod
    def write_json(file_path, data):
        """
        Write data to a JSON file.
        :param file_path: Path to the JSON file
        :param data: Data to write
        """
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def write_yaml(file_path, data):
        """
        Write data to a YAML file.
        :param file_path: Path to the YAML file
        :param data: Data to write
        """
        with open(file_path, 'w') as file:
            yaml.dump(data, file)

    @staticmethod
    def calculate_difference_in_days(start_date, end_date, format="%Y-%m-%d"):
        """
        Calculate the number of days between two dates.
        :param start_date: Start date as a string
        :param end_date: End date as a string
        :param format: Format of the input dates
        :return: Difference in days as an integer
        """
        start = datetime.strptime(start_date, format)
        end = datetime.strptime(end_date, format)
        return (end - start).days

    @staticmethod
    def is_valid_email(email):
        """
        Validate if a string is a properly formatted email.
        :param email: Email string
        :return: Boolean indicating validity
        """
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
