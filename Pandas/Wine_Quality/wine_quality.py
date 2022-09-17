from multiprocessing.reduction import duplicate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

wine_data = pd.read_csv(r"D:\Development\GitHub\Python_Development\Pandas\Wine_Quality\winequality_data.csv")

print(wine_data.head())
print(wine_data.shape)
print(wine_data.describe())
print(wine_data["quality"].value_counts())
wine_data.rename(columns={
    "fixed acidity" : "Fixed_Acidity", "volatile acidity" : "Volatile_Acidity", "citric acid" : "Citric_Acid", "residual sugar" : "Residual_Sugar", "free sulfur dioxide" : "Free_Sulfur_Dioxide",
    "total sulfur dioxide" : "Total_Sulfur_Dioxide", "chlorides": "Chlorides", "density":"Density", "sulphates":"Sulphates", "alcohol":"Alcohol", "quality":"Quality"
}, inplace= True)

print(wine_data.describe())
print(wine_data.isnull().sum())
dupl_entr = wine_data[wine_data.duplicated()]
print("Tekrar eden verilerin sayısı: ", dupl_entr.shape)

y = wine_data.Quality
x = wine_data.drop("Quality", axis=1)

wine_data.hist(bins=10, figsize=(16,12))
plt.show()