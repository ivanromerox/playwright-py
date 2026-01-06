from typing import Any, Union
from playwright.sync_api import Locator, Page


class EditInvoicePage:
	def __init__(self, page: Page) -> None:
		self.page = page
		self.success_banner: Locator = page.get_by_text("Invoice created successfully")

	def fill_invoice_number(self, invoice_number: str) -> None:
		self.page.get_by_role("textbox", name="Number").fill(invoice_number)

	def fill_service_month(self, date: str) -> None:
		self.page.get_by_role("textbox", name="Service Month").fill(date)

	def fill_amount(self, invoice_amount: Union[int, float]) -> None:
		self.page.get_by_role("spinbutton", name="Amount").fill(str(invoice_amount))

	def fill_issue_date(self, date: str) -> None:
		self.page.get_by_role("textbox", name="Issue Date").fill(date)

	def select_service_by_label(self, service: str) -> None:
		self.page.get_by_role("combobox", name="Select Service").click()
		self.page.get_by_role("option", name=service).click()

	def select_service_by_index(self, index: int) -> None:
		self.page.get_by_role("combobox", name="Select Service").click()
		self.page.get_by_role("option").nth(index).click()

	def fill_awb(self, awb: str) -> None:
		locator = self.page.get_by_role("textbox", name="AWB")
		if locator.is_visible():
			locator.fill(awb)

	def fill_kg(self, weight: Union[int, float]) -> None:
		locator = self.page.get_by_placeholder("KG")
		if locator.is_visible():
			locator.fill(str(weight))

	def fill_items(self, items: Union[int, None]) -> None:
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

	def click_go_back_btn(self) -> None:
		self.page.get_by_role("button", name="Go Back").click()

	def click_update_btn(self) -> None:
		self.page.get_by_role("button", name="Update").click()

	def fill_invoice_form(self, invoice: Any, service: str) -> None:
		self.fill_invoice_number(invoice.number)
		self.fill_issue_date(invoice.issue_date)
		self.fill_service_month(invoice.service_month)
		self.fill_amount(invoice.unit_price)
		self.select_service_by_label(service)
		self.fill_awb(invoice.awb)
		self.fill_kg(invoice.kg)
		self.fill_items(invoice.items)
		self.click_update_btn()
