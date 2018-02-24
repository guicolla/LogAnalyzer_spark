# scripts_spark

Repositorio criado para armazenar scripts que utilizam o spark para a sua execução.

Para alguns scripts foram utilizadas bibliotecas externas como:
   - pyspark
   - sparksql
   - pyspark.sql

Scripts:
   - AnalisarLogs.py
      - Script feito para realizar análise de logs de um servidor apache, o script busca um arquivo armazenado no HDFS e depois retonra as informações abaixo:
      <br /> 
         -- Número de hosts únicos.
         -- O total de erros 404.
         -- Os 5 URLs que mais causaram erro 404.
         -- Quantidade de erros 404 por dia.
         -- O total de bytes retornados.
