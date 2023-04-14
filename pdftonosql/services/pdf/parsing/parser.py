import logging
import pytesseract
from pdf2image import convert_from_path, pdfinfo_from_path
from services.pdf.utils.helpers import clean_text
from fastapi import UploadFile
from tempfile import NamedTemporaryFile
import os
from multiprocessing import Process, Queue, Pool, cpu_count
from itertools import chain


class PDFParser():
    def __init__(self):
        logging.info("[PDF Parser] Initialised")

    def _parse_pytesseract(self, page_chunk):
        if "nt" in os.name:
            pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        start_page, chunk = page_chunk
        page_data = []
        for pageNum, imgBlob in enumerate(chunk):
            text = pytesseract.image_to_string(imgBlob, lang='eng')
            page_data.append((start_page + pageNum, clean_text(text)))
        return page_data

    def _get_ocr_body(self, path) -> str:
        body = {}
        pdf_info = pdfinfo_from_path(path)
        max_pages = pdf_info["Pages"]
        pages_chunks = []
        for page in range(1, max_pages+1, 10):
            pages_chunks.append((page, convert_from_path(
                path, first_page=page, last_page=min(page+10-1, max_pages))))
        with Pool(processes=int(cpu_count() * 1.5)) as pool:
            page_results = [pool.apply_async(
                self._parse_pytesseract, (page_chunk,)) for page_chunk in pages_chunks]
            pool.close()
            pool.join()
        multiple_results = list(
            chain(*[page_result.get() for page_result in page_results]))
        for result in multiple_results:
            body[result[0]] = result[1]
        return body

    def parse(self, path: str) -> str:
        pdf_body = self._get_ocr_body(path)
        return pdf_body


def get_pdf_body(file: UploadFile) -> dict:
    pdf_parser = PDFParser()
    temp_file = NamedTemporaryFile(delete=False)
    try:
        file_contents = file.file.read()
        with temp_file as f:
            f.write(file_contents)
    except:
        return ""

    body = pdf_parser.parse(temp_file.name)
    temp_file.close()
    os.remove(temp_file.name)
    return body
