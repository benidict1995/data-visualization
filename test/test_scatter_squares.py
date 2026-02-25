import importlib
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def _import_no_show(name):
    prev_show = plt.show
    plt.show = lambda *a, **k: None
    if name in sys.modules:
        del sys.modules[name]
    mod = importlib.import_module(name)
    plt.show = prev_show
    return mod


def test_scatter_squares_points_and_axes():
    mod = _import_no_show('scatter_squares')
    assert hasattr(mod, 'fig')
    assert hasattr(mod, 'ax')
    # scatter creates a PathCollection stored in ax.collections
    cols = mod.ax.collections
    assert len(cols) >= 1
    offsets = cols[0].get_offsets()
    assert offsets.shape[0] == 1000
    first = offsets[0]
    last = offsets[-1]
    assert int(first[0]) == 1
    assert int(first[1]) == 1
    assert int(last[0]) == 1000
    assert int(last[1]) == 1000**2
    # axis limits were set explicitly in the script
    xlim = tuple(map(int, mod.ax.get_xlim()))
    ylim = tuple(map(int, mod.ax.get_ylim()))
    assert xlim == (0, 1100)
    assert ylim == (0, 1100000)
