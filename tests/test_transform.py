import pandas as pd
from transform import transformar_dados

def test_transformar_dados_gera_mensagem():
    df = pd.DataFrame({
        "nome": ["Ana"],
        "conta": ["123"],
        "cartao": ["****"]
    })

    resultado = transformar_dados(df)

    assert "mensagem" in resultado.columns
    assert len(resultado.loc[0, "mensagem"]) > 0
