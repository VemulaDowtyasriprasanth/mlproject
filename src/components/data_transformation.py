import sys 
import os 
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.logger import logging
from src.exception import CustomException


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join("artifacts", "preprocessor_obj.pkl")
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    def get_data_transformer_object(self):
        try:
            numerical_columns=['writing_score','reading_score']
            categorical_columns=[
                "gender",
                "race_ethinicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            
        except:
            pass