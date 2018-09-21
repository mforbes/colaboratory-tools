"""Tools for making animations.
"""
import matplotlib.animation
from matplotlib import pyplot as plt


class MovieBase(object):
    """Base class for making animations for Colaboratory.

    To use this, inherit from MovieBase and the define either the
    generator or overload the update function.

    Attributes
    ----------
    frames : iterable
       List of "frames".  These can be anything such as a list of
       times, or frame numbers, etc.  These will be passed to the
       self.update(frame) function.
    interval : float, optional
       Delay between frames in milliseconds. Defaults to 50
    repeat : bool, optional
       Controls whether the animation should repeat when the sequence
       of frames is completed. Defaults to False. 
    FuncAnimation_args : dict, optional
       Additional arguments to pass to FuncAnimation.

    References
    ----------
    * https://medium.com/lambda-school-machine-learning/making-animations-work-in-google-colaboratory-new-home-for-ml-prototyping-c6147186ae75
    """
    fig = None
    interval = 50
    repeat = False
    blit = False
    FuncAnimation_args = {}
    
    def __init__(self, frames, **kw):
        self.frames = frames
        self.FuncAnimation_args = kw

    def update(self, frame):
        """Update the plot with the specified frame.

        If self.blit is True, then this must return a list of modified
        artists.  

        This is the only function you need to define.
        """

    ######################################################################
    # Optional functions
    def initial_frame(self):
        """Draw the initial frame."""
        return self.update(self.frames[0])
  
    def show_animation(self):
        if self.fig is None:
            self.fig = plt.figure(figsize=(10, 5))
        anim = matplotlib.animation.FuncAnimation(
            self.fig, self.update,
            init_func=getattr(self, 'initial_frame', None),
            frames=self.frames, interval=self.interval,
            repeat=self.repeat, blit=self.blit,
            **self.FuncAnimation_args)
        plt.close('all')
        matplotlib.rc('animation', html='jshtml')
        return anim
  
    @property
    def anim(self):
        """Return the current animation."""
        return self.show_animation()
