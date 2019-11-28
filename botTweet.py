import tweepy

from random import randint

from time import sleep

consumer_key = 'wxswvldJI8CxpKK0eBpYnSVB8'
consumer_secret='waxL4unknlXHYlLu9WGqa533vmmGa4b36syfyrTLiObP2Ade8s'
access_token='1199797594744147969-fZLZ7JozEeDuR359gtCZgBzX6w1fzj'
access_token_secret='U8tgMne2qufgCyO3gKgEWWeOKIMM63OGuLpe3IW4PgsdQ'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def choisirLettre(c1,c2,c3):
    liste=[]
    for k in dict[c1][c2][c3]:
        for i in range(dict[c1][c2][c3][k]):
            liste.append(k)
    r = randint(0,max(0,len(liste)-1))
    if liste!=[]:
        return liste[r]

def genMot():
    mot=""
    c1,c2,c3=" "," ",choisirLettre(" "," "," ")
    while (c1!=" " or c2!=" " or c3!=" "):
        if c1==None or c2==None or c3==None:
            return mot
        else:
            c1,c2,c3=c2,c3,choisirLettre(c1,c2,c3)
            if c1==None or c2==None or c3==None:
                return mot
            else:
                mot+=c1
    return(mot)

file=open("dictxt.txt","r")
dict=eval(file.read())
while True:
    mot=genMot()
    api.update_status(mot)
    sleep(21600)
