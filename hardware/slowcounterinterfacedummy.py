# -*- coding: utf-8 -*-

from core.Base import Base
from hardware.slowcounterinterface import SlowCounterInterface
from collections import OrderedDict
import random
import time

import numpy as np

class slowcounterinterfacedummy(Base,SlowCounterInterface):
    """This is the Interface class to define the controls for the simple 
    microwave hardware.
    """
    
    def __init__(self, manager, name, config, **kwargs):
        Base.__init__(self, manager, name, configuation=config)
        self._modclass = 'niinterface'
        self._modtype = 'slowcounterinterface'

        self.connector['out']['counter'] = OrderedDict()
        self.connector['out']['counter']['class'] = 'slowcounterinterface'
        
        self.logMsg('The following configuration was found.', 
                    messageType='status')
                    
        # checking for the right configuration
        for key in config.keys():
            self.logMsg('{}: {}'.format(key,config[key]), 
                        messageType='status')
    
        if 'clock_frequency' in config.keys():
            self._clock_frequency=config['clock_frequency']
        else:
            self._clock_frequency=100
            self.logMsg('No clock_frequency configured tanking 100 Hz instead.', \
            messageType='warning')
            
        if 'samples_number' in config.keys():
            self._samples_number=config['samples_number']
        else:
            self._samples_number=10
            self.logMsg('No samples_number configured tanking 10 instead.', \
            messageType='warning')
            
    
    def set_up_clock(self, clock_frequency = None, clock_channel = None):
        """ Configures the hardware clock of the NiDAQ card to give the timing. 
        <blank line>
        @param float clock_frequency: if defined, this sets the frequency of the clock
        @param string clock_channel: if defined, this is the physical channel of the clock
        <blank line>
        @return int: error code (0:OK, -1:error)
        """ 
        
        if clock_frequency != None:
            self._clock_frequency = float(clock_frequency)
            
        self.logMsg('slowcounterinterfacedummy>set_up_clock', 
                    messageType='warning')
                    
        time.sleep(0.5)
        
        return 0
    
    
    def set_up_counter(self, counter_channel = None, photon_source = None, clock_channel = None):
        """ Configures the actual counter with a given clock. 
        <blank line>
        @param string counter_channel: if defined, this is the physical channel of the counter
        @param string photon_source: if defined, this is the physical channel where the photons are to count from
        @param string clock_channel: if defined, this specifies the clock for the counter
        <blank line>
        @return int: error code (0:OK, -1:error)
        """
        
        self.logMsg('slowcounterinterfacedummy>set_up_counter', 
                    messageType='warning')
                    
        time.sleep(0.5)
        
        return 0
        
        
    def get_counter(self, samples=None):
        """ Returns the current counts per second of the counter. 
        <blank line>
        @param int samples: if defined, number of samples to read in one go
        <blank line>
        @return float: the photon counts per second
        """
        
        self.logMsg('slowcounterinterfacedummy>get_counter', 
                    messageType='warning')
                    
        if samples == None:
            samples = int(self._samples_number)
        else:
            samples = int(samples)
        
        count_data = np.empty((samples,), dtype=np.uint32) # count data will be written here in the NumPy array
        
        for i in range(samples):
            count_data[i] = random.uniform(0, 1e6)
            
        time.sleep(1./self._clock_frequency)
        
        return count_data
    
    def close_counter(self):
        """ Closes the counter and cleans up afterwards. 
        <blank line>
        @return int: error code (0:OK, -1:error)
        """
        
        self.logMsg('slowcounterinterfacedummy>set_up_clock', 
                    messageType='warning')
        return 0
        
    def close_clock(self,power=0):
        """ Closes the clock and cleans up afterwards. 
        <blank line>
        @return int: error code (0:OK, -1:error)
        """
        
        self.logMsg('slowcounterinterfacedummy>set_up_clock', 
                    messageType='warning')
        return 0