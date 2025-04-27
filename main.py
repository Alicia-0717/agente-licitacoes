
import time
import requests

def processar_edital(link_edital, prefeitura, numero_edital):
    try:
        response = requests.get(link_edital)
        if response.status_code == 200:
            # Simulação de processamento do edital
            print(f"✅ Edital {numero_edital} da {prefeitura} baixado com sucesso!")
            print(f"📄 Tamanho do edital: {len(response.content)} bytes")
            return {"status": "sucesso", "mensagem": "Edital processado com sucesso."}
        else:
            print(f"❌ Falha ao baixar o edital. Código {response.status_code}")
            return {"status": "erro", "mensagem": "Falha ao baixar o edital."}
    except Exception as e:
        print(f"❌ Erro no processamento: {str(e)}")
        return {"status": "erro", "mensagem": str(e)}

def executar_agente():
    while True:
        print("Agente de Licitações rodando...")
        time.sleep(60)

if __name__ == "__main__":
    executar_agente()
