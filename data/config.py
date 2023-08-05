import os

from dotenv import dotenv_values

CONFIG_DATA: dict = dict(dotenv_values('data/.env'))
