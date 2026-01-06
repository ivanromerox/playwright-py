from playwright.sync_api import Locator, Page, Response


class HomePage:
	def __init__(self, page: Page) -> None:
		self.page = page
		self.import_success_banner: Locator = page.get_by_text("Successful import")
		self.delete_success_banner: Locator = page.get_by_text("Invoice deleted successfully")

	def go_to(self) -> Response | None:
		return self.page.goto("providers/portal/invoices")

	def click_dark_mode_btn(self) -> None:
		self.page.get_by_role("button", name="Toggle color mode").click()

	def logout(self, user: str) -> None:
		self.page.getByText(user, {exact: true}).click()
		self.page.get_by_role("menuitem", name="Logout").click()

	def click_create_multiple_invoices_btn(self) -> None:
		self.page.get_by_role("button", name="Create Multiple Invoices").click()

	def click_create_invoice_btn(self) -> None:
		self.page.get_by_role("button", name="Create Invoice").click()

	def import_invoice_draft(self, file_path: str) -> None:
		self.page.get_by_role("button", name="Import Invoice").click()
		self.page.get_by_role("dialog", name="Import Invoices").locator("label").set_input_files(
			file_path
		)

	def click_draft_invoices_btn(self) -> None:
		self.page.get_by_role("tab", name="Draft Invoices").click()

	def click_official_invoices_btn(self) -> None:
		self.page.get_by_role("tab", name="Invoices").click()

	def fill_search_invoice_by_number(self, invoice_number: str) -> None:
		self.page.get_by_role("textbox", name="Search by invoice number…").fill(invoice_number)

	def filter_draft_invoice(self, invoice_number: str) -> None:
		self.fill_search_invoice_by_number(invoice_number)

	def filter_by_services(self, service: str) -> None:
		self.page.get_by_role("button", name="By Services").click()
		self.page.get_by_role("menuitem", name=service).click()

	def filter_by_status(self, status: str) -> None:
		self.page.get_by_role("button", name="By Status").click()
		self.page.get_by_role("menuitem", name=status).click()

	def filter_by_issued_date(self) -> None:
		self.page.get_by_role("button", name="By Issued Date").click()
		self.page.get_by_role("button", name="Apply Date Filter").click()

	def filter_by_service_month(self) -> None:
		self.page.get_by_role("button", name="By Service Month").click()
		self.page.get_by_role("textbox", name="Service until").click()
		self.page.get_by_role("button", name="Apply Date Filter").click()

	def click_reset_filters_btn(self) -> None:
		self.page.get_by_role("button", name="Reset").click()

	def click_sort_by_issue_date_btn(self, order_direction: str) -> None:
		self.page.get_by_role("button", name=f"Sort by issue date: {order_direction}").click()

	def click_edit_invoice_draft_btn(self) -> None:
		self.page.get_by_role("button", name="Edit Draft").first.click()

	def delete_invoice_draft(self, password: str) -> None:
		self.page.get_by_role("button", name="Delete Draft").last.click()
		self.page.get_by_role("textbox", name="Enter your password").fill(password)
		self.page.get_by_role("button", name="Delete").click()

	def click_send_invoice_draft_btn(self) -> None:
		self.page.get_by_role("button", name="Send Draft").nth(1).click()
