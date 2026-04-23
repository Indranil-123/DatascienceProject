import os
import yaml
from src.DSproject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from box.exceptions import  BoxValueError


#first helper function

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns a ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise BoxValueError(f"yaml file: {path_to_yaml} is invalid")
    except Exception as e:
        raise e




##second helper Function
@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")



#third helper function
@ensure_annotations
def load_json(path:Path) ->ConfigBox:

    with open(path) as f:
        content = json.load(f)
        logger.info(f"json file: {path} loaded successfully")

    return ConfigBox(content)


@ensure_annotations
def save_model(data:any, path:Path):

    joblib.dump(value=data,filename=path)
    logger.info(f"model file {path} saved successfully")


@ensure_annotations
def load_model(path:Path) ->Any:
    """
    Loads a model from a file.
    """
    return joblib.load(path)