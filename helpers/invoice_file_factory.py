from helpers import DataFactory
from models import Invoice, InvoiceFile
from utils.excel_factory import ExcelFactory


class InvoiceFileFactory:
	@staticmethod
	def create_invoice_import_file() -> InvoiceFile:
		invoice: Invoice = DataFactory.create_invoice()
		headers = ["Number", "Amount", "Issue Date", "Service Month"]
		data_row = [
			invoice.number,
			str(invoice.amount),
			invoice.issue_date,
			invoice.service_month,
		]

		filename = f"invoice_{invoice.issue_date}.xlsx"
		excel_gen = ExcelFactory.get_instance()
		file_path = excel_gen.create_file(filename, headers, [data_row])

		return InvoiceFile(file_path=file_path, invoice=invoice)

	@staticmethod
	def delete_generated_file(file_path: str) -> None:
		excel_gen = ExcelFactory.get_instance()
		excel_gen.delete_file(file_path)
