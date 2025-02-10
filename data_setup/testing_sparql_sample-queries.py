from rdflib import Graph, Namespace, Literal, URIRef

# Create a graph to hold the ontology
g = Graph()
# Define namespaces
g.parse("datafiles/ecommerce_inferred_ontology.ttl", format="turtle")
query1 = """
PREFIX ecom: <http://example.org/ecommerce#>
SELECT ?customerName ?cost ?orderStatus WHERE {
    ?customer a ecom:Customer ;
              ecom:name ?customerName ;
              ecom:placesOrder ?order .
    ?order a ecom:Order ;
           ecom:cost ?cost ;
           ecom:orderStatus ?orderStatus;
           ecom:orderStatus "delivered" .
}
"""

query2 = """
PREFIX ecom: <http://example.org/ecommerce#>
SELECT ?customer WHERE {
    ?customer a ecom:Customer ;
              ecom:placesOrder ?order .
    ?order a ecom:Order ;
           ecom:orderStatus "delivered" ;
           ecom:containsProduct ?product .
    ?product a ecom:Product ;
           ecom:productName "vivo Xplay6" .      
}
"""

# Execute the query
results = g.query(query2)
print("Customers and Their Orders:")
for row in results:
    print(row)
    # print(f"Customer: {row.customerName}, Email: {row.email}")