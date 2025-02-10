from rdflib import Graph, Namespace, Literal, URIRef
from owlready2 import get_ontology, sync_reasoner, default_world
from rdflib.plugins.sparql import prepareQuery

g = Graph()
# Define namespaces
g.parse("datafiles/ecommerce_inferred_ontology.ttl", format="turtle")

# Run SPARQL Query to Find High-Value Customers (after reasoning)
query = prepareQuery("""
    PREFIX ecom: <http://example.com/ecommerce#>
    SELECT ?customer WHERE {
        ?customer a ecom:placesOrder .
    }
""")
print("High-Value Customers:")
for row in g.query(query):
    print(row.customer)