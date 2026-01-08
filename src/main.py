import logging
from extract import extrair_dados
from transform import transformar_dados
from load import carregar_dados

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

if __name__ == "__main__":
    logging.info("Iniciando pipeline ETL")
    dados = extrair_dados()
    logging.info("Extração concluída")

    dados_transformados = transformar_dados(dados)
    logging.info("Transformação concluída")

    carregar_dados(dados_transformados)
    logging.info("Carregamento concluído com sucesso")
