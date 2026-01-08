from typing import Dict
import pandas as pd

PROMPT_TEMPLATE = """
Você é um assistente de marketing de um banco digital.

Crie uma mensagem curta, profissional e personalizada para o cliente abaixo:

Nome: {nome}
Conta: {conta}
Cartão: {cartao}

Regras:
- Tom cordial e institucional;
- Não exponha dados sensíveis;
- Incentive o relacionamento com o banco;
- Mensagem com no máximo 3 frases.
"""

def gerar_prompt(registro: Dict[str, str]) -> str:
    return PROMPT_TEMPLATE.format(
        nome=registro["nome"],
        conta=registro["conta"],
        cartao=registro["cartao"],
    )

def simular_resposta_ia(prompt: str) -> str:
    # Simulação de resposta (pronta para substituir por API real)
    return (
        "Olá, agradecemos por confiar em nossos serviços. "
        "Sua conta está ativa e estamos à disposição para apoiar suas necessidades financeiras. "
        "Conte conosco sempre."
    )

def transformar_dados(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["prompt"] = df.apply(lambda row: gerar_prompt(row.to_dict()), axis=1)
    df["mensagem"] = df["prompt"].apply(simular_resposta_ia)
    return df[["nome", "conta", "cartao", "mensagem"]]
