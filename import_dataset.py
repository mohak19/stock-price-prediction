def importer():
    #import packages
    import pandas as pd
    import numpy as np

    #to plot within notebook
    import matplotlib.pyplot as plt

    #setting figure size
    from matplotlib.pylab import rcParams
    rcParams['figure.figsize'] = 20,10

    #for normalizing data
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))

    #read the file
    df = pd.read_csv('C:/ml projects/stock prediction own/data/NSE-TATAGLOBAL11.csv')

    #setting index as date
    df['Date'] = pd.to_datetime(df.Date,format='%Y-%m-%d')
    df.index = df['Date']
    return df