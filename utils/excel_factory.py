from pathlib import Path
from typing import Any

from openpyxl import Workbook


class ExcelFactory:
	_instance: ExcelFactory | None = None

	def __new__(cls) -> ExcelFactory:
		if cls._instance is None:
			cls._instance = super().__new__(cls)
			cls._instance._init()
		return cls._instance

	def _init(self) -> None:
		project_root = Path(__file__).parent.parent
		self._output_folder = project_root / "assets" / "output"
		self._output_folder.mkdir(parents=True, exist_ok=True)

	@classmethod
	def get_instance(cls) -> ExcelFactory:
		return cls()

	def create_file(
		self,
		filename: str,
		headers: list[str],
		data_rows: list[list[Any]],
		sheet_name: str = "Sheet1",
	) -> str:
		workbook = Workbook()
		worksheet = workbook.active
		worksheet.title = sheet_name

		worksheet.append(headers)
		for row in data_rows:
			worksheet.append(row)

		file_path = self._output_folder / filename
		workbook.save(str(file_path))
		return str(file_path)

	def delete_file(self, file_path: str) -> None:
		path = Path(file_path)
		if path.exists():
			path.unlink()
