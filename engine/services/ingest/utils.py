from langchain.text_splitter import CharacterTextSplitter
from typing import List

def get_chunks(
        text: str,
        chunk_size: int=1000,
        chunk_overlap=200,
        separator="\n",
    ) -> List[str]:
    text_splitter = CharacterTextSplitter(
        separator=separator,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )

    chunks = text_splitter.split_text(text)
    return chunks