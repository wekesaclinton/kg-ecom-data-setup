from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS, OWL
from uuid import uuid4
import hashlib

from knowledge_graph_import_data import Customer, Order, Product
from typing import List, Optional, Dict, Any


def add_data_to_knowledge_graph(g: Graph, customer_data: List[Customer]):
    print("We have recieved data now to add to a model.")

    ns = Namespace("http://example.org/ecommerce#")
    g.bind("ecom", ns)
    g.bind("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    g.bind("rdfs", "http://www.w3.org/2000/01/rdf-schema#")

    if customer_data:
        for customer in customer_data:
            print("We are handling customers data now.")
            # give customer uniqueness which is repeatable
            unique_id = hashlib.sha256(customer.customer_id.encode()).hexdigest()
            customer1 = URIRef(ns + unique_id)
            # add the customer details
            g.add((customer1, RDF.type, ns.Customer))
            g.add((customer1, ns.name, Literal(customer.customer_name)))
            g.add((customer1, ns.email, Literal(customer.customer_id)))

            for index, order in enumerate(customer.orders):
                order1 = URIRef(ns + "-od-" + str(index)  + unique_id)
                g.add((order1, RDF.type, ns.Order))
                g.add((order1, ns.cost, Literal(order.total_cost)))
                g.add((order1, ns.orderStatus, Literal(order.state)))

                for i, product in enumerate(order.products):
                    #  a product will be unique so no need to avoid handling it singly
                    product1 = URIRef(ns +  hashlib.sha256(product.product_name.encode()).hexdigest())
                    g.add((product1, RDF.type, ns.Product))
                    g.add((product1, ns.cost, Literal(product.product_cost)))
                    g.add((product1, ns.productName, Literal(product.product_name)))
                    g.add((order1, ns.containsProduct, product1))
                #     add customer here now
                g.add((customer1, ns.placesOrder, order1))
        # Serialize the ontology to a file (e.g., in Turtle format)
        # we inference data now
        # Add rules (using SPARQL Inferencing) - Example rules
        # Rule 1: If a customer has an order and that order is shipped, the customer is a "valued customer".
        # rule1 = """
        # PREFIX ecom: <http://example.org/ecommerce#>
        # PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        # PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        #
        # CONSTRUCT {
        #   ?customer ecom:isValuedCustomer true .
        # }
        # WHERE {
        #   ?customer ecom:placesOrder ?order .
        #   ?order ecom:orderStatus "delivered" .
        # }
        # """
        # g.parse(data=rule1, format="n3")  # Parse the rule (N3 format is common

        g.serialize(destination="datafiles/ecommerce_ontology.ttl", format="turtle")
        print("Ontology created and saved to 'ecommerce_ontology.ttl'.")
