import os
import pandas as pd

def carregar_dados(df: pd.DataFrame, destino: str = "data/output/mensagens_geradas.csv") -> None:
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    df.to_csv(destino, index=False)
