from src.service import load_chemprop_model
from src.service import Service
from src.service import CHECKPOINTS_BASEDIR, FRAMEWORK_BASEDIR

import os

root = os.path.dirname(os.path.realpath(__file__))
mdl = load_chemprop_model(
    os.path.join(root, "model", FRAMEWORK_BASEDIR),
    os.path.join(root, "model", CHECKPOINTS_BASEDIR),
)

service = Service()
service.pack("model", mdl)
service.save()
