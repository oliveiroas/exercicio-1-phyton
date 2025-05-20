import json
import os

data = "funcionarios.json"

def  carregar_dados():
    if os.path.exists(data):
         with open(data, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []
         
funcionarios = carregar_dados()
def carregar_funcionarios():
    for funcionario in funcionarios:
        print(f"do funcionario{funcionario ["nome"]} salario do funcionario: {funcionario["salario"]}")

carregar_funcionarios()