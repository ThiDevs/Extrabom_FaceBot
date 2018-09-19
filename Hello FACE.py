from Facebot_Extrabom import Facebook

# Precisa que ChromeDriver esteja no path

facebot = Facebook.Facebook()
facebot.setLogin(login='[YOUR EMAIL FACEBOOK]',
                 senha='[YOUR PASSWORD]')  # LOGIN E SENHA A QUAL O BOT VAI LOGAR E POSTAR

groupID = ['1889352911359628']  # ID DO GRUPO QUE DESEJA FAZER O POST
facebot.setGrouopIds(groupID)

Posts = ['Post com Imagem']


facebot.start(posts=Posts)

facebot.stop()
