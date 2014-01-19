"""Module that provides convenience for loading data from a YAML
configuration file.

"""
import os

import yaml


def get_config(config_key):
    current_dir = os.path.dirname(__file__)
    config_file = os.path.join(current_dir, '..', 'resources', 'config.yaml')

    with open(config_file) as f:
        conf = yaml.load(f)
        return conf[config_key]
