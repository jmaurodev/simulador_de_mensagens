from django.shortcuts import render
from random import randint
from datetime import datetime

def index(request):
    return render(request, 'index.html')


def mensageiro(request):
    def precedencia(i):
        return{
        1: 'Urgentíssima',
        2: 'Urgente',
        3: 'Preferencial',
        4: 'Rotina',
        }[i]

    def class_sigilosa(i):
        return{
        1: 'Ultra-Secreto',
        2: 'Secreto',
        3: 'Confidencial',
        4: 'Reservado',
        5: 'Ostensivo',
        }[i]

    def criptografado(i):
        return{
        0: 'Não',
        1: 'Sim',
        }[i]

    def meio(i):
        return{
        1: 'Rádio',
        2: 'Zimbra',
        3: 'Mensageiro',
        }[i]

    def de_para(i):
        return{
        1: '25 BI Pqdt',
        2: '26 BI Pqdt',
        3: '27 BI Pqdt',
        4: '8 GAC Pqdt',
        5: '21 Bia AAAe Pqdt',
        6: '20 B Log',
        7: 'Cia Prec Pqdt',
        8: '1 Esqd C Pqdt',
        9: '1 Cia E Cmb Pqdt',
        }[i]

    arquivo = open('app_mensageiro/static/mensagens', encoding='utf-8')
    referencia = randint(1, 1000)
    linhas = arquivo.readlines()
    mensagem = linhas[referencia][:-1]
    meio = meio(randint(1, 3))
    de = de_para(randint(1,9))
    para = de_para(randint(1,9))
    precedencia = precedencia(randint(1, 4))
    class_sigilosa = class_sigilosa(randint(1, 5))
    criptografado = criptografado(randint(0, 1))
    gdh = datetime.now().strftime("%d%H%M-%m-%Y")
    intervalo = 3000
    context = {
        'mensagem': mensagem,
        'meio': meio,
        'de': de,
        'para': para,
        'precedencia': precedencia,
        'class_sigilosa': class_sigilosa,
        'referencia': referencia,
        'criptografado': criptografado,
        'gdh': gdh,
        'intervalo': intervalo
    }
    return render(request, 'mensageiro.html', context)
