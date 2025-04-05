from Swayam_TextSummarization.logging import logger
from Swayam_TextSummarization.config.configuration import ConfigurationManager
from Swayam_TextSummarization.components.data_validation import DataValidation

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()