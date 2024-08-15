
from SPARQLWrapper import SPARQLWrapper, JSON 

sparql = SPARQLWrapper(
    "http://vocabs.ardc.edu.au/repository/api/sparql/"
    "csiro_international-chronostratigraphic-chart_geologic-time-scale-2020"
)
sparql.setReturnFormat(JSON)

# gets the first 3 geological ages
# from a Geological Timescale database,
# via a SPARQL endpoint
sparql.setQuery("""
    PREFIX gts: <http://resource.geosciml.org/ontology/timescale/gts#>

    SELECT * WHERE {
        ?a a gts:Age .
    }
    ORDER BY ?a
    LIMIT 3
    """
)

try:
    ret = sparql.queryAndConvert()

    for r in ret["results"]["bindings"]:
        print(r)
except Exception as e:
    print(e)
