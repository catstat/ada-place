from pathlib import Path

import numpy as np
import torch


class SavedPlacement:
    def place(self, benchmark):
        path = Path(__file__).parent / 'placements' / benchmark.name / 'placement.npz'
        with np.load(path, allow_pickle=False) as saved:
            return torch.from_numpy(saved['positions'].copy())
