from typing import List

import torch
from tqdm import tqdm

from chemprop.data import MoleculeDataLoader, MoleculeDataset, StandardScaler
from chemprop.models import MoleculeModel


def predict(model: MoleculeModel,
            data_loader: MoleculeDataLoader,
            disable_progress_bar: bool = False,
            scaler: StandardScaler = None) -> List[List[float]]:
    """
    Makes predictions on a dataset using an ensemble of models.

    :param model: A :class:`~chemprop.models.model.MoleculeModel`.
    :param data_loader: A :class:`~chemprop.data.data.MoleculeDataLoader`.
    :param disable_progress_bar: Whether to disable the progress bar.
    :param scaler: A :class:`~chemprop.features.scaler.StandardScaler` object fit on the training targets.
    :return: A list of lists of predictions. The outer list is molecules while the inner list is tasks.
    """
    print("Evaluating model")
    model.eval()
    print("Evaluation done")

    preds = []

    for batch in tqdm(data_loader, disable=disable_progress_bar, leave=False):
        print("Preparing batch")
        # Prepare batch
        batch: MoleculeDataset
        mol_batch, features_batch, atom_descriptors_batch, atom_features_batch, bond_features_batch = \
            batch.batch_graph(), batch.features(), batch.atom_descriptors(), batch.atom_features(), batch.bond_features()

        print("Making predictions")
        # Make predictions
        with torch.no_grad():
            print("No grad")
            batch_preds = model(mol_batch, features_batch, atom_descriptors_batch,
                                atom_features_batch, bond_features_batch)
            print("Done")

        print("CPU numpy")
        batch_preds = batch_preds.data.cpu().numpy()

        # Inverse scale if regression
        if scaler is not None:
            print("Scaler available")
            batch_preds = scaler.inverse_transform(batch_preds)

        print("Collecting")
        # Collect vectors
        batch_preds = batch_preds.tolist()
        preds.extend(batch_preds)

    return preds
