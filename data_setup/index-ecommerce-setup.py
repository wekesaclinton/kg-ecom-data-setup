from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS, OWL
import knowledge_graph_inits as kb
import knowledge_graph_import_data as data
import knowledge_graph_add_data as loader

# we start by loading the file first
kb.create_graph()
# then lets load the graph and add data to it now
g = kb.load_graph()

filepath = 'datafiles/user_data.json'  # Replace with your file path
print("We are now printing data here...")
people_data = data.load_data_from_json(filepath)
print("Lets now create a model...")
loader.add_data_to_knowledge_graph(g, people_data)
print("Done now")
