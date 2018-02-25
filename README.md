# pyspark-NASA_loganalyzer

Para o script para analisar os log de dados da NASA foram utilizadas bibliotecas externas como:
   - pyspark
   - sparksql
   - pyspark.sql

Script:
   - LogAnalyzer.py
      - Script feito para realizar análise de logs de um servidor apache, o script busca um arquivo armazenado no HDFS e depois retonra as informações abaixo: <br /> 
         -- Número de hosts únicos. <br /> -- O total de erros 404. <br /> -- Os 5 URLs que mais causaram erro 404. <br /> -- Quantidade de erros 404 por dia. <br /> -- O total de bytes retornados.
