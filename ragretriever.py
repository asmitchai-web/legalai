from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import GPT4All

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
db = FAISS.load_local("vector_store", embeddings)

llm = GPT4All(model="llama-3-8b-instruct.gguf")

def get_rag_answer(query: str):
    docs = db.similarity_search(query, k=4)
    context = "\n\n".join([d.page_content for d in docs])
    
    prompt = f"""You are a legal expert AI.
Use ONLY the context below to answer.

Context:
{context}

Question: {query}
Answer:"""

    return llm(prompt)
