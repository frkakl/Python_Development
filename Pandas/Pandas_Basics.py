import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

#Series,Lists
"""
list_1 = ["a", "b", "c", "d"]
labels = [1,2,3,4]
ser_1 = pd.Series(data = list_1, index = labels) # list_1 listesindeki verileri, labes listesindeki sayılara indexleyip SERİ haline getiriyor.

print(ser_1)

arr_1 = np.array([1,2,3,4]) #liste oluşturur.
ser_2 = pd.Series(arr_1)    #listeyi SERİ haline getirir.
print(ser_2)

print(ser_2 + ser_2) 

print(ser_2 - ser_2)

print(ser_2 * ser_2)

print(ser_2 / ser_2)


print(np.exp(ser_2)) #exponential e^x

dict_1 = {"First Name": "Ömer", "Last Name": "Akal", "Age": 20} #Sözlük formatı denilen bu method ile ":" kullanarak veriyi isime indexliyor.
ser_3 = pd.Series(dict_1, name = "Who am I?") # Sözlük SERİ haline getiriyor ve isim veriyor.
print(ser_3)
"""

#Data Frames
"""
arr_2 = np.random.randint(31,62, size=(4,3)) # 4e 3 büyüklüğünde, 31 ve 62 sayıları arasında rastgele bir matris oluşturuyor.
print(arr_2)

df_1 = pd.DataFrame(arr_2, ["A","B","C","D"],["E","F","G"]) # arr_2 matrisinin satır ve sütünlarına harf atıyor ve çerçeveliyor.
print(df_1)

dict_2 = {1 : pd.Series([31, 43.3, 5.9], index= ["A", "B", "C"]),
          2 : pd.Series([31, 43.3, 5., 69], index= ["A", "B", "C","D"])} # Her iki elemanı da SERİ olan iki elemanlı bir sözlük tanımlıyor.
df_2 = pd.DataFrame(dict_2) #Sözlük çerçeveleniyor.
print(df_2)

df_3 = pd.DataFrame.from_dict(dict([("A", [1,2,3]), ("B", [4,5,6])])) #Yukarıda yaptığımız işlemin tek satıra indirilerek kendiliğinden indexlenmiş versiyonu.
print(df_3)

df_4 = pd.DataFrame.from_dict(dict([("A", [1,2,3]), ("B", [4,5,6])]),
                              orient= "index", columns=["C","D","E"]) #Yukarıda yaptığımız işlemin indexlenmiş versiyonu.
print(df_4)
"""

# Read_Write
"""
a = pd.read_csv(r"D:\Development\GitHub\Python_Development\Pandas\00.csv")
print(a)

df_1 = pd.DataFrame.from_dict(dict([("A", [1,2,3]), ("B", [4,5,6])]),
                              orient= "index", columns=["C","D","E"])

df_1.to_csv("01.csv", index= False) # Dataframe'den csv dosyası oluşturma
"""


exam_scores = pd.read_csv(r"D:\Development\GitHub\Python_Development\Pandas\exam_scores.csv")
a = exam_scores.gender.unique()
print(a)

"""
print(exam_scores.shape) # satır ve sütün sayısını verir
print(exam_scores.head) # Dataset'in ilk kısmını verir, parantez içine girilen sayı kadar baştan satır gösterir
print(exam_scores.tail(3)) # Dataset'in son kısmını verir, parantez içine girilen sayı kadar sondan satır gösterir
print(exam_scores.dtypes) # Her sütunun veri tipini gösterir
print(exam_scores.info()) # Dataset hakkında kısa bir özet gösterir
"""
print(exam_scores.isna().sum())

"""
print(exam_scores.iloc[0:5,4]) # 0 ile 5. satırların 4. sütundaki(0'dan başlayarak) değerlerini gösterir
print(exam_scores.iloc[[1,3,5],2]) # 1, 3 ve 5. satırların 2. sütundaki değerlerini gösterir.
print(exam_scores.iloc[-3: , 0:2]) # sondan 3 satırın ilk üç sütundaki değerlerini gösterir
print(exam_scores.loc[0:5 , ["gender"]]) # ilk 5 satırın "gender" sütunundaki değerlerini gösterir

print(exam_scores.gender) # DataSet'deki "gender" sütununu gösterir.
print(exam_scores["gender"]) # ""   ""  ""

print(exam_scores[["gender", "reading score"]]) # DataSet'deki "gender" ve "reading score" sütunlarını gösterir.
print(exam_scores.gender == "male") #gender sütununda male yazanları true diğerlerini false olarak gösterir
print(exam_scores[exam_scores.gender == "male"]) #gender sütununda male yazanları gösterir
exam_scores.gender = 'Male' # Gender sütunundaki tüm verileri male olarak değiştirir.
print(exam_scores)
"""

x = pd.read_csv(r"D:\Development\GitHub\Python_Development\Pandas\01.csv")

"""
print(x)
print(x.loc[9,["crime_rate"]])
print(x.loc[0:99,["physicians"]])
sample_data1 = x.loc[[3, 5, 7, 9, 13, 98],["land_area", "income", "region", "crime_rate"]]
print(sample_data1)
sample_data2 = x[x.region == 2]
print(sample_data2)
"""

"""
print(exam_scores.describe()) # Sayısal sütunların özetini gösterir
print(exam_scores.describe(include= "object")) # "include" parametresi ile istediğin kategorideki sütunları gösteriri
print(exam_scores.describe(include= "all")) # Bütün kategorideki sütunları gösterir

print(x.mean())
print(x.region.unique())
a = x.describe()
a.to_csv("00.csv", index= False)

print(x.describe(include= "all"))
print(x.info())

b = x[x.region == 3]
print(b)
print(b.info())
print(x.region.value_counts())
"""

"""
print(exam_scores.columns)
exam_scores.rename(columns= { # İstenilen sütunların ismini değiştirir.
    "race/ethnicity" : "race",
    "parental level of education" : "parental_education"}, inplace= True)
"""

"""
print(x.sort_values(by= "crime_rate").tail())

print(exam_scores.isna())
print(exam_scores.isnull())
print(exam_scores.isnull().sum())
"""

"""
titanic_data = pd.read_csv(r"D:\Development\GitHub\Python_Development\Pandas\titanic_data.csv")

print(titanic_data.isnull().sum())
print(titanic_data.Age.mean())
titanic_data.Age.fillna(29.69)
print(titanic_data.Age.mean())
print(titanic_data.Embarked.value_counts())
titanic_data.Embarked.fillna(644)
print(titanic_data.Embarked.value_counts())
"""
