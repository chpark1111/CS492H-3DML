import logging
import numpy as np
import torch
import torch.optim as optim
from torch.autograd.variable import Variable
from tensorboard_logger import configure, log_value

from utils import read_config
#from Model.models import Encoder

config = read_config.Config("2dsup_config.yml")

# author's code
model_name = config.model_path.format(config.mode)
print(config.config, flush=True)
config.write_config("log/configs/{}_config.txt".format(model_name))
configure("log/tensorboard/{}".format(model_name), flush_secs=5)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler(
    'log/logger/{}.log'.format(model_name), mode='w')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

#My code
#encoder = Encoder()