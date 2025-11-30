from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

texts = []
folder = "backend/data/judgments"

for f in os.listdir(folder):
    texts.append(open(f"{folder}/{f}").read())

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
db = FAISS.from_texts(texts, embeddings)
db.save_local("backend/vector_store")
