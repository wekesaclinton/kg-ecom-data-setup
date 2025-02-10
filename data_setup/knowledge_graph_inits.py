from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS, OWL

# Create a graph to hold the ontology
def create_graph():
    g = Graph()
    # Define namespaces
    ns = Namespace("http://example.org/ecommerce#")
    g.bind("ecom", ns)

    # Define classes (entities)
    Customer = ns.Customer
    Order = ns.Order
    Product = ns.Product
    SupportTicket = ns.SupportTicket
    Agent = ns.Agent
    FAQ = ns.FAQ

    # Add classes to the graph
    g.add((Customer, RDF.type, OWL.Class))
    g.add((Order, RDF.type, OWL.Class))
    g.add((Product, RDF.type, OWL.Class))
    g.add((SupportTicket, RDF.type, OWL.Class))
    g.add((Agent, RDF.type, OWL.Class))
    g.add((FAQ, RDF.type, OWL.Class))

    # Define properties (relationships)
    # Add properties to the graph
    g.add((ns.placesOrder, RDF.type, OWL.ObjectProperty))
    g.add((ns.containsProduct, RDF.type, OWL.ObjectProperty))
    g.add((ns.raisedByCustomer, RDF.type, OWL.ObjectProperty))
    g.add((ns.handlesTicket, RDF.type, OWL.ObjectProperty))
    g.add((ns.relatedToIssueType, RDF.type, OWL.ObjectProperty))

    # Define domain and range for properties
    g.add((ns.placesOrder, RDFS.domain, Customer))
    g.add((ns.placesOrder, RDFS.range, Order))
    g.add((ns.containsProduct, RDFS.domain, Order))
    g.add((ns.containsProduct, RDFS.range, Product))
    g.add((ns.raisedByCustomer, RDFS.domain, SupportTicket))
    g.add((ns.raisedByCustomer, RDFS.range, Customer))
    g.add((ns.handlesTicket, RDFS.domain, Agent))
    g.add((ns.handlesTicket, RDFS.range, SupportTicket))
    g.add((ns.relatedToIssueType, RDFS.domain, FAQ))
    g.add((ns.relatedToIssueType, RDFS.range, SupportTicket))
    # Serialize the ontology to a file (e.g., in Turtle format)
    g.serialize(destination="datafiles/ecommerce_ontology.ttl", format="turtle")
    print("Ontology created and saved to 'ecommerce_kg_ontology.ttl'.")
def load_graph() -> Graph:
    g = Graph()
    # Define namespaces
    g.parse("datafiles/ecommerce_ontology.ttl", format="turtle")
    return g