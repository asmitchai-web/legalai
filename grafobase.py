from neo4j import GraphDatabase
import os

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j","password"))

def create_node(tx, label, text):
    tx.run("CREATE (n:{label} {text:$text})", text=text)

def build_graph():
    files = os.listdir("backend/data/judgments")

    with driver.session() as session:
        for f in files:
            text = open(f"backend/data/judgments/{f}").read()
            session.write_transaction(create_node, "Judgment", text)

if __name__ == "__main__":
    build_graph()
