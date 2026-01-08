import pandas as pd

REQUIRED_COLUMNS = {"nome", "conta", "cartao"}

def validar_dataframe(df: pd.DataFrame) -> None:
    if not REQUIRED_COLUMNS.issubset(set(df.columns)):
        raise ValueError("Arquivo de entrada inválido: colunas obrigatórias ausentes.")
    if df.isnull().any().any():
        raise ValueError("Arquivo de entrada contém valores nulos.")

def extrair_dados(caminho: str = "data/input/usuarios.csv") -> pd.DataFrame:
    try:
        df = pd.read_csv(caminho)
        validar_dataframe(df)
        return df
    except FileNotFoundError:
        raise FileNotFoundError("Arquivo de entrada não encontrado.")
