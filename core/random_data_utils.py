from faker import Faker
import logging
import uuid

faker = Faker()


def get_first_name():
    first_name = faker.first_name()
    logging.info(f"Generate first name: {first_name}")
    return first_name


def get_last_name():
    last_name = faker.last_name()
    logging.info(f"Generate last name: {last_name}")
    return last_name


def get_unique_email():
    email = "API_TEST_" + str(uuid.uuid1()) + "@mailnesia.com"
    email = email.replace("-","")
    logging.info(f"Generate email: {email}")
    return email


def get_unique_business_name():
    business_name = "API_TEST_" + str(uuid.uuid1())
    business_name = business_name.replace("-","")
    logging.info(f"Generate Business Name: {business_name}")
    return business_name
