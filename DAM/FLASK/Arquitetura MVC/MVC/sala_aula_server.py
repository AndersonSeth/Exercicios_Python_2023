from flask import Flask, jsonify, request

import controller.aluno_controller as aluno_controller

app = Flask (__name__)

@app.route("/")
def start():
    return "Legal demais, separamos o codigo em pastas com o MVC"

@app.route('/alunos')
def getAlunos():#Lembrando que o metodo GET é padrão, por isso não é necessario passar o verbo
    return aluno_controller.listar()

@app.route('/alunos/<int:id_consulta>', methods=['GET'])
def getAlunosId(id_consulta):
    return aluno_controller.localizaPorId(id_consulta)

@app.route('/alunos/maior_media', methods=["GET"])
def getAlunoMaiorMedia():
    return aluno_controller.localizarPorMaiorMedia()

@app.route('/alunos', methods=['POST'])
def inserir():
    aluno = request.json
    return aluno_controller.inserirAluno(aluno)

@app.route('/alunos/<int:id_deletar>', methods=['DELETE'])
def excluir(id_deletar):
    return aluno_controller.excluirPorId(id_deletar)

@app.route('/alunos/<int:id_alterar>', methods=['PUT'])
def alterar(id_alterar):
    aluno = request.json
    return aluno_controller.alterarAluno(id_alterar, aluno)




if __name__ == '__main__':
    app.run(host='localhost', port = 5002, debug= True)