import pandas as pd
import numpy as np
import urllib.request

# Cargamos el fichero
full_airbnb = pd.read_csv('./data/airbnb-listings.csv',sep=';', decimal='.')
print(full_airbnb.shape)

#Para obtener las imagenes de cada registro vamos a usar la columna "Thumbnail Url" ya que tienen un size acorde a nuestras necesidades
#Nos quedamos con el ID (para identificar de manera univoca la iamgen una vez descargada) y obviamente con la url

#Incluimos una nueva columna con NaN donde ira el path de las imagenes descargadas
nan_value = float("NaN")
full_airbnb["image_path"] = nan_value


#Definimos la funcion que se encargara de descargar las imagenes
def download_image(id,url,file_path):
    
    try:
        filename = 'image-{}.jpg'.format(id)
        full_path = '{}{}'.format(file_path, filename)
        urllib.request.urlretrieve(url, full_path)
        return full_path
    except:
        nan_value = float("NaN")
        return nan_value

# Set Constants
FILE_PATH = 'images/'


#Recorremos las urls del dataset
for index, row in full_airbnb.iterrows():
    if type(row['Thumbnail Url'])==str:
        id = row['ID']
        url = row['Thumbnail Url']
        image_path = download_image(id,url,FILE_PATH)
        full_airbnb.loc[index,"image_path"] = image_path

#full_airbnb["image_path"].isnull().sum()

# #Este funciona
# id = 10403923
# url = "https://a0.muscache.com/im/pictures/638a5a56-d8b3-4aec-9b01-d2cde5111b8c.jpg?aki_policy=small"
# image_path = download_image(id,url,'images2/')
# full_airbnb.loc[full_airbnb.ID == id, 'image_path'] = image_path
# print(full_airbnb.loc[full_airbnb.ID == id, 'image_path'].values[0])

# #Este no funciona
# id = 9987434
# url = "https://a0.muscache.com/im/pictures/4f5b247f-3cad-480a-bf11-121f37b88f8a.jpg?aki_policy=small"
# image_path = download_image(id,url,'images2/')
# full_airbnb.loc[full_airbnb.ID == id, 'image_path'] = image_path

# print(full_airbnb.loc[full_airbnb.ID == id, 'image_path'].values[0])

