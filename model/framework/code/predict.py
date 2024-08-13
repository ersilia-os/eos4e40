"""Loads a trained chemprop model checkpoint and makes predictions on a dataset."""
import os
import sys

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)

from chemprop.train import chemprop_predict

if __name__ == "__main__":
    chemprop_predict()
