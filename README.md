# CSV_Handling
My own functions to handle csv files from scratch, returning lists or dictionaries

3 functions to deal with my CSV files with no external libraries:

csv_em_linhas_list(caminho: str) turns a csv file into a list of rows divided by columns

colunas_em_dicionarios(cabecalho,dados) given a header and data, returns a dictionary with keys being the header items and values being a list of values for each header

csv_em_dicionario(caminho: str) combines to functions to open a csv and return directly a dictionary like the previous functions (actually it uses both functions above)
