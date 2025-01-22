import os
from box.exceptions import BoxValueError
import yaml
#from src.winequality_practice.logging import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from typing import List

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            #logger.info(f"reading the yaml file from {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        return ValueError
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(paths,verbose=False):
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path,exist_ok=True)
            if verbose:
                print(f"Created dirctory at {path}")

@ensure_annotations
def get_size(path=Path)->list:
    size_in_kb=round(os.path.getsize(path)/1024,2)
    return size_in_kb  

@ensure_annotations
def save_json(path:Path, data:dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        #logger.info(f"save json file at : {path}")

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    with open(path,"r") as f:
        content=json.load(f)
        #logger.info(f"loading json file from : {path}")
        return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any, path:Path):
    joblib.dump(value=data, filename=path)
    #logger.info(f"save binary file at : {path}")

@ensure_annotations
def load_bin(path:Path)->Any:
    data=joblib.load(path)
    #logger.info(f"loading binary file from : {path}")
    return data