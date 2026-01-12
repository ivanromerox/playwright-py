from datetime import datetime

from faker import Faker

from models import AirWaybill, Invoice

fake = Faker()


class DataFactory:
	@staticmethod
	def create_awb() -> AirWaybill:
		prefix = fake.random_int(min=100, max=999)
		suffix = fake.random_int(min=10000000, max=99999999)
		return AirWaybill(
			code=f"{prefix}-{suffix}",
			destination=fake.country(),
			weight=float(fake.pyfloat(min_value=1.0, max_value=5000.0, right_digits=3)),
		)

	@staticmethod
	def create_invoice(awb_count: int = 1) -> Invoice:
		today = datetime.now().strftime("%Y-%m-%d")
		awbs = [DataFactory.create_awb() for _ in range(awb_count)]

		return Invoice(
			number=str(fake.random_int(min=100000000, max=999999999)),
			issue_date=today,
			service_month=today,
			amount=float(fake.pyfloat(min_value=100, max_value=999999, right_digits=2)),
			airwaybills=awbs,
			items=fake.random_int(10, max=999),
			attachment="/assets/receipt.png",
			details="/assets/details.png",
		)
