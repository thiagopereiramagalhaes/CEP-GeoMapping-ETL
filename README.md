# CEP-GeoMapping-ETL
Pipeline ETL para conversão de CEPs em endereços completos usando a API do Geopy. O projeto processa dados geográficos de arquivos CSV, armazena os resultados em um Data Lake estruturado.

## Estrutura do Projeto

- `datasets/raw/` → Contém os arquivos de entrada brutos.
- `datasets/processed/` → Contém os dados já tratados e processados.
- `datasets/curated/` → Contém os dados refinados prontos para uso.
- `src/domain/` → Implementação da lógica de negócio (Serviço de Geolocalização).
- `src/application/` → Processamento ETL.
- `src/infrastructure/` → Configuração e manipulação de diretórios.
- `tests/` → Testes automatizados.

## Como Executar

1. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```
2. Execute o script principal:
    ```sh
    python src/main.py
    ```

## Dependências

- `geopy`
- `pandas`
