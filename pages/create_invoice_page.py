from playwright.sync_api import Locator, Page, Response

from models import AirWaybill, Invoice


class CreateInvoicePage:
	def __init__(self, page: Page) -> None:
		self.page = page
		self.success_banner: Locator = page.get_by_text("Invoice created successfully")

	def go_to(self) -> Response | None:
		response = self.page.goto("providers/invoices/create")
		self.page.wait_for_url("**/providers/invoices/create")
		return response

	def click_go_back_btn(self) -> None:
		self.page.get_by_role("button", name="Go Back").click()

	def fill_invoice_number(self, invoice_number: str) -> None:
		self.page.get_by_role("textbox", name="Number").fill(invoice_number)

	def fill_issue_date(self, date: str) -> None:
		self.page.get_by_placeholder("Issue date").fill(date)

	def fill_service_month(self, date: str) -> None:
		self.page.get_by_placeholder("Service month").fill(date)

	def fill_amount(self, invoice_amount: int | float) -> None:
		self.page.get_by_placeholder("Amount").fill(str(invoice_amount))

	def select_service_by_label(self, service: str) -> None:
		self.page.get_by_role("combobox", name="Select Service").click()
		self.page.get_by_role("option", name=service).click()

	def select_service_by_index(self, index: int) -> None:
		self.page.get_by_role("combobox", name="Select Service").click()
		self.page.get_by_role("option").nth(index).click()

	def set_attachment_file(self, file_path: str) -> None:
		self.page.get_by_text("Upload attachment fileSelect").set_input_files(file_path)

	def set_details_file(self, file_path: str) -> None:
		locator = self.page.get_by_text("Upload details fileSelect")
		if locator.is_visible():
			locator.set_input_files(file_path)

	def fill_air_waybills_form(
		self, air_waybill_code: str, destination_country: str, air_waybill_weight: float
	) -> None:
		locator = self.page.get_by_role("button", name="Manage AWB List")
		if locator.is_visible():
			locator.click()
			self.page.get_by_role("button", name="Add AWB Row").click()
			self.page.get_by_role("textbox", name="-12345678").fill(air_waybill_code)
			self.page.get_by_role("textbox", name="Search country...").fill(destination_country)
			self.page.get_by_role("option", name=destination_country).click()
			self.page.get_by_placeholder("0").fill(air_waybill_weight)
			self.page.get_by_role("button", name="Done (1 AWBs)").click()

	def fill_items(self, items: int | float) -> None:
		locator = self.page.get_by_placeholder("Items")
		if locator.is_visible():
			if items is None:
				raise ValueError("Items is None")
			locator.fill(items)

	def fill_comment(self, comment: str) -> None:
		self.page.get_by_role("textbox", name="Comment").fill(comment)

	def click_submit_btn(self) -> None:
		self.page.get_by_role("button", name="Submit").click()

	def fill_invoice_form(self, invoice: Invoice, service: str, air_waybill: AirWaybill) -> None:
		self.fill_invoice_number(invoice.number)
		self.fill_issue_date(invoice.issue_date)
		self.fill_service_month(invoice.service_month)
		self.fill_amount(invoice.amount)
		self.set_attachment_file(invoice.attachment)
		self.select_service_by_label(service)
		self.fill_air_waybills_form(
			air_waybill.code, air_waybill.destination_country, air_waybill.weight
		)
		self.set_details_file(invoice.details)
		self.fill_items(invoice.items)
		self.fill_comment(invoice.comment)
		self.click_submit_btn()
