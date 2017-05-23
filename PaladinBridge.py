#######################################################
# Active RFID People / Asset Tracking System
# http://www.ns-tech.co.uk/active-rfid-tracking-system/
#######################################################

from synapse.switchboard import *

#Init
def startup():
    # Connect serial port to STDIN   
    crossConnect(DS_UART1, DS_STDIO)
    
    initUart(1, 9600) #Set UART1 to 9600 baud
    #flowControl(1, False) #Turn off flow control

    print "Reader Powered Up"

#If this is the reader connected to server, erlay any tag pings received to the seral port
def tagPingAggregate(tag_addr, lq, reader_addr):
    print bin2hex(tag_addr), ",", bin2hex(reader_addr), ",", lq

#Convert bytes to hex
def bin2hex(str):
    hex = ""
    count = len(str)
    index = 0
    while index < count:
        byte = ord(str[index])
        hex += bin2hex_nibble(byte >> 4)
        hex += bin2hex_nibble(byte)
        index += 1
    return hex

def bin2hex_nibble(nibble):
    hexStr = "0123456789ABCDEF"
    return hexStr[nibble & 0xF]


# Install event handlers
snappyGen.setHook(SnapConstants.HOOK_STARTUP, startup)
#snappyGen.setHook(SnapConstants.HOOK_STDIN, stdinHandle)