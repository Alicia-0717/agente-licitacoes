from flask import Flask, request, jsonify
import main  # seu script atual

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Agente de Licitações ativo', 200

@app.route('/verificar-edital', methods=['POST'])
def verificar_edital():
    dados = request.json

    link = dados.get('link_edital')
    prefeitura = dados.get('prefeitura')
    numero = dados.get('numero_edital')

    # Aqui você chamaria sua função de análise do edital
    resultado = main.processar_edital(link, prefeitura, numero)

    return jsonify({'resultado': resultado}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
