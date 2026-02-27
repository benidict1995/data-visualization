import importlib
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#Test comment

def _import_no_show(name):
    """Import a module while stubbing out plt.show() so tests don't display GUI."""
    prev_show = plt.show
    plt.show = lambda *a, **k: None
    if name in sys.modules:
        del sys.modules[name]
    mod = importlib.import_module(name)
    plt.show = prev_show
    return mod


def test_mpl_squares_creates_line():
    mod = _import_no_show('mpl_squares')
    assert hasattr(mod, 'fig')
    assert hasattr(mod, 'ax')
    lines = mod.ax.get_lines()
    assert len(lines) == 1
    xdata, ydata = lines[0].get_data()
    assert list(xdata) == [1, 2, 3, 4, 5]
    assert list(ydata) == [1, 4, 9, 16, 25]
