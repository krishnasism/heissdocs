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
    authenticated: bool = Depends(verify_token),
):
    query = query.lower()
    answer = ask(
        user_email=user_email,
        question=query,
    )
    return JSONResponse(
        content={
            "answer": answer,
        },
        status_code=200
        if answer != "Sorry, I couldn't find an answer to your question."
        else 404,
    )
