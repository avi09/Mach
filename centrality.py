from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import functions
from graphframes import *
from pyspark.sql.functions import explode

sc=SparkContext("local", "degree.py")
sqlContext = SQLContext(sc)
sc.setLogLevel("ERROR")

def closeness(g):

    # Get list of vertices. We'll generate all the shortest paths at
    # once using this list.
    # YOUR CODE HERE
    x=g.vertices.rdd.map(lambda x:x[0])
    x=x.map(lambda x:x.encode('ascii','ignore')).collect()
    x1 = g.shortestPaths(landmarks=x)
    x1=x1.rdd
    def fn(x):
        y=str(x)
        y=y.encode('ascii','ignore')
        y=int(y)
        y=y**-1
        y=str(y)
        return y
    
    # first get all the path lengths.
    x1=x1.map(lambda x:(x[0].encode('ascii','ignore'),x[1].values()))
    # Break up the map and group by ID for summing

    
    # Sum by ID
    x1=x1.map(lambda x:(x[0],sum(x[1])))
    
    x1=x1.map(lambda x:(x[0],fn(x[1])))
    # Get the inverses and generate desired dataframe.
    x1=sqlContext.createDataFrame(x1,["id","closeness"])
    return x1
    
print("Reading in graph for problem 2.")
graph = sc.parallelize([('A','B'),('A','C'),('A','D'),
	('B','A'),('B','C'),('B','D'),('B','E'),
	('C','A'),('C','B'),('C','D'),('C','F'),('C','H'),
	('D','A'),('D','B'),('D','C'),('D','E'),('D','F'),('D','G'),
	('E','B'),('E','D'),('E','F'),('E','G'),
	('F','C'),('F','D'),('F','E'),('F','G'),('F','H'),
	('G','D'),('G','E'),('G','F'),
	('H','C'),('H','F'),('H','I'),
	('I','H'),('I','J'),
	('J','I')])
	
e = sqlContext.createDataFrame(graph,['src','dst'])
v = e.selectExpr('src as id').unionAll(e.selectExpr('dst as id')).distinct()
print("Generating GraphFrame.")
g = GraphFrame(v,e)

print("Calculating closeness.")
closeness(g).sort('closeness',ascending=False).show()
closeness(g).toPandas().to_csv("centrality_out.csv")
