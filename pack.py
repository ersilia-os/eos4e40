from src.service import load_chemprop_model
from src.service import eos4e40 as Service
import os

root = os.path.dirname(os.path.realpath(__file__))
mdl = load_chemprop_model(os.path.join(root, "model/checkpoints"))

service = Service()
service.pack('model', mdl)
service.save()
