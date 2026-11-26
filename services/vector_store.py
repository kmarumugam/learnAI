from langchain_chroma import Chroma
from langchain_huggingface  import   HuggingFaceEmbeddings



embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def create_store(chunks):

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="data/chroma_db"
    )

    db.persist()


def get_store():

    return Chroma(
        persist_directory="data/chroma_db",
        embedding_function=embeddings
    )

