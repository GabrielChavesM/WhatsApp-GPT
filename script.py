import os
import pywhatkit as kit
from groq import Groq
from dotenv import load_dotenv
import time

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Função para ler os prompts
def ler_historico_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as file:
            historico = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        historico = []
    return historico

# Função para escrever no arquivo de texto
def escrever_no_arquivo(nome_arquivo, mensagem):
    with open(nome_arquivo, "a", encoding="utf-8") as file:
        file.write(mensagem + "\n")

# Função para limpar o arquivo de texto
def limpar_arquivo(nome_arquivo):
    with open(nome_arquivo, "w", encoding="utf-8") as file:
        file.write("")

HISTORICO_TXT = "prompts.txt"

# Função para obter a resposta da IA via API Groq
def obter_resposta_groq(pergunta):
    client = Groq(api_key=GROQ_API_KEY)

    historico = ler_historico_arquivo(HISTORICO_TXT)
    historico.append(f"Usuário: {pergunta}")
    prompt_completo = "\n".join(historico)

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": f"{prompt_completo}"}
            ],
            model="llama3-8b-8192",
        )

        resposta_bot = chat_completion.choices[0].message.content.strip()

        historico.append(f"Bot: {resposta_bot}")       
        escrever_no_arquivo(HISTORICO_TXT, f"Usuário: {pergunta}")
        escrever_no_arquivo(HISTORICO_TXT, f"Bot: {resposta_bot}")

        return resposta_bot

    except Exception as e:
        print(f"Ocorreu um erro ao acessar a API Groq: {str(e)}")
        return "Ocorreu um erro ao acessar a API. Por favor, tente novamente mais tarde."

# Função para enviar a mensagem via pywhatkit para o número de WhatsApp
def enviar_mensagem(numero_telefone, mensagem):
    try:
        # O número de telefone precisa ser no formato internacional
        # O formato do número de telefone: +351 e número sem parênteses
        # Exemplo: +351 999999999
        
        # Enviar a mensagem via pywhatkit
        print(f"Enviando mensagem para {numero_telefone}...")
        kit.sendwhatmsg_instantly(numero_telefone, mensagem)
        time.sleep(1)  # Tempo para garantir que a mensagem foi enviada

        print(f"Mensagem enviada: {mensagem}")
    except Exception as e:
        print(f"Erro ao enviar a mensagem via WhatsApp: {str(e)}")

def main():
    print("Bem-vindo ao chat com a IA!")
    print("Você pode conversar comigo sobre qualquer assunto.")
    print("Para sair, digite 'sair' a qualquer momento.\n")

    numero_telefone = input("Digite o número de telefone (com código do país, ex: +351 999999999): ")

    while True:
        pergunta = input("Mensagem: ")

        if pergunta.lower() == 'sair':
            print("Saindo do chat...")
            limpar_arquivo(HISTORICO_TXT)  # Limpar o arquivo ao sair
            break

        # Obter a resposta da IA
        resposta = obter_resposta_groq(pergunta)
        print("AI: ", resposta)

        # Enviar a resposta para o número de WhatsApp fornecido
        enviar_mensagem(numero_telefone, resposta)
        print()

if __name__ == "__main__":
    main()