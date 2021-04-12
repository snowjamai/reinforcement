import numpy as np
import tensorflow as tf
import tensorflow.keras.backend as K
import matplotlib.pyplot as plt

from a2c_actor import Actor
from a2c_critic import Critic

class A2Cagent(object):
    def __init__(self,env):
        self.sess = tf.Session()
        tf.Sess