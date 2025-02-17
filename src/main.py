import os
from src.infrastructure.data_lake_paths import DataLakePaths
from src.domain.geolocation_service import GeoLocationService
from src.application.etl_process import GeoLocationETL

if __name__ == "__main__":
    data_lake = DataLakePaths()
    geo_service = GeoLocationETL()
    etl_process = GeoLocationService()

    input_csv_path = os.path.join(data_lake.raw_path, 'input_addresses.csv')
    processed_file = etl_process.process_addresses(input_csv_path)
    print(f"Processamento concluído. Arquivo salvo em: {processed_file}")