from fastapi import FastAPI
from rag_retriever import get_rag_answer
from graph_rag import graph_query

app = FastAPI(title="Legal AI System")

@app.get("/legal-query")
def legal_query(q: str):
    answer = get_rag_answer(q)
    return {"answer": answer}

@app.get("/graph-query")
def graph_search(q: str):
    result = graph_query(q)
    return {"result": result}
