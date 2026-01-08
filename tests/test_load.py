import os
import pandas as pd
from load import carregar_dados

def test_carregar_dados_cria_arquivo(tmp_path):
    df = pd.DataFrame({
        "nome": ["Ana"],
        "conta": ["123"],
        "cartao": ["****"],
        "mensagem": ["Teste"]
    })

    destino = tmp_path / "saida.csv"
    carregar_dados(df, str(destino))

    assert os.path.exists(destino)
