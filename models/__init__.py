from dataclasses import dataclass
from typing import List, Optional, Union


@dataclass
class AirWaybill:
	code: str
	destination: str
	weight: Union[int, float]


@dataclass
class Invoice:
	number: str
	issue_date: str
	service_month: str
	amount: Union[int, float]
	attachment: str
	details: Optional[str]
	air_waybills: Optional[List[AirWaybill]]
	items: Optional[int]
	comment: str


@dataclass
class InvoiceFile:
	file_path: str
	invoice: Invoice
