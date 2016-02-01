"""Module that provides convenience for loading data from a YAML
configuration file.

config_loader
==============

The *config_loader* ensures that additional languages can be supported by
simply modifying the `config.yaml` file.
"""
import os
from typing import AnyStr

import yaml


def get_config(config_key: str) -> [AnyStr]:
    """Retrieves the configuration list for a given config_key.

    :param config_key: The key to that target configuration list.
    :return: A configuration list for the given configuration key.
    """
    current_dir = os.path.dirname(__file__)
    config_file = os.path.join(current_dir, 'config.yaml')

    with open(config_file) as f:
        conf = yaml.load(f)
        return conf[config_key]
