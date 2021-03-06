'''
  @file ann.py

  Class to benchmark the Nearpy Approximate Nearest Neighbors method.
'''

import os, sys, inspect

# Import the util path, this method even works if the path contains symlinks to
# modules.
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(
  os.path.split(inspect.getfile(inspect.currentframe()))[0], "../../util")))
if cmd_subfolder not in sys.path:
  sys.path.insert(0, cmd_subfolder)

from util import *
from nearpy import Engine
from nearpy.hashes import RandomBinaryProjections

'''
This class implements the Approximate K-Nearest-Neighbors benchmark.
'''
class NEARPY_ANN(object):
  def __init__(self, method_param, run_param):
    self.info = "NEARPY_ANN ("  + str(method_param) +  ")"

    # Assemble run model parameter.
    self.data = load_dataset(method_param["datasets"], ["csv"])
    self.data_split = split_dataset(self.data[0])

    self.build_opts = {}
    if "k" in method_param:
      self.build_opts["k"] = int(method_param["k"])

  def __str__(self):
    return self.info

  def metric(self):
    totalTimer = Timer()
    with totalTimer:
      dimension = self.data_split[0].shape[1]
      rbp = RandomBinaryProjections('rbp', 10)
      engine = Engine(dimension, lshashes=[rbp])
      for i in range(len(self.data_split[0])):
          engine.store_vector(self.data_split[0][i], 'data_%d' % i)
      for i in range(len(self.data[1])):
          v = engine.neighbours(self.data[1][i])

    metric = {}
    metric["runtime"] = totalTimer.ElapsedTime()
    return metric
