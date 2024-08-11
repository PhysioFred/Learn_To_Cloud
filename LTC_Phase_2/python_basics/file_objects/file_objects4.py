import os
#change to file diretory:
os.chdir("/home/fredunix/Fred/learntocloud/LTC_Phase_2/python_basics/file_objects")

#Two methods

#Method 1: Entire file
with open ("angry-homer.jpg", "rb") as rf:
    with open ("angry-homer-copy.jpg", "wb") as wf:
        for line in rf:
            wf.write(line)

#Method 2: Small chunks at a time
with open ("angry-homer.jpg", "rb") as rf:
    with open ("angry-homer-copy.jpg", "wb") as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


#Seperator
print("-"*15)

