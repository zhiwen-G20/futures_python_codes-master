import  pandas as np
import numpy as np
import  sys

from toolkit.datapreprocessing.dataloading import getrawdatafromcsvfile
from toolkit.datashow.rawdatashow import plot5levelrawdata_bar3d, plot5levelrawdata_wireframe,plot5levelrawdata_surface,plot5levelrawdata_contour

filefullpath = "../maininsts/sn/sn0000/20190801Tgsn190920190801.csv"
# filefullpath = "../maininsts/ni/ni0000/20190801Tgni191020190801.csv"
# filefullpath = "../maininsts/rb/rb0000/20190801Tgrb191020190801.csv"
# plot2dBarTest()
rawdata = getrawdatafromcsvfile(filefullpath, 5)
# plot5levelrawdata_bar3d(rawdata, starttime='21:00:21', lastSeconds=100)
plot5levelrawdata_contour(rawdata, starttime='21:00:21', lastSeconds=100000)


# plot5level2dbars(rawdata.loc[:,:])
# print(rawdata.head(5))

