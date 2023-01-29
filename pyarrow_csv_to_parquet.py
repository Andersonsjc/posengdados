import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from datetime import datetime


print(f'INICIO PROCESSO DE CONVERSAO')
data_dir = 'C:\\Users\\andesiqu\\Downloads\\AWS\\data'
parquet_dir = 'C:\\Users\\andesiqu\\Downloads\\AWS\\parquet_dir'
fileNames = [fileName for fileName in os.listdir(data_dir) if fileName.endswith(".txt")]
for file in fileNames:
    print(f'    {file}')
    file_parquet = file.replace('.txt','.parquet')
    #print(f'    file_parquet = {file_parquet}')
    print(f'INICIO PROCESSAMENTO DO ARQUIVO: {datetime.now()}')
    file_name_in = f'{data_dir}\\{file}'
    file_name_out = f'{parquet_dir}\\{file_parquet}'
    print(f'File IN: {file_name_in}')
    print(f'File OUT: {file_name_out}')
    #Leitura do arquivo CSV
    df = pd.read_csv(file_name_in, sep=';', encoding='latin1')
    df.to_parquet(file_name_out)
    #print(df.head(5))
    #number_of_rows = len(df.index) + 1
    #print(number_of_rows)
    print(f'CARREGADO PANDAS: {datetime.now()}')

    # Convertendo o DataFrame para o formato Parquet
    #table = pa.Table.from_pandas(df)
    #pq.write_table(table, file_name_out)

    print(f'FIM PROCESSAMENTO DO ARQUIVO: {datetime.now()}\n\n')

print(f'FIM PROCESSO DE CONVERSAO')