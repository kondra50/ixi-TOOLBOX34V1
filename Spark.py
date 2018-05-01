from pyspark import SparkContext, SparkConf

# logFile = 'C:\\UI\\spark.txt'  # Should be some file on your system
# sc = SparkContext("local", "Simple App")
# logData = sc.textFile(logFile).cache()
#
# numAs = logData.filter(lambda s: 'a' in s).count()
# numBs = logData.filter(lambda s: 'b' in s).count()
#
# print("Lines with a: %i, lines with b: %i" % (numAs, numBs))
conf = SparkConf().setAppName('myapp').setMaster('local')
sc = SparkContext(conf=conf)
distFile = sc.textFile("log.csv").cache()
dis1=distFile.filter(lambda line: "ERROR" in line)
numAs = distFile.filter(lambda s: 'MNAFISI' in s).count()
numBs = distFile.filter(lambda s: 'SMANSON' in s).count()
print("Lines with a: %i, lines with b: %i" % (numAs, numBs))



distFile = sc.textFile("log1.csv").cache()
dis1=distFile.filter(lambda line: "ERROR" in line)
numAs = distFile.filter(lambda s: 'MNAFISI' in s).count()
numBs = distFile.filter(lambda s: 'SMANSON' in s).count()
print("Lines with a: %i, lines with b: %i" % (numAs, numBs))



distFile = sc.textFile("log2.csv").cache()
dis1=distFile.filter(lambda line: "ERROR" in line)
numAs = distFile.filter(lambda s: 'MNAFISI' in s).count()
numBs = distFile.filter(lambda s: 'SMANSON' in s).count()
print("Lines with a: %i, lines with b: %i" % (numAs, numBs))
# data = [1, 2, 3, 4, 5]

distFile = sc.textFile("log3.csv").cache()
dis1=distFile.filter(lambda line: "ERROR" in line)
numAs = distFile.filter(lambda s: 'MNAFISI' in s).count()
numBs = distFile.filter(lambda s: 'SMANSON' in s).count()
print("Lines with a: %i, lines with b: %i" % (numAs, numBs))
# distData = sc.parallelize(data)

distFile = sc.textFile("log4.csv").cache()
dis1=distFile.filter(lambda line: "ERROR" in line)
numAs = distFile.filter(lambda s: 'MNAFISI' in s).count()
numBs = distFile.filter(lambda s: 'SMANSON' in s).count()
print("Lines with a: %i, lines with b: %i" % (numAs, numBs))



print(distFile)