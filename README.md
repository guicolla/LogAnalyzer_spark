# LogAnalyzer_spark
This project consists of code to do an analysis of an apache log in my test I use the NASA Log, the analysis consists in:
* The Number of unique hosts
* Total of 404 error
* Top 5 URL caused by 404 error
* Amount of 404 error per day
* Total of bytes

## Getting Started
I use the Hortonworks sandbox to do a development of my program
Sandbox: https://br.hortonworks.com/products/sandbox/

### Prerequisites
You  need an Apache Log file, in my case i use the Nasa Log you can find in the link below and a Spark 2.0+
Nasa Log: http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html

### Installing
```
git clone https://github.com/guicolla/LogAnalyzer_spark.git
```
After do git clone you need to put the file into hdfs
```
hdfs dfs -copyFromLocal local_path/* /tmp/log_nasa/
```
After this just execute the code
```
spark-submit LogAnalyzer.py
```
