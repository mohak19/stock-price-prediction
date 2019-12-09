from import_dataset import importer
from lstm import lstm_model
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = importer()
    #plot
    plt.figure(figsize=(16,8))
    plt.plot(df['Close'], label='Close Price history')
    lstm_model(df)