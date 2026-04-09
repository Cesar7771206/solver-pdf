from fastapi import APIRouter, UploadFile, File, HTTPException # UploadFile y File vienen de pip install python-multipart
from app.schemas.pdf import MarkdownResponse
from app.services.pdf_service import PDFConverterService

router = APIRouter(prefix='/pdf', tags=["Conversion"])

@router.post('/convertir-pdf-markdown', response_model=MarkdownResponse)
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith('pdf'):
        raise HTTPException(status_code=400, detail="El archivo debe ser un PDF")
    
    pdf_bytes = await file.read()

    try: 
        texto_markdown = PDFConverterService.to_markdown(pdf_bytes)

        return MarkdownResponse(
            filename=file.filename,
            content=texto_markdown,
            size_bytes=len(pdf_bytes)
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el PDF: {str(e)}")