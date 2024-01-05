import os
import sys

def getByteSize():
    st = os.stat('test.txt')
    return st.st_size



print(getByteSize())
print(sys.argv)

        
    