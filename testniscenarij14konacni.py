import rdflib
import owlready2
from owlready2 import *
from rdflib import Graph, RDF
import traceback
from rdflib.plugins.parsers import notation3
def load_ontology(ontology_file):
    try:
        g = Graph()
        with open(ontology_file, 'r', encoding='utf-8') as f:
            ontology_data = f.read()
            g.parse(data=ontology_data, format='xml')
        return g
    except Exception as e:
        print("RDF datoteka ontologije nije ucitana:")
        traceback.print_exc()
        return None
def load_ttl(ttl_file):
    try:
        file_graph = Graph()
        file_graph.parse(ttl_file, format="ttl")
        return file_graph
    except Exception as e:
        print("TTL datoteka nije ucitana::")
        traceback.print_exc()
        return None
def find_missing_entities(ttl_graph, ontology_graph):
    print("Entiteti iz TTL datoteke koji nisu sukladni s ontologijom:")
    ttl_entities = set()
    ontology_entities = set()
    for s, p, o in ttl_graph:
        if isinstance(s, rdflib.URIRef):
            ttl_entities.add(s.split('/')[-1].split('#')[-1])
        if isinstance(p, rdflib.URIRef):
            ttl_entities.add(p.split('/')[-1].split('#')[-1])
        if isinstance(o, rdflib.URIRef):
            ttl_entities.add(o.split('/')[-1].split('#')[-1])
    for s, p, o in ontology_graph:
        if isinstance(s, rdflib.URIRef):
            ontology_entities.add(s.split('/')[-1].split('#')[-1])
        if isinstance(p, rdflib.URIRef):
            ontology_entities.add(p.split('/')[-1].split('#')[-1])
        if isinstance(o, rdflib.URIRef):
            ontology_entities.add(o.split('/')[-1].split('#')[-1])
    missing_entities = ttl_entities - ontology_entities
    for entity in missing_entities:
        if entity.endswith('OccupationType'):
            print('OccupationType')
        else:
            print(entity)
if __name__ == "__main__":
    ontology_file = input("Kopirajte putanju do RDF datoteke ontologije: ").strip('"')
    ttl_file = input("Kopirajte putanju do TTL datoteke za koju se zeli provjeriti uskladenost s ontologijom: ").strip('"')
    onto = load_ontology(ontology_file)
    file_graph = load_ttl(ttl_file)
    if onto is not None and file_graph is not None:
        find_missing_entities(file_graph, onto)
