import pandas as pd

class GeoLocationETL:
    def __init__(self, data_lake_paths, geolocation_service):
        self.data_lake_paths = data_lake_paths
        self.geolocation_service = geolocation_service

    def process_addresses(self, input_csv):
        df = pd.read_csv(input_csv)
        df['full_address'] = df['cep'].apply(self.geolocation_service.get_address)
        output_path = self.data_lake_paths.get_processed_file('processed_addresses.csv')
        df.to_csv(output_path, index=False)
        return output_path