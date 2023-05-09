import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
                 MedInc:float,
                 HouseAge:float,
                 AveRooms:float,
                 AveBedrms:float,
                 Population:float,
                 AveOccup:float,
                 Latitude:str,
                 Longitude:str):
        
        self.MedInc=MedInc
        self.HouseAge=HouseAge
        self.AveRooms=AveRooms
        self.AveBedrms=AveBedrms
        self.Population=Population
        self.AveOccup=AveOccup
        self.Latitude = Latitude
        self.Longitude = Longitude

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'MedInc':[self.MedInc],
                'HouseAge':[self.HouseAge],
                'AveRooms':[self.AveRooms],
                'AveBedrms':[self.AveBedrms],
                'Population':[self.Population],
                'AveOccup':[self.AveOccup],
                'Latitude':[self.Latitude],
                'Longitude':[self.Longitude]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)
