#Realizando os import necessarios
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import split, regexp_extract
from pyspark.sql.functions import col

#Lendo o arquivo dentro do hdfs
sc = SparkContext()
sqlContext= SQLContext(sc)
log_nasa = sqlContext.read.text("hdfs:///tmp/log_nasa/")

#Formatando o arquivo lido, para ficar no formato de Host,Timestamp,URL,codeHTTP,byte
log_nasa_format = log_nasa.select(regexp_extract('value', r'^([^\s]+\s)', 1).alias('host'),
regexp_extract('value', r'^.*\[(\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} -\d{4})]', 1).alias('timestamp'),
regexp_extract('value', r'^.*"\w+\s+([^\s]+)\s+HTTP.*"', 1).alias('URL'),
regexp_extract('value', r'^.*"\s+([^\s]+)', 1).cast('integer').alias('codeHTTP'),
regexp_extract('value', r'^.*\s+(\d+)$', 1).cast('integer').alias('byte'))

#Agrupando os dados por host, realizando um count e retornando apenas o host que possuem uma unica contagem
log_nasa_format.groupBy('host').count().filter('count = 1').select('host').show()

#Realizando a contagem de quantos erros 404 foram apresentados no log
log_nasa_format.groupBy('codeHTTP').count().filter('codeHTTP = "404"').show()

#Mostrando o top 5 de URL que causaram o erro 404
log_nasa_format.filter('codeHTTP = "404"').groupBy('URL').count().sort(col("count").desc()).show(5, truncate=False)

#Mostrando a quantidade de error 404 por dia
log_nasa_format.filter('codeHTTP = "404"').groupBy(log_nasa_format.timestamp.substr(1,11).alias('day')).count().show()

#Realizando a contagem do total de bytes no arquivo
log_nasa_format.select('byte').groupBy().sum().show()
