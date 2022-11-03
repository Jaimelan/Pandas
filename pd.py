#!/usr/bin/python3

import readline
import pandas as pd
from matplotlib import pyplot as plt

import palmerpenguins


palmerpenguins.load_penguins()

def main():
    print("Vuelta a python para pandas bby")
    # Dictionary one
    d = {'col1': [1, 2], 'col2': [3, 4]}
    
    df = pd.DataFrame(data=d)
    
    print(df)
    
    col3 = [1,4]
    
    
    df['col3'] = col3
    
    plt.boxplot(df)
    plt.show()
    
    
    # Carga de datos externos desde .txt:
    with open("data.txt", "r") as data:
        d_2 = eval(data.readline())

    df_2 = pd.DataFrame(data=d_2)
    
    print(df_2)
    input("Any key to end")
    
    
if __name__ == "__main__":
    main()