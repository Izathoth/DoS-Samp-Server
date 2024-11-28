import socket
import time
import os
import requests
import threading
from termcolor import colored  # Importando a biblioteca para colorir as mensagens

# Variáveis configuráveis
REQUEST_TIMEOUT = 5          # Tempo limite para a requisição (em segundos)
CHECK_INTERVAL = 10          # Intervalo entre verificações (em segundos)
RQS_GET = 50                 # Número de requisições GET para realizar
RQS_POST = 50                # Número de requisições POST para realizar

# Função para verificar se o servidor está online
def check_server_online(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(REQUEST_TIMEOUT)
        sock.connect((ip, port))
        sock.close()
        print(colored(f"Servidor {ip} na porta {port} está ONLINE.", 'green'))
        return True
    except socket.error:
        print(colored(f"Servidor {ip} na porta {port} está OFFLINE.", 'red'))
        return False

# Função para obter o status do servidor
def get_server_status(ip):
    try:
        # Usando uma requisição HTTP para verificar se o servidor está acessível na web
        response = requests.get(f"http://{ip}", timeout=REQUEST_TIMEOUT)
        if response.status_code == 200:
            print(colored(f"Servidor {ip} está ONLINE (status HTTP: {response.status_code}).", 'green'))
        else:
            print(colored(f"Servidor {ip} está ONLINE (status HTTP: {response.status_code}).", 'yellow'))
    except requests.exceptions.RequestException as e:
        print(colored(f"Erro ao tentar conectar ao servidor {ip}: {e}", 'red'))

# Função para testar o ping do servidor
def test_ping(ip):
    response = os.system(f"ping -c 1 {ip}")
    if response == 0:
        print(colored(f"{ip} está ONLINE (Ping bem-sucedido).", 'green'))
    else:
        print(colored(f"{ip} está OFFLINE (Ping falhou).", 'red'))

# Função para monitorar o servidor em tempo real
def monitor_server(ip, port):
    print(colored("Iniciando o monitoramento do servidor...\n", 'blue'))
    while True:
        if check_server_online(ip, port):
            get_server_status(ip)
            test_ping(ip)
        else:
            print(colored(f"Servidor {ip} na porta {port} está OFFLINE.\n", 'red'))
        
        # Espera antes de realizar a próxima verificação
        time.sleep(CHECK_INTERVAL)

# Função de loop para enviar requisições
def send_requests(ip):
    while True:
        # Enviar requisições GET
        for i in range(RQS_GET):
            try:
                response = requests.get(f"http://{ip}", timeout=REQUEST_TIMEOUT)
                print(colored(f"Requisição GET {i+1}/{RQS_GET} enviada. Status: {response.status_code}", 'cyan'))
            except requests.exceptions.RequestException as e:
                print(colored(f"Erro na requisição GET {i+1}/{RQS_GET}: {e}", 'red'))
        
        # Enviar requisições POST
        for i in range(RQS_POST):
            try:
                response = requests.post(f"http://{ip}", data={"test": "data"}, timeout=REQUEST_TIMEOUT)
                print(colored(f"Requisição POST {i+1}/{RQS_POST} enviada. Status: {response.status_code}", 'cyan'))
            except requests.exceptions.RequestException as e:
                print(colored(f"Erro na requisição POST {i+1}/{RQS_POST}: {e}", 'red'))
        
        time.sleep(CHECK_INTERVAL)

# Função principal que roda os testes em paralelo
def main():
    # Solicitar ao usuário o IP e a porta do servidor
    ip = input(colored("Digite o IP do servidor de SAMP para testar: ", 'yellow'))
    port = int(input(colored("Digite a porta do servidor de SAMP: ", 'yellow')))
    
    # Rodar monitoramento do servidor e envio de requisições em threads separadas
    monitor_thread = threading.Thread(target=monitor_server, args=(ip, port))
    request_thread = threading.Thread(target=send_requests, args=(ip,))
    
    monitor_thread.start()
    request_thread.start()

    monitor_thread.join()
    request_thread.join()

if __name__ == "__main__":
    main()