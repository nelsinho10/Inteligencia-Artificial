import pandas as pd

def get_dataframe_from_csv(filename, index_col_num):
  """Retorna un DataFrame leyendolo desde el archivo <filename>, define la columna en la posicion 
  <index_col_num> como índice de éste."""
  df = pd.read_csv(filename, index_col = index_col_num)
  return df

def get_custom_dataframe(data_dict, index_name):
  """Retorna un DataFrame a partir del diccionario <data_dict>, define la columna <index_name> como
  índice del dataframe"""

  df = pd.DataFrame(data_dict)
  df.set_index(index_name, inplace=True)
  return df

def get_first_n_rows(dataframe, n):
  """Retorna un DataFrame que contiene las primeras <n> filas de <dataframe>"""
  df = dataframe.head(n)
  return df

def get_last_n_rows(dataframe, n):
  """Retorna un DataFrame que contiene las últimas <n> filas de <dataframe>"""
  df = dataframe.tail(n)
  return df

def get_shape(dataframe):
  """Retorna una tupla con las dimensiones del DataFrame <dataframe>"""
  return dataframe.shape

def change_column_names(dataframe, new_names):
  """Retorna un DataFrame cuyas columnas han sido renombradas de acuerdo a los nombres proporcionados en 
  <new_names> que es una lista de strings."""
  dataframe.columns = new_names
  return dataframe

def count_nulls_per_column(dataframe):
  """Retorna una Serie (columna) que contiene como índice los nombres de las columnas del 
    <dataframe> y en sus datos el total de elementos de tipo null o na que se encuentran en cada una.
  """
  df = dataframe.isnull().sum()
  return df

def remove_cols_with_nulls(dataframe):
  """Retorna <dataframe> con todas las columnas que tienen datos de tipo null removidas."""
  df = dataframe.dropna(1)
  return df

def get_slice(dataframe, start, end):
  """Retorna un DataFrame formado por un grupo de filas de <dataframe>, desde la fila en la posición
  <start> hasta la fila en la posición <end> - 1"""
  df = dataframe.iloc[start:end]
  return df

def filter_by_col(dataframe, column_name, value):
  """Filtra <dataframe> retornando un DataFrame que sólo contiene las filas donde el valor de la 
  columna <column_name> es igual a <value>"""
  df = dataframe[dataframe[column_name] == value]
  return df

def fill_numeric_nulls(dataframe): 
  """Retorna <dataframe> con sus los valores numéricos faltantes sustituídos por el valor de la media de la 
  columna a la que pertenecen y los no numéricos se dejan tal como están."""
  df = dataframe.fillna(dataframe.mean())
  return df

# def get_most_correlated_cols(dataframe, umbral): 
#   """Retorna un conjunto de frozensets con los pares de columnas cuyas correlaciones positivas o negativas 
#   sean mayores o iguales a <umbral>."""

#   fz = {}
#   return fz