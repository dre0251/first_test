import copy
import numpy as np
import torch.nn as nn
import torch
import torch.optim as optim
import matplotlib.pyplot as plt
import math
from torch.autograd import Variable
import torch.nn.functional as F
import os

torch.manual_seed(42)
file_name = "test.txt"

with open(file_name, "r", encoding='utf-8') as f:
    text = f.read()

print(text)