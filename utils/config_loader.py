import yaml

class ConfigLoader():
    def __init__(self):
            self.config = self.load_config()
    def load_config(self,config_path: str = "config/config.yaml") -> dict:
        with open(config_path,"r") as config_file:
            config = yaml.safe_load(config_file)
        return config
    def __getitem__(self, key):
        return self.config[key]