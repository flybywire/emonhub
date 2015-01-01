import struct

# Initialize nodes data
nodelist = {}


def check_datacode(datacode):

    # Data types & sizes (number of bytes)
    datacodes = {'b': '1', 'h': '2', 'i': '4', 'l': '4', 'q': '8', 'f': '4', 'd': '8',
                 'B': '1', 'H': '2', 'I': '4', 'L': '4', 'Q': '8', 'c': '1', '?': '1','J':3}

    # if datacode is valid return the data size in bytes
    if datacode in datacodes:
        return int(datacodes[datacode])
    # if not valid return False
    else:
        return False

# J,['30', '137', '1']
def decode(datacode, frame):
    # Ensure little-endian & standard sizes used
    e = '<'

    # set the base data type to bytes
    b = 'B'

    # get data size from data code
    s = int(check_datacode(datacode))
    print datacode[0]
    #print *frame
    
    result = struct.unpack(e + datacode[0], struct.pack(e + b*s, *frame))
    return result[0]

#        number of bytes to decode 3['30', '137', '1']
