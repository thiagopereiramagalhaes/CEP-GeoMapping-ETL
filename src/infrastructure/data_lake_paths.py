import os

class DataLakePaths:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.raw_path = os.path.join(self.base_path, '../../datasets/raw')
        self.processed_path = os.path.join(self.base_path, '../../datasets/processed')
        self.curated_path = os.path.join(self.base_path, '../../datasets/curated')

        os.makedirs(self.raw_path, exist_ok=True)
        os.makedirs(self.processed_path, exist_ok=True)
        os.makedirs(self.curated_path, exist_ok=True)

    def get_processed_file(self,filename):
        return os.path.join(self.processed_path, filename)
    
    def get_curated_file(self, filename):
        return os.path.join(self.curated_path, filename)