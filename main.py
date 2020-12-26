import tweepy
import sys

file = []

try:
    file = open("credentials.txt", 'r').read().split('\n')
    if(len(file) != 4):
        raise Exception('Por favor verifique que el archivo tiene todas las credenciales')
except FileNotFoundError:
    print("Ha ocurrido un error al abrir el archivo, asegurese que el archivo exista")
    sys.exit()

CONSUMER_KEY = file[0]
CONSUMER_SECRET = file[1]
ACCESS_TOKEN = file[2]
ACCESS_TOKEN_SECRET = file[3]

if len(CONSUMER_KEY) == 0 or len(CONSUMER_SECRET) == 0 or len(ACCESS_TOKEN) == 0 or len(ACCESS_TOKEN_SECRET) == 0:
    raise Exception("Las credenciales de acceso son obligatorias")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def publictweet():
    try:
        print('Escriba el tweet que será publicado')
        print('*Cuando termine solo presione enter')
        string = str(input())
        if(len(string) == 0):
            raise Exception("vacio")
        api.update_status(string)
        print('Mensaje publicado con exito!', string)
    except:
        print('Ha ocurrido un error')


def getAllTweetByUser():
    print('Ingrese el id del usuario')
    user = str(input())
    if(len(user) == 0):
        print('El nombre de usuario no es valido')
        sys.exit()
    for status in tweepy.Cursor(api.user_timeline, id=user, tweet_mode="extended").items():
        print(status.full_text)

print('Escriba la accion a ealizar')
print('1 <= Escribir un tweet')
print('2 <= Obtener los tweet de un usuario')

response = str(input())
if(response == '1'):
    publictweet()
elif(response == '2'):
    getAllTweetByUser()
else:
    print('El valor ingresado: ', response,' no es valido')




