from SPARQLWrapper import SPARQLWrapper, POST, DIGEST

# this needs actual info
sparql = SPARQLWrapper("https://example.org/sparql")
sparql.setHTTPAuth(DIGEST)
sparql.setCredentials("some-login", "some-password")
sparql.setMethod(POST)

sparql.setQuery("""
    PREFIX dbp:  <http://dbpedia.org/resource/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    WITH <http://example.graph>
    DELETE {
       dbo:Asturias rdfs:label "Asturies"@ast
    }
    """
)

results = sparql.query()
print results.response.read()
