import socket
import select

alvo=input("Digite o IP do alvo: ").strip()
inicio=int(input("A partir de qual porta deve-se iniciar o loop? "))
fim=int(input("A partir de qual porta deve-se encerrar o loop? "))

portas_abertas=[]
tamanho_percorrido_por_loop=100

def percorrer_portas_intervalo(inicio_do_alcance,fim_do_alcance):
    
    portas_sendo_testadas={}
    for porta in range(inicio_do_alcance,fim_do_alcance+1):
        conexao=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conexao.setblocking(False)
        conexao.connect_ex((alvo,porta))
        portas_sendo_testadas[conexao]=porta

    sockets_sendo_testadas=list(portas_sendo_testadas.keys())

    while sockets_sendo_testadas:

        nada,conexoes_testadas,nada=select.select([], sockets_sendo_testadas, [], 3)

        for conexao in conexoes_testadas:
            resultado = portas_sendo_testadas[conexao]
            valor_retornado = conexao.getsockopt(socket.SOL_SOCKET,socket.SO_ERROR)

            if valor_retornado==0:
                portas_abertas.append(resultado)
            conexao.close()

            if conexao in sockets_sendo_testadas:
                sockets_sendo_testadas.remove(conexao)

        if not conexoes_testadas:
            for conexao in sockets_sendo_testadas:
                conexao.close()
            break
        

for alcance in range(inicio,fim+1,tamanho_percorrido_por_loop):
    fim_do_alcance = min(alcance+tamanho_percorrido_por_loop-1,fim)
    percorrer_portas_intervalo(alcance,fim_do_alcance)

if portas_abertas:
    for porta in portas_abertas:
        print(f"A porta {porta} está aberta.")
else: print("Nenhuma porta aberta foi encontrada.")