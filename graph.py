from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "password")
)

def graph_query(query: str):
    cypher = f"""
    MATCH (n)-[r]->(m)
    WHERE n.text CONTAINS '{query}' OR m.text CONTAINS '{query}'
    RETURN n, r, m LIMIT 10
    """
    with driver.session() as session:
        result = session.run(cypher)
        return [record.data() for record in result]
