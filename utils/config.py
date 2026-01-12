import os

from dotenv import load_dotenv

load_dotenv()


class Config:
	_auth_credentials = os.getenv("AUTH_CREDS")
	if not _auth_credentials:
		raise ValueError("Missing AUTH_CREDS environment variable")

	parts = _auth_credentials.split(":", 1)
	if len(parts) != 2:
		raise ValueError("AUTH_CREDS must be in 'email:password' format")

	AUTH_EMAIL, AUTH_PASSWORD = parts

	BASE_URL = os.getenv("BASE_URL")
	if not BASE_URL:
		raise ValueError("Missing BASE_URL environment variable")
