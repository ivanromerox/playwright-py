from playwright.sync_api import Locator, Page, Response


class LoginPage:
	def __init__(self, page: Page) -> None:
		self.page = page
		self.user_not_found_alert: Locator = page.get_by_text("User not found")
		self.invalid_password_alert: Locator = page.get_by_text("Invalid password")
		self.short_password_alert: Locator = page.get_by_text("Password must be at least 8")
		self.check_email_alert: Locator = page.get_by_text("Please check your email for")

	def go_to(self) -> Response | None:
		return self.page.goto("login")

	def login(self, email: str, password: str) -> None:
		self.page.get_by_role("textbox", name="Email").fill(email)
		self.page.get_by_role("textbox", name="Password").fill(password)
		self.page.get_by_role("button", name="Login").click()

	def forgot_password(self, email: str) -> None:
		self.page.get_by_text("Forgot your password?").click()
		self.page.get_by_role("textbox", name="Email").fill(email)
		self.page.get_by_role("button", name="Send Recovery Email").click()
