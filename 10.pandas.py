import pandas as pd
"""
#series ve data-frame adlı veri modelleri ile ünlüdür...

indeksler_listesi = ['ülke', 'başkent', 'kıta', 'kısaltma']
veri_listesi = ['Türkiye', 'Ankara', 'Avrupa-Asya', 'TR']

seri1 = pd.Series(veri_listesi, indeksler_listesi)

#veri_listesi = [['Türkiye', 'Ankara', 'Avrupa-Asya', 'TR'], ['İtalya', 'Roma', 'Avrupa', 'İT']]

seri2 = pd.Series([34, 67, 90, -9, 56])

seri3 = pd.Series([58, 100, 7, -43, -19, 90])

print(seri2 + seri3)

from numpy.random import randn

df1 = pd.DataFrame(data = randn(3,3), index = ['a', 'b', 'c'], columns = ['sütun1', 'sütun2', 'sütun3'])
df2 = pd.DataFrame(data = randn(4,6))

print(df1[['sütun1', 'sütun3']])

df1['sütun4'] = pd.Series(randn(3),['a', 'b', 'c'])

df2['sütun_yeni'] = pd.Series(randn(3)) #burada 3 satır dediğimiz için df2 son satırda nan oluşur...
"""

araba = pd.read_csv('car-sales.csv')

print(araba.head())
print(araba.shape)

#araba.columns = ['üretici', 'model', ....]

araba['yeni_sütun'] = araba.Model + ', ' + araba.Manufacturer

yiyecek = pd.read_excel('food-sales.xlsx', sheet_name=0)

araba.to_csv('yeni_car-sales.csv')

yiyecek.to_excel('yeni_dosya.xlsx')

araba.drop_duplicates()
araba2 = araba.drop(['Model', 'Manufacturer'], axis=1)
araba3 = araba.drop([0, 1])

araba4 = araba.loc[:,['Model', 'Vehicle_type']]

araba5 = araba.iloc[:,[1, 4]]

araba6 = araba.dropna()







