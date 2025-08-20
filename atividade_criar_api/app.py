#Integrantes:
#João Manoel Lelis Oliveira RA: 2401807
#Murilo Gomes Sardinha RA: 2401763
#Vinicius Chamone Guedes Janini RA: 2401580


from flask import Flask, jsonify, request

meuApp = Flask(__name__)

Users = []

@meuApp.route('/users', methods=['POST'])
def create_users():
    data = request.json

    campos = [
        'nome', 'email', 
    ]

    campos_vazio = [campo for campo in campos if not data.get(campo)]
    if campos_vazio:
        return jsonify({'mensagem': f'Esses campos são obrigatorios e não podem estar vazios: {", ".join(campos_vazio)}'}), 400
    
    user = {'id': len(Users) + 1, 'nome': data['nome'], 'email': data['email']}
    Users.append(user)
    return jsonify(user), 201

@meuApp.route('/users', methods=['GET'])
def get_users():
    return jsonify({'Users': Users}), 200

@meuApp.route('/users/<int:user_id>', methods=["GET"])
def get_user(user_id):
    for user in Users:
        if user['id'] == user_id:
            return jsonify(user), 200
    return jsonify({'mensagem': 'Aluno não encontrado'}), 404

@meuApp.route('/users/<int:user_id>', methods=["PUT"])
def update_user(user_id):    
    for user in Users:
        if user['id'] == user_id:
            dados = request.json
        
        campos = [
            'nome', 'email'
        ]

        for campo in campos:
            if campo in dados:
                user[campo] = dados[campo]
        return jsonify(user), 200
    return jsonify({'mensagem': 'User não encontrado'}), 404

@meuApp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in Users:
        if user['id'] == user_id:
            Users.remove(user)
            return jsonify({'mensagem': 'User removido'}), 200
    return jsonify({'mensagem': 'User não encontrado'}), 404


if __name__ == '__main__':
    meuApp.run(debug=True)

