# Explorando IA Generativa em um Pipeline ETL com Python

[![CI](https://github.com/odevfigueiredo/etl-ia-generativa-python/actions/workflows/ci.yml/badge.svg)](https://github.com/odevfigueiredo/etl-ia-generativa-python/actions/workflows/ci.yml)

## 📌 Visão Geral

Este projeto exemplifica a construção de um pipeline ETL (Extração, Transformação e Carregamento) utilizando Python, integrando Inteligência Artificial generativa para a criação automatizada de mensagens personalizadas. O foco está em demonstrar:

- **Boas práticas de Engenharia de Dados:** modularização do código, validação de dados e tratamento de erros.  
- **Integração com IA generativa:** estruturação de prompts e simulação de respostas, com possibilidade de integração futura a APIs como OpenAI GPT.  
- **Testes automatizados:** garantia de qualidade e confiabilidade do código com `pytest`.  
- **Integração Contínua (CI):** pipeline configurada para rodar testes automaticamente via GitHub Actions.

---

## 🚀 Funcionalidades

- Extração de dados a partir de arquivos CSV estruturados.  
- Validação do schema e integridade dos dados.  
- Transformação com geração de prompts personalizados para IA.  
- Simulação da geração de mensagens personalizadas (facilmente substituível por chamada real a API de IA).  
- Carregamento dos dados processados em arquivo CSV final.  
- Testes unitários para cada etapa do pipeline.  
- Workflow de CI para execução automática dos testes.

---

## 📂 Estrutura do Projeto

```
etl-ia-generativa-python/
├── data/
│   ├── input/                # Arquivos CSV de entrada
│   └── output/               # Resultados do pipeline
├── src/                     # Código-fonte modular
│   ├── extract.py           # Extração de dados
│   ├── transform.py         # Transformação e IA
│   ├── load.py              # Carregamento de dados
│   └── main.py              # Orquestração do pipeline
├── tests/                   # Testes unitários com pytest
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
├── .github/
│   └── workflows/
│       └── ci.yml           # Configuração CI GitHub Actions
├── pyproject.toml           # Configuração do projeto e dependências
├── README.md                # Documentação do projeto
└── CHANGELOG.md             # Histórico de versões
```

---

## ⚙️ Requisitos e Instalação

- Python 3.9 ou superior  
- Dependências listadas no `pyproject.toml`

### Instalação rápida

```bash
git clone https://github.com/odevfigueiredo/etl-ia-generativa-python.git
cd etl-ia-generativa-python
pip install -e .[dev]
```

---

## 🏃‍♂️ Como Executar o Pipeline

```bash
python -m src.main
```

O pipeline realizará as etapas de Extração, Transformação (geração de mensagens) e Carregamento dos dados no arquivo `data/output/mensagens_geradas.csv`.

---

## 🧪 Testes Automatizados

Para garantir a qualidade do código, use:

```bash
pytest
```

---

## 🔄 Integração Contínua (CI)

Este projeto inclui um workflow GitHub Actions que executa os testes automaticamente a cada push ou pull request na branch `main`.
