from fastapi import FastAPI

from agents.graph import graph

app = FastAPI()


@app.get("/ask")
def ask(question: str):

    result = graph.invoke(
        {
            "question": question
        }
    )

    return result