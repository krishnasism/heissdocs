from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer
from services.security.verify_token import verify_token
from services.local.postgres import PostgresManager
from services.qunda.qunda import ask
import logging

router = APIRouter()
token_auth_scheme = HTTPBearer()
pm = PostgresManager()


@router.get("/ask")
async def ask_pdf(
    query: str,
    user_email: str,
    model: str,
    authenticated: bool = Depends(verify_token),
):
    query = query.lower()
    try:
        answer, source_metadata = await ask(
            user_email=user_email,
            question=query,
            model=model,
        )
        return JSONResponse(
            content={
                "answer": answer,
                "source_metadata": source_metadata,
            },
            status_code=200
            if answer != "Sorry, I couldn't find an answer to your question."
            else 404,
        )
    except Exception as e:
        logging.error(f"[Qunda] {e}")
        return JSONResponse(
            content={
                "answer": "Sorry, I couldn't find an answer to your question.",
            },
            status_code=404,
        )
