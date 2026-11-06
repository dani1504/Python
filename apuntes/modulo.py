latencias_web = [1.5, 2.3 , 4.7, 8.9]
latencias_ftp = [1.5, 2.3 , 4.7, 8.9]

from utiles import calcula_media

media_web = calcula_media(latencias_web)
media_ftp = calcula_media(latencias_ftp)

if media_ftp > media_web:
    print("Media ftp es mayor")
elif media_web > media_ftp:
    print("Media web es mayor")
else:
    print("Las medias son iguales")