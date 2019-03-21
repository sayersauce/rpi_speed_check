'''
Created on Aug 15, 2011

@author: tomkent

Edited on March 21 2019

@editor: maxsayer
'''

import urllib2
import time
import optparse
import monotonic

def push_block_size(remote_file, block_size, block_window=1.0, telemetry=False):
    """ Grow the blocksize to a suitable value for this connection
    
    If the block is downloaded in less than block_window seconds, then double it. 
    Repeat until we have two runs in a row that take longer than block_window
    """
    f = remote_file
    
    #prime the pump
    temp = f.read(block_size)
    temp = f.read(block_size)
    temp = f.read(block_size)

    start = monotonic.monotonic_time()
    previous = start
    last = False
    second = False
    debug_data = []
    while not last and not second:
        temp = f.read(block_size)
        if len(temp)==0: #We've gotten all the file
            raise IOError("file was to short to complete setup")
        current = monotonic.monotonic_time()
        debug_data.append((current-previous, block_size))
        if(current-previous)*32 < block_window:
            multiplier = block_window / (current-previous)
            multiplier = multiplier / 16 # add in some leeway
            block_size = int(block_size * multiplier)
            if telemetry:
                print "increasing block size to: " + str(block_size) + " B"
            last = False
            second = False
        elif(current-previous) < block_window:
            block_size = block_size * 2
            if telemetry:
                print "doubling block size to: " + str(block_size) + " B"
            last = False
            second = False
        elif last:
            #TODO: if elapsed time is more than a few percent over block_window, lower block_size
            second = True
        else: 
            #TODO: if elapsed time is more than a few percent over block_window, lower block_size
            last = True
        previous = current
    debug_data.append((current-previous, block_size))
    for t,b in debug_data:
        print t,",",b
    return block_size

def speed_check(remote_file, test_seconds, block_size, output_time=0):
    average, bytes, elapsed, block_size = speed_check_info(remote_file,  
        test_seconds, block_size, output_time)
    return average

def speed_check_info(remote_file, test_seconds, block_size, output_time=0):
    start = monotonic.monotonic_time()
    bytes = 0
    previous = start
    last_output = start
    f = remote_file

    while previous < (start + test_seconds):
        temp = f.read(block_size)
        if len(temp)==0: #We've gotten all the file
            break
        bytes += block_size
        current = monotonic.monotonic_time()
            
        if (current - last_output) > output_time and output_time != 0:
            print str(bytes/(current-start)) + " KB/s"
            last_output = current
            
        previous = current
        
    finish = previous
    elapsed = finish-start
    average = bytes / elapsed
   
    return average, bytes, elapsed, block_size   
    
def Speed_Check():
    block = 1024
    test_time = 20
    message_freq = 0
    growth = False
    window = 0.5
    
    f = urllib2.urlopen('http://speedtest.wdc01.softlayer.com/downloads/test500.zip')
    block_size = push_block_size(f, block, window, growth)
    average = speed_check(f, 20, block, message_freq)
    f.close()
   
    print str(average) + ' Bps'
    print str(average/125000) + ' Mbps'
    return average
  
