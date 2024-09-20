import os

def getSize(filename):
    st = os.stat(filename)
    return st.st_size