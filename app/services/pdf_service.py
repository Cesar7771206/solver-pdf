import pymupdf4llm
import tempfile
import os

class PDFConverterService:
    @staticmethod
    def to_markdown(file_bytes: bytes) -> str:
        with tempfile.NamedTemporaryFile(delete=False, suffix='pdf') as tmp:
            tmp.write(file_bytes)
            tmp_path = tmp.name

        try: 
            md_text = pymupdf4llm.to_markdown(tmp_path)
            return md_text
        
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)