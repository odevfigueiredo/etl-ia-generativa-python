import pandas as pd
import pytest
from extract import validar_dataframe

def test_validar_dataframe_ok():
    df = pd.DataFrame({
        "nome": ["Ana"],
        "conta": ["123"],
        "cartao": ["****"]
    })
    validar_dataframe(df)  # não deve lançar exceção

def test_validar_dataframe_colunas_faltando():
    df = pd.DataFrame({"nome": ["Ana"]})
    with pytest.raises(ValueError):
        validar_dataframe(df)
