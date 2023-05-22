from flask import Flask, make_response, jsonify, request
from bd import jogos

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/jogos', methods=['GET'])
def get_jogos():
    return make_response(
            jsonify(jogos))


@app.route('/jogos', methods=['POST'])
def inserir_jogos():
    jogo = request.json
    jogos.append(jogo)
    return make_response(
        jsonify(jogo))


app.run()



