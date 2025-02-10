import knowledge_graph_inits as kb
from owlrl import DeductiveClosure, RDFS_Semantics, OWLRL_Semantics

g = kb.load_graph()

# Apply OWL 2 RL reasoning
deductive_closure = DeductiveClosure(OWLRL_Semantics)
deductive_closure.expand(g)

# Print the inferred triples
print("Inferred Triples:")
for s, p, o in g:
    print(f"{s} {p} {o}")
g.serialize(destination="datafiles/ecommerce_inferred_ontology.ttl", format="turtle")