"""
:Author: Seth Johnson
:Date: 11-13-2023
:Description:

"""
### Import packages ###

### Class definition ###
class Television:
    """
    TODO:
    - How to manage volume when muted
        - do I save the volume? does it get reset to MIN?
    """
    ### Class Variables ###
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    ### Constructors ###
    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    ### Mutators ###
    def power(self):
        self.__status = False if self.powered() else True
    
    def mute(self):
        # Mutes and unmutes TV
        if self.powered():
            self.__muted = False if self.muted() else True

    def channel_up(self):
        # Increments tv channel value when tv is on
        if self.powered():
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                # If on maximum channel value and called again, cycles back to min channel value
                self.__channel = self.MIN_CHANNEL
    
    def channel_down(self):
        # Decrements tv channel value when tv is on.
        if self.powered():
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                # Cycles back to max channel called at min value
                self.__channel = self.MAX_CHANNEL
    
    def volume_up(self):
        # incraments tv volume when tv is on. remains at maximum when called at max value
        if self.powered():
            if self.muted():
                # automatically unmutes tv
                self.mute()
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
    
    def volume_down(self):
        # decrements tv volume when tv is on. remains at min value when called at min value
        if self.powered():
            if self.muted():
                # automatically unmutes tv
                self.mute()
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    ### Accessors ###
    def powered(self): # returns status boolean
        return self.__status

    def muted(self): # returns muted boolean
        return self.__muted

    def getVolume(self): # returns volume int value
        return 0 if self.muted() else self.__volume
        
    def getChannel(self): # returns channel value
        return self.__channel
        
    def __str__(self):
        return f"Power- {self.powered()}, Channel-{self.getChannel()}, Volume-{self.getVolume()}"
    
"""
TODO:
- create a new branch named test
- add docstrings and typehinting to television.py
- create test_television.py
    - write unit tests for each of the methods using pytest
- Commit changes to test branch
- push changes to GitHub repository
- get link of my public remote repository
"""