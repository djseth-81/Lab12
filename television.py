"""
:Author: Seth Johnson
:Date: 11-13-2023
:Description:
This script houses the object Television to represent its basic behavior. It is called in main.py for operation.
"""

### Class definition ###
class Television:
    """
    A class representing a Television.

    Attributes
    ----------
    status : bool
        Determines if the television (tv) is powered on or not
    muted : bool
        Determines if the tv has been muted, reverting the volume value to 0
    volume : int
        Represents the volume of the tv
    channel : int
        Represents the selected channel of the tv
    
    Methods
    -------
    power():
        Toggles the status boolean to turn the tv on and off
    mute():
        Toggles the muted boolean to mute and unmute the tv. When the tv is muted, the volume is displayed as 0
    channel_up():
        Incraments the channel variable until the maximum channel value is reached, after which cycles back to the minimum channel value.
    channel_down():
        Decraments the channel variable until the minimum channel value is reached, after which it cycles to the maximum channel value
    volume_up():
        Incraments the volume variable until the maximum volume value is reached.
    volume_down():
        Decrements the volume variable until the minimum volume vaule is reached.
    powered():
        Returns the state of the status boolean
    muted():
        Returns the state of the muted boolean
    getVolume():
        Returns the integer value of volume
    getChannel():
        Returns the integer value of channel
    __str__():
        returns a formatted string which calls powered(), getChannel(), and getVolume() to display the given state of a tv object
    """

    ### Class Variables ###
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int= 0
    MAX_CHANNEL: int= 3

    ### Constructors ###
    def __init__(self) -> None:
        """
        Constructs the instance attributes for the tv object
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    ### Mutators ###
    def power(self) -> None:
        """
        Toggles the status boolean to turn the tv on and off
        """
        self.__status = False if self.powered() else True
    
    def mute(self) -> None:
        """
        Toggles the mute boolean to mute and unmute the tv.
        """
        # Mutes and unmutes TV
        if self.powered():
            self.__muted = False if self.muted() else True

    def channel_up(self) -> None:
        """
        Incraments the channel variable until the maximum channel value is reached, after which cycles back to the minimum channel value.
        """
        # Increments tv channel value when tv is on
        if self.powered():
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                # If on maximum channel value and called again, cycles back to min channel value
                self.__channel = Television.MIN_CHANNEL
    
    def channel_down(self) -> None:
        """
        Decraments the channel variable until the minimum channel value is reached, after which it cycles to the maximum channel value
        """
        # Decrements tv channel value when tv is on.
        if self.powered():
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                # Cycles back to max channel called at min value
                self.__channel = Television.MAX_CHANNEL
    
    def volume_up(self) -> None:
        """
        Incraments the volume variable until the maximum volume value is reached.
        """
        # incraments tv volume when tv is on. remains at maximum when called at max value
        if self.powered():
            if self.muted():
                # automatically unmutes tv
                self.mute()
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
    
    def volume_down(self) -> None:
        """
        Decrements the volume variable until the minimum volume vaule is reached.
        """
        # decrements tv volume when tv is on. remains at min value when called at min value
        if self.powered():
            if self.muted():
                # automatically unmutes tv
                self.mute()
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    ### Accessors ###
    def powered(self) -> bool:
        """
        Returns the state of the status boolean
        :return: self.__status
        """
        return self.__status

    def muted(self) -> bool:
        """
        Returns the state of the muted boolean
        :return: self.__muted
        """
        return self.__muted

    def getVolume(self) -> int:
        """
        Returns the integer value of volume
        :return: 0 if the tv is muted or self.__volume otherwise
        """
        return 0 if self.muted() else self.__volume
        
    def getChannel(self) -> int:
        """
        Returns the integer value of channel
        :return: self.__channel
        """
        return self.__channel
        
    def __str__(self) -> str:
        """
        Returns a formatted string which calls powered(), getChannel(), and getVolume() to display the given state of a tv object
        :return: string of the power status, channel value, and volume value
        """
        return f"Power = {self.powered()}, Channel = {self.getChannel()}, Volume = {self.getVolume()}"

""" 
-0.5pts: GitHub repository name should be python str 
-1pt: Your output statements should follow the same format as the ones provided in the main.py file comments It’s better to use Television.MIN_CHANNEL rather than self.MIN_CHANNEL (refer to the discussion video minute 12:41 on the implication of using self vs the class name when it comes to class variables). 
test_init: -2pts: Missing test Resubmit by 11/19/23 – 10pm
"""