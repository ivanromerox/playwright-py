from playwright.sync_api import Locator, Page
from models import AirWaybill, Invoice


class EditInvoicePage:
	def __init__(self, page: Page) -> None:
		self.page = page
		self.success_banner: Locator = page.get_by_text("Invoice created successfully")

	def click_go_back_btn(self) -> None:
		self.page.get_by_role("button", name="Go Back").click()

	def fill_invoice_number(self, invoice_number: str) -> None:
		self.page.get_by_role("textbox", name="Number").fill(invoice_number)

	def fill_service_month(self, date: str) -> None:
		self.page.get_by_role("textbox", name="Service Month").fill(date)

	def fill_amount(self, invoice_amount: int | float) -> None:
		self.page.get_by_role("spinbutton", name="Amount").fill(str(invoice_amount))

	def fill_issue_date(self, date: str) -> None:
		self.page.get_by_role("textbox", name="Issue Date").fill(date)

	def select_service_by_label(self, service: str) -> None:
		self.page.get_by_role("combobox", name="Select Service").click()
		self.page.get_by_role("option", name=service).click()

	def select_service_by_index(self, index: int) -> None:
		self.page.get_by_role("combobox", name="Select Service").click()
		self.page.get_by_role("option").nth(index).click()

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

	def fill_items(self, items: int | None) -> None:
		locator = self.page.get_by_role("textbox", name="Items")
		if locator.is_visible():
			if items is None:
				raise ValueError("Items is None")
			locator.fill(str(items))

	def set_attachment_file(self, file_path: str) -> None:
		self.page.get_by_role("textbox", name="Attachment").set_input_files(file_path)

	def set_details_file(self, file_path: str) -> None:
		locator = self.page.get_by_role("textbox", name="Details")
		if locator.is_visible():
			locator.set_input_files(file_path)

	def fill_comment(self, comment: str) -> None:
		self.page.get_by_role("textbox", name="Comment").fill(comment)

	def click_update_btn(self) -> None:
		self.page.get_by_role("button", name="Update").click()

	def fill_invoice_form(self, invoice: Invoice, service: str, air_waybill: AirWaybill) -> None:
		self.fill_invoice_number(invoice.number)
		self.fill_issue_date(invoice.issue_date)
		self.fill_service_month(invoice.service_month)
		self.fill_amount(invoice.amount)
		self.select_service_by_label(service)
		self.fill_air_waybills_form(
			air_waybill.code, air_waybill.destination_country, air_waybill.weight
		)
		self.fill_items(invoice.items)
		self.fill_comment(invoice.comment)
		self.click_update_btn()
