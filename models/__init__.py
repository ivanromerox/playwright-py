from dataclasses import dataclass
from typing import list


@dataclass
class AirWaybill:
	code: str
	destination: str
	weight: int | float


@dataclass
class Invoice:
	number: str
	issue_date: str
	service_month: str
	amount: int | float
	attachment: str
	details: str | None
	air_waybills: list[AirWaybill] | None
	items: int | None
	comment: str


@dataclass
class InvoiceFile:
	file_path: str
	invoice: Invoice
