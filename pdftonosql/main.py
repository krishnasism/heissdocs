from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from services.pdf.parsing.parser import get_pdf_body
app = FastAPI()


@app.get("/health-check")
def health_check():
    return {"code": 200, "message": "healthy"}


@app.post("/pdf/upload/")
def upload_pdf(file: UploadFile):
    try:
        pdf_body = get_pdf_body(file)
        return JSONResponse(
            content={
                "parse_result": {
                    "pdf_body": pdf_body
                }
            },
            status_code=200
        )
    except Exception as e:
        return JSONResponse(
            content={
                "error": str(e)
            },
            status_code=500
        )
