#!/usr/bin/env python
# -*-coding:utf-8 -*-

# __all__ = ['getrawdatacsvColumnFormat','getrawdatafromcsvfile']

import pandas as pd
import numpy as np

def getrawdatacsvColumnFormat(datalevel=1):
    ''' 原始数据文件csv每一列的定义，目前有一档行情和五档行情两种，
    后续可以增加其他类型。
    :param datalevel: 1 表示一档行情，5 表示五档行情
    :return: 数据列定义的一个列表
    '''
    if datalevel == 1:
        cvs_columns = ['UpdateTime', 'localTime', 'LastPrice', 'BidPrice1', 'AskPrice1', 'Volume', \
                       'BidVolume1', 'AskVolume1', 'OpenInterest', 'Turnover', 'AvgPrice', 'UpdateMilisec',
                       'm_lasttime']
    elif datalevel == 5:
        cvs_columns = ['UpdateTime', 'localTime', 'LastPrice', 'BidPrice1', 'AskPrice1', 'Volume', \
                       'BidVolume1', 'AskVolume1', 'OpenInterest', 'Turnover', 'AvgPrice', 'UpdateMilisec',
                       'm_lasttime', \
                       'BidVolume2', 'BidVolume3', 'BidVolume4', 'BidVolume5', \
                       'AskVolume2', 'AskVolume3', 'AskVolume4', 'AskVolume5', \
                       'BidPrice2', 'BidPrice3', 'BidPrice4', 'BidPrice5', \
                       'AskPrice2', 'AskPrice3', 'AskPrice4', 'AskPrice5']
    else:
        cvs_columns = None

    return cvs_columns

def getrawdatafromcsvfile(filefullpath, datalevel=1):
    '''
    读取单个数据文件
    :param filefullpath: 文件的全路径，绝对路径或是相对路径均可
    :param datalevel: 1 表示一档行情，5 表示五档行情
    :return: dataframe，
    '''
    colnames = getrawdatacsvColumnFormat(datalevel)
    tempdata = None
    try:
        tempdata = pd.read_csv(filefullpath, sep=',', header=None, names=colnames)
    except:
        print('{} read failed!'.format(filefullpath))

    return tempdata


if __name__ ==  '__main__':
    print('This is dataloading main function')
    # import  datapreprocessing
    # print(help(datapreprocessing.dataloading))

