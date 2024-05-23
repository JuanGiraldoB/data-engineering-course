(SELECT 'name', 'rating', 'region' FROM ratings)
UNION
SELECT * FROM ratings
INTO OUTFILE 'C:/Users/Max/work/jd/data_enginieering_zoomcamp/de_specialization_duke/scripting_with_python_and_sql_for_de/week4/sql_scripts/table.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'