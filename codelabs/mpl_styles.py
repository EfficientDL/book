"""Set of utility functions to better style Matplotlib plots in Colab.

Utility functions and better default styles for plotting in Colab using
Matplotlib.

Please run setup.sh to install the fonts.
"""

import os
import subprocess
import tempfile

import cycler
from IPython import display
import matplotlib as mpl
from matplotlib import font_manager
import matplotlib.pyplot as plt
from pandas import plotting

# Default dpi for plots. These are large but look good on modern 'retina'
# displays and when copied into presentations and docs.
_FIGURE_DPI = 288
# See options here: https://matplotlib.org/gallery/color/colormap_reference.html
_PLOT_DEFAULT_CMAP = 'Set2'
_PLOT_TEXT_COLOR = '#444444'
_PLOT_TICK_COLOR = '#666666'
_FONT_PARENT_DIR = 'fonts'
_FONT_DIR_NAMES = ['Roboto', 'Noto_Sans', 'Poppins']


def import_fonts(font_path: str) -> None:
  """Import fonts stored locally for use in Colab.

  Args:
    font_path: Path to either a directory that contains .ttf fonts or to a 
      specific .ttf font file.
  """
  if os.path.isdir(font_path):
    font_files = font_manager.findSystemFonts(fontpaths=font_path)
  else:
    # Assume the path points to a file if it's not a directory.
    font_files = [font_path]

  # Add fonts to default font manager.
  for font_file in font_files:
    font_manager.fontManager.addfont(font_file)


def import_default_fonts() -> None:
  """Register a set of default fonts with Matplotlib."""
  for font_path in _FONT_DIR_NAMES:
    import_fonts(os.path.join(_FONT_PARENT_DIR, font_path))


def set_default_styles(retina: bool = True) -> None:
  """Set Matplotlib styles for plots.

  Sets better default styles for Matplotlib-based plots.
  See all options here:
    https://matplotlib.org/tutorials/introductory/customizing.html#a-sample-matplotlibrc-file

  To override any of these settings, just change the rcParams value in Colab
  after you run this function, e.g.:
    mpl.rcParams['font.size'] = 9.0

  Args:
    retina: whether to use IPython's 'retina' InlineBackend setting. This can
      make the plots smaller (and sometimes slightly blurry) inlined in Colab
      but the plot regains its actual size and resolution when copied, saved or
      opened in a new tab. This setting is nice in Colab because it allows your
      plots to be really high resolution but shows them at a reasonable size
      inlined in Colab. Note, when using this setting and saving figures, you
      might want to double the dpi via `fig.savefig(..., dpi=fig.dpi*2)`.
  """
  # Register Pandas formatters and converters with Matplotlib to help with
  # plotting timeseries data stored in a Pandas DataFrame.
  plotting.register_matplotlib_converters()

  # Import and register fonts with Matplotlib so we can use them.
  import_default_fonts()

  if retina:
    dpi = _FIGURE_DPI // 2
    display.set_matplotlib_formats('retina')
  else:
    dpi = _FIGURE_DPI

  mpl_styles = {
      'axes.axisbelow': True,
      'axes.edgecolor': _PLOT_TICK_COLOR,
      'axes.grid': True,
      'axes.labelcolor': _PLOT_TEXT_COLOR,
      # Set default color palette.
      'axes.prop_cycle': cycler.cycler(
          'color', mpl.cm.get_cmap(_PLOT_DEFAULT_CMAP).colors),
      'axes.spines.right': True,
      'axes.spines.top': True,
      'font.family': ['Poppins', 'Noto Sans', 'Roboto'],
      # You can scale all other text by scaling this.
      'font.size': 9.0,
      'font.weight': 'light',
      'figure.figsize': (6, 4),
      # Up the default resolution for figures.
      'figure.dpi': dpi,
      'savefig.dpi': dpi,
      'lines.linewidth': 1.25,
      'grid.color': '#EEEEEE',
      'grid.linewidth': 0.4,
      'text.color': _PLOT_TEXT_COLOR,
      'xtick.color': _PLOT_TICK_COLOR,
      'ytick.color': _PLOT_TICK_COLOR,
      'legend.borderaxespad': 1.0,
      'legend.borderpad': 0.8,
      'legend.edgecolor': '1.0',
      'legend.facecolor': '#F3F3F3',
      'legend.fontsize': 'small',
      'legend.framealpha': 0.75,
      'legend.labelspacing': 0.6,
  }

  mpl.rcParams.update(mpl_styles)
