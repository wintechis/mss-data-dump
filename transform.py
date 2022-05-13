from rdflib import Dataset, RDF, URIRef
from rdflib.plugins.sparql.results.csvresults import CSVResultSerializer
from sys import stdout

g = Dataset()
g.parse("rdf/modularSmartphone-70.trig", format="trig")

q = """
PREFIX : <http://arena2036.example.org/>
PREFIX ldp: <http://www.w3.org/ns/ldp#>
PREFIX st: <http://127.0.1.1:8080/stations/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?solderingStation1Status ?solderingStation1Recipe ?solderingStation1TaskCount ?solderingStation1AffordanceCount ?solderingStation1InputProductCount ?solderingStation1OutputProductCount
       ?memoryStorageStation1Status ?memoryStorageStation1Recipe ?memoryStorageStation1TaskCount ?memoryStorageStation1AffordanceCount ?memoryStorageStation1InputProductCount ?memoryStorageStation1OutputProductCount
       ?cpuStorageStation1Status ?cpuStorageStation1Recipe ?cpuStorageStation1TaskCount ?cpuStorageStation1AffordanceCount ?cpuStorageStation1InputProductCount ?cpuStorageStation1OutputProductCount
WHERE {
  GRAPH st:solderingStation1 {
    st:solderingStation1 :status ?solderingStation1Status ;
      ldp:contains ?solderingStation1PropertyContainer .
  }
  GRAPH ?solderingStation1PropertyContainer {
    ?solderingStation1PropertyContainer a :PropertyContainer ;
      ldp:contains ?solderingStation1RecipeResource .
  }
  GRAPH ?solderingStation1RecipeResource {
    ?solderingStation1RecipeResource rdf:value ?solderingStation1Recipe .
  }
  {
    SELECT (COUNT(?solderingStation1Affordances) AS ?solderingStation1AffordanceCount)
    WHERE {
      GRAPH st:solderingStation1 {
        st:solderingStation1 :affords ?solderingStation1Affordances .
      }
    }
  }
  {
    SELECT (COUNT(?solderingStation1Tasks) AS ?solderingStation1TaskCount)
    WHERE {
      GRAPH st:solderingStation1 {
        st:solderingStation1 ldp:contains ?solderingStation1TaskContainer .
      }
      GRAPH ?solderingStation1TaskContainer {
        ?solderingStation1TaskContainer a :TaskContainer .
        OPTIONAL {
          ?solderingStation1TaskContainer ldp:contains ?solderingStation1Tasks .
        }
      }
    }
  }
  {
    SELECT (COUNT(?solderingStation1InputProducts) AS ?solderingStation1InputProductCount)
    WHERE {
      GRAPH st:solderingStation1 {
        st:solderingStation1 :inputPort ?solderingStation1InputPort .

        ?solderingStation1InputPort :products ?solderingStation1InputProducts .
      }
    }
  }
  {
    SELECT (COUNT(?solderingStation1OutputProducts) AS ?solderingStation1OutputProductCount)
    WHERE {
      GRAPH st:solderingStation1 {
        st:solderingStation1 :outputPort ?solderingStation1OutputPort .

        ?solderingStation1OutputPort :products ?solderingStation1OutputProducts .
      }
    }
  }

  GRAPH st:memoryStorageStation1 {
    st:memoryStorageStation1 :status ?memoryStorageStation1Status ;
      ldp:contains ?memoryStorageStation1PropertyContainer .
  }
  GRAPH ?memoryStorageStation1PropertyContainer {
    ?memoryStorageStation1PropertyContainer a :PropertyContainer ;
      ldp:contains ?memoryStorageStation1RecipeResource .
  }
  GRAPH ?memoryStorageStation1RecipeResource {
    ?memoryStorageStation1RecipeResource rdf:value ?memoryStorageStation1Recipe .
  }
  {
    SELECT (COUNT(?memoryStorageStation1Affordances) AS ?memoryStorageStation1AffordanceCount)
    WHERE {
      GRAPH st:memoryStorageStation1 {
        st:memoryStorageStation1 :affords ?memoryStorageStation1Affordances .
      }
    }
  }
  {
    SELECT (COUNT(?memoryStorageStation1Tasks) AS ?memoryStorageStation1TaskCount)
    WHERE {
      GRAPH st:memoryStorageStation1 {
        st:memoryStorageStation1 ldp:contains ?memoryStorageStation1TaskContainer .
      }
      GRAPH ?memoryStorageStation1TaskContainer {
        ?memoryStorageStation1TaskContainer a :TaskContainer .
        OPTIONAL {
          ?memoryStorageStation1TaskContainer ldp:contains ?memoryStorageStation1Tasks .
        }
      }
    }
  }
  {
    SELECT (COUNT(?memoryStorageStation1InputProducts) AS ?memoryStorageStation1InputProductCount)
    WHERE {
      GRAPH st:memoryStorageStation1 {
        st:memoryStorageStation1 :inputPort ?memoryStorageStation1InputPort .

        ?memoryStorageStation1InputPort :products ?memoryStorageStation1InputProducts .
      }
    }
  }
  {
    SELECT (COUNT(?memoryStorageStation1OutputProducts) AS ?memoryStorageStation1OutputProductCount)
    WHERE {
      GRAPH st:memoryStorageStation1 {
        st:memoryStorageStation1 :outputPort ?memoryStorageStation1OutputPort .

        ?memoryStorageStation1OutputPort :products ?memoryStorageStation1OutputProducts .
      }
    }
  }

  GRAPH st:cpuStorageStation1 {
    st:cpuStorageStation1 :status ?cpuStorageStation1Status ;
      ldp:contains ?cpuStorageStation1PropertyContainer .
  }
  GRAPH ?cpuStorageStation1PropertyContainer {
    ?cpuStorageStation1PropertyContainer a :PropertyContainer ;
      ldp:contains ?cpuStorageStation1RecipeResource .
  }
  GRAPH ?cpuStorageStation1RecipeResource {
    ?cpuStorageStation1RecipeResource rdf:value ?cpuStorageStation1Recipe .
  }
  {
    SELECT (COUNT(?cpuStorageStation1Affordances) AS ?cpuStorageStation1AffordanceCount)
    WHERE {
      GRAPH st:cpuStorageStation1 {
        st:cpuStorageStation1 :affords ?cpuStorageStation1Affordances .
      }
    }
  }
  {
    SELECT (COUNT(?cpuStorageStation1Tasks) AS ?cpuStorageStation1TaskCount)
    WHERE {
      GRAPH st:cpuStorageStation1 {
        st:cpuStorageStation1 ldp:contains ?cpuStorageStation1TaskContainer .
      }
      GRAPH ?cpuStorageStation1TaskContainer {
        ?cpuStorageStation1TaskContainer a :TaskContainer .
        OPTIONAL {
          ?cpuStorageStation1TaskContainer ldp:contains ?cpuStorageStation1Tasks .
        }
      }
    }
  }
  {
    SELECT (COUNT(?cpuStorageStation1InputProducts) AS ?cpuStorageStation1InputProductCount)
    WHERE {
      GRAPH st:cpuStorageStation1 {
        st:cpuStorageStation1 :inputPort ?cpuStorageStation1InputPort .

        ?cpuStorageStation1InputPort :products ?cpuStorageStation1InputProducts .
      }
    }
  }
  {
    SELECT (COUNT(?cpuStorageStation1OutputProducts) AS ?cpuStorageStation1OutputProductCount)
    WHERE {
      GRAPH st:cpuStorageStation1 {
        st:cpuStorageStation1 :outputPort ?cpuStorageStation1OutputPort .

        ?cpuStorageStation1OutputPort :products ?cpuStorageStation1OutputProducts .
      }
    }
  }
}
"""

serializer = CSVResultSerializer(g.query(q))
serializer.serialize(stdout)