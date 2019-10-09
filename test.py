import  pandas as np
import numpy as np
import  sys
from toolkit.datapreprocessing.dataloading import getrawdatafromcsvfile
from toolkit.datashow.rawdatashow import plot5levelrawdata

filefullpath = "../maininsts/sn/sn0000/20190919Tgsn200120190919.csv"
# plot2dBarTest()
rawdata = getrawdatafromcsvfile(filefullpath, 5)
plot5levelrawdata(rawdata, starttime='21:00:21', lastSeconds=10)


# plot5level2dbars(rawdata.loc[:,:])
# print(rawdata.head(5))