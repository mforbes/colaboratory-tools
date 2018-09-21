# ColaboratoryTools

Tools for working with
[Colaboratory](https://colab.research.google.com) - Jupyter Notebooks
in Google Drive.  The idea is to install this package at the start of
your Colaboratory notebook so you can access these tools.

To use, add and execute the following cell in your Colaboratory
document:

```bash
# Run this cell to install some useful packages for working with collaboratory
# See https://github.com/mforbes/colaboratory-tools for details
!pip install git+git://github.com/mforbes/colaboratory-tools.git
```

Then you can import and use the various tools.


Animation
---------

Here is how to make a simple movie:

```python
%pylab inline --no-import-all
from colaboratory_tools.animation import MovieBase

class Movie(MovieBase):
  def __init__(self):
    # Initialize figure, setting size etc.
    self.fig = plt.figure(figsize=(5, 3))
    
    # These are the frames to be drawn.  Here they are frequency
    # factors for the sine wave.
    self.frames = np.linspace(1, 5, 20)
    
    # Define any local variables and data.
    self.x = np.linspace(0, 1, 100)
    
    # Draw the artists so they can be modified.
    self._line, = plt.plot(self.x, self.get_y(1))
    self._title = plt.title("f=1")
    plt.xlabel("x")
    plt.ylabel("y")
    
  def get_y(self, f):
    """Helper function to return the computed data."""
    return np.sin(2*np.pi*self.x*f)
    
  def update(self, f):
    """Update the data and return list of artists."""
    self._line.set_data(self.x, self.get_y(f))
    self._title.set_text("f={:.2f}".format(f))
    return [self._line, self._title]
    
Movie().anim
```
