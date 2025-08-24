from dataclasses import dataclass 



@dataclass 
class DataIngestionArtifact: 
    trained_filepath:str 
    test_filepath:str

@dataclass 
class DataValidationArtifact: 
    validation_status: bool 
    message : str 
    drift_report_filepath : str 