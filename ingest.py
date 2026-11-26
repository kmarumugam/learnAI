from services.pdf_ingestion import load_pdf

from services.vector_store import (
    create_store
)

chunks = load_pdf(
    "data/pdfs/FeeStructure.pdf"
)

create_store(chunks)

print("Done")