import config
from core.ssEMnet import ssEMnet
from core.util import read_array_from_file

'''
Trains a ssEMnet to do 2D affine co-registration 
'''

X1, X2 = read_array_from_file(config.training_saved_filename)

net = ssEMnet(X1.shape[1:], X2.shape[1:],
              config.checkpoint_autoencoder_filename, config.checkpoint_ssemnet_filename)

net.train(X1, X2)
