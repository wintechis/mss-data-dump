from rdflib import Dataset, RDF, URIRef
from rdflib.plugins.sparql.results.csvresults import CSVResultSerializer
from sys import stdout

f = open("dump.csv", "w")

q = """
PREFIX : <http://arena2036.example.org/>
PREFIX ldp: <http://www.w3.org/ns/ldp#>
PREFIX st: <http://127.0.1.1:8080/stations/>
PREFIX tr: <http://127.0.1.1:8080/transporters/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?solderingStation1Status ?solderingStation1Recipe ?solderingStation1TaskCount ?solderingStation1AffordanceCount ?solderingStation1InputProductCount ?solderingStation1OutputProductCount
       ?solderingStation1LocationX1 ?solderingStation1LocationX2 ?solderingStation1LocationY1 ?solderingStation1LocationY2
       ?memoryStorageStation1Status ?memoryStorageStation1Recipe ?memoryStorageStation1TaskCount ?memoryStorageStation1AffordanceCount ?memoryStorageStation1InputProductCount ?memoryStorageStation1OutputProductCount
       ?memoryStorageStation1LocationX1 ?memoryStorageStation1LocationX2 ?memoryStorageStation1LocationY1 ?memoryStorageStation1LocationY2
       ?cpuStorageStation1Status ?cpuStorageStation1Recipe ?cpuStorageStation1TaskCount ?cpuStorageStation1AffordanceCount ?cpuStorageStation1InputProductCount ?cpuStorageStation1OutputProductCount
       ?cpuStorageStation1LocationX1 ?cpuStorageStation1LocationX2 ?cpuStorageStation1LocationY1 ?cpuStorageStation1LocationY2
       ?boardStorageStation1Status ?boardStorageStation1Recipe ?boardStorageStation1TaskCount ?boardStorageStation1AffordanceCount ?boardStorageStation1InputProductCount ?boardStorageStation1OutputProductCount
       ?boardStorageStation1LocationX1 ?boardStorageStation1LocationX2 ?boardStorageStation1LocationY1 ?boardStorageStation1LocationY2
       ?fastTransporter1Status ?fastTransporter1ProductCount ?fastTransporter1LocationX ?fastTransporter1LocationY
WHERE {
  GRAPH st:solderingStation1 {
    st:solderingStation1 :status ?solderingStation1Status ;
      :locationX1 ?solderingStation1LocationX1 ;
      :locationX2 ?solderingStation1LocationX2 ;
      :locationY1 ?solderingStation1LocationY1 ;
      :locationY2 ?solderingStation1LocationY2 ;
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
      :locationX1 ?memoryStorageStation1LocationX1 ;
      :locationX2 ?memoryStorageStation1LocationX2 ;
      :locationY1 ?memoryStorageStation1LocationY1 ;
      :locationY2 ?memoryStorageStation1LocationY2 ;
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
      :locationX1 ?cpuStorageStation1LocationX1 ;
      :locationX2 ?cpuStorageStation1LocationX2 ;
      :locationY1 ?cpuStorageStation1LocationY1 ;
      :locationY2 ?cpuStorageStation1LocationY2 ;
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

  GRAPH st:boardStorageStation1 {
    st:boardStorageStation1 :status ?boardStorageStation1Status ;
      :locationX1 ?boardStorageStation1LocationX1 ;
      :locationX2 ?boardStorageStation1LocationX2 ;
      :locationY1 ?boardStorageStation1LocationY1 ;
      :locationY2 ?boardStorageStation1LocationY2 ;
      ldp:contains ?boardStorageStation1PropertyContainer .
  }
  GRAPH ?boardStorageStation1PropertyContainer {
    ?boardStorageStation1PropertyContainer a :PropertyContainer ;
      ldp:contains ?boardStorageStation1RecipeResource .
  }
  GRAPH ?boardStorageStation1RecipeResource {
    ?boardStorageStation1RecipeResource rdf:value ?boardStorageStation1Recipe .
  }
  {
    SELECT (COUNT(?boardStorageStation1Affordances) AS ?boardStorageStation1AffordanceCount)
    WHERE {
      GRAPH st:boardStorageStation1 {
        st:boardStorageStation1 :affords ?boardStorageStation1Affordances .
      }
    }
  }
  {
    SELECT (COUNT(?boardStorageStation1Tasks) AS ?boardStorageStation1TaskCount)
    WHERE {
      GRAPH st:boardStorageStation1 {
        st:boardStorageStation1 ldp:contains ?boardStorageStation1TaskContainer .
      }
      GRAPH ?boardStorageStation1TaskContainer {
        ?boardStorageStation1TaskContainer a :TaskContainer .
        OPTIONAL {
          ?boardStorageStation1TaskContainer ldp:contains ?boardStorageStation1Tasks .
        }
      }
    }
  }
  {
    SELECT (COUNT(?boardStorageStation1InputProducts) AS ?boardStorageStation1InputProductCount)
    WHERE {
      GRAPH st:boardStorageStation1 {
        st:boardStorageStation1 :inputPort ?boardStorageStation1InputPort .

        ?boardStorageStation1InputPort :products ?boardStorageStation1InputProducts .
      }
    }
  }
  {
    SELECT (COUNT(?boardStorageStation1OutputProducts) AS ?boardStorageStation1OutputProductCount)
    WHERE {
      GRAPH st:boardStorageStation1 {
        st:boardStorageStation1 :outputPort ?boardStorageStation1OutputPort .

        ?boardStorageStation1OutputPort :products ?boardStorageStation1OutputProducts .
      }
    }
  }

  GRAPH tr:fastTransporter1 {
    tr:fastTransporter1 :status ?fastTransporter1Status ;
      :locationX ?fastTransporter1LocationX ;
      :locationY ?fastTransporter1LocationY .
  }
  {
    SELECT (COUNT(?fastTransporter1Products) AS ?fastTransporter1ProductCount)
    WHERE {
      GRAPH tr:fastTransporter1 {
        tr:fastTransporter1 :products ?fastTransporter1Products .
      }
    }
  }
}
"""

for i in range(0,70):
  g = Dataset()
  g.parse("rdf/modularSmartphone-{}.trig".format(i), format="trig")
  serializer = CSVResultSerializer(g.query(q))
  serializer.serialize(f)
f.close()

f = open("dump.csv", "r")
lines = f.readlines()[1::2]
for i in range(0, len(lines)):
  lines[i] = str(i) + "," + lines[i].replace("http://arena2036.example.org/", "").replace("http://127.0.1.1:8080/recipes/", "")
f.close()

f = open("dump.csv", "w")
f.write("step,solderingStation1Status,solderingStation1Recipe,solderingStation1TaskCount,solderingStation1AffordanceCount,solderingStation1InputProductCount,solderingStation1OutputProductCount,solderingStation1LocationX1,solderingStation1LocationX2,solderingStation1LocationY1,solderingStation1LocationY2,memoryStorageStation1Status,memoryStorageStation1Recipe,memoryStorageStation1TaskCount,memoryStorageStation1AffordanceCount,memoryStorageStation1InputProductCount,memoryStorageStation1OutputProductCount,memoryStorageStation1LocationX1,memoryStorageStation1LocationX2,memoryStorageStation1LocationY1,memoryStorageStation1LocationY2,cpuStorageStation1Status,cpuStorageStation1Recipe,cpuStorageStation1TaskCount,cpuStorageStation1AffordanceCount,cpuStorageStation1InputProductCount,cpuStorageStation1OutputProductCount,cpuStorageStation1LocationX1,cpuStorageStation1LocationX2,cpuStorageStation1LocationY1,cpuStorageStation1LocationY2,boardStorageStation1Status,boardStorageStation1Recipe,boardStorageStation1TaskCount,boardStorageStation1AffordanceCount,boardStorageStation1InputProductCount,boardStorageStation1OutputProductCount,boardStorageStation1LocationX1,boardStorageStation1LocationX2,boardStorageStation1LocationY1,boardStorageStation1LocationY2,fastTransporter1Status,fastTransporter1ProductCount,fastTransporter1LocationX,fastTransporter1LocationY\n")
f.write("".join(lines))
f.close()