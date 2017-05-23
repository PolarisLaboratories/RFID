# Replace with the address of the reader plugged into a PC
PC_LINKED_READER = '\x61\xE7\x68'

# Receive pings from tags
def tagPing(address):
    # Read signal
    lq = getLq()

    #Send tag id, signal, reader id to reader connected to server (via mesh network)
    rpc(PC_LINKED_READER, 'tagPingAggregate', address, lq, localAddr())