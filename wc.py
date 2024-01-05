import os
import sys

def getByteSize(txt):
    st = os.stat(txt)
    return st.st_size

if(sys.argv[1] == "-c"):
    print(getByteSize(sys.argv[2]),sys.argv[2])
    
if(sys.argv[1] == "-l"):
    print(getByteSize(sys.argv[2]),sys.argv[2])
    



        
    