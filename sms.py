import requests, os, sys, time, datetime
from requests import get
starttime = datetime.datetime.now().strftime("%X")
print("\033[96m Made by github.com/SukunaBR \033[0m ")
print("\033[93m Versão 1.0 \033[0m")
print("\033[91m Conectando com o servidor... \033[0m")
time.sleep(2)
os.system("bash rq.sh")
def menu() :
    print("\033[91m1. \033[92mEnviar mensagem anonima\033[0m")
    print("\033[91m2. \033[92mVerificar status do servidor\033[0m")
    print("\033[91m3. \033[92mAjuda\033[0m")
    print("\033[91m4. \033[92mVerificar historico \033[0m")
    print("\033[91m5. \033[92mSair\033[0m")
def control() :
    ctrl = input("Selecione uma opção: ")
    if ctrl == "1" :
        sms()
    elif ctrl == "2" :
        status()
    elif ctrl == "3" :
        help()
    elif ctrl == "4" :
        history()
    elif ctrl == "5" :
        print("obrigado por usar AnnonymusSMS.\nvolte sempre!")
        exit()
    else :
        print("\033[91mNumero invalido!\033[0m")
def sms() :
   phone_no = input("Insira o numero : ")
   msg = input("Mensagem a enviar : ")

   resp = requests.post('https://textbelt.com/text',{
	'phone' : phone_no,
	'message' : msg ,
	'key' : 'textbelt'
   })
   print(resp.text)
   time = datetime.datetime.now()
   clock = time.strftime("%X")  
   date = time.strftime("%x")
   save = open("sess.txt", "a")
   save.write(f"\nip = {ip} : time = {clock} : date = {date} : stats = {resp.text} : phone no.  = {phone_no} ")
def history() :
    if os.path.exists("sess.txt") :
        with open("sess.txt","r") as file :
            sessions = file.read().splitlines()
            ses_numbers = len(sessions)
            if ses_numbers > 1 :
                os.system("python sess_info.py")
                more_details = input("Deseja ver as sessoes? (Default : nao) : ").lower()
                if more_details == "sim" or more_details == "s" :
                    os.system("cat sess.txt")
                else :
                    print("Obrigado por usar AnnonymusSMS. Volte Sempre!")
            elif ses_number == 1: 
                print(file.readline)
            else :
                print("ocorreu um erro desconhecido!")
    else :
        print("Voce esta usando pela primeira vez ou historico foi apagado.")
def status() :
  textID = input("Insira o ID da Mensagem : ") 
  os.system(f"curl https://textbelt.com/status/{textID}")
def help() :
    print("escolha o seu problema de acordo com as condições existentes! ")
    print("A. Não é possível enviar sms após uma tentativa no mesmo número!")
    print("B. Não é possível enviar sms devido ao grande uso do site. ")
    print("C. Não envia mais de um sms, mesmo para um número diferente. ")
    print("D. Outro")
    qna = input(">>> ").lower()
    if qna == "a" :
        print("esta é uma versão demo, portanto, pode enviar apenas 1 sms por dia para o mesmo número. Você pode enviar para um número diferente usando o vpn.")
    elif qna == "b" :
        print("às vezes, quando o site é usado em grande quantidade, eles desativam o sms gratuito por algum tempo. Por favor, espere um pouco ...")
    elif qna == "c" :
        print("por favor, verifique seu vpn com cuidado e use apenas os melhores vpns. Como nordvpn, protonvpn etc.")
    elif qna == "d" :
        print("desculpe por qualquer problema! Você pode mencioná-lo em github.com/SukunaBR")
    else :
        print("Opcão invalida!! \n Saindo.. Desculpe..")
        exit()
os.system("clear")
os.system("toilet -f mono12 -F gay SukunaBR")
print("\033[94m####################### \033[31mVersão 1.0\033[0m \033[94m######################  ")
print("\033[1;96mMade by github.com/SukunaBR\033[0m")
print(f"Programa iniciado às: {starttime}")
ip = get("https://api.ipify.org").text
ip_c = input("\033[95;107mDeseja ver o seu endereço IP atual ? : \033[0m").lower()
if ip_c == "sim" or ip_c == "s" :
   print(f"\033[1;93mVoce esta conectado ao IP :\033[0m \033[91;107m{ip}\033[0m ")
elif ip_c == "nao" or ip_c == "n" :
   print("\033[93;101mespero que saiba o que esta fazendo :) \033[0m")
else :
   print("Opção invalida!! selecione sim ou nao ")
menu()
control()