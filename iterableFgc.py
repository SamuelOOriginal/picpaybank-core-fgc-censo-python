import json
import os.path

from inserts import gerar_insert_titular, gerar_insert_conta, gerar_insert_produto, gerar_insert_endereco


def runCode():
    folder = 'file'
    for archive in os.listdir(folder):
        if archive.endswith('.json'):
            path_archive = os.path.join(folder, archive)

            with open(path_archive, 'r') as f:
                data = json.load(f)

            for conta in data['data']['emissores'][0]['contas']:
                cod_agencia = conta['agencia']
                data_base = data['data']['dataBase']
                conglomerado = data['data']['cnpjConglomerado']
                nro_conta = conta['numeroConta']

                insert_titular = gerar_insert_titular(conta['titulares'][0], data_base, cod_agencia, conglomerado,
                                                      nro_conta)
                insert_conta = gerar_insert_conta(conta, data_base, cod_agencia, conglomerado)
                insert_produto = gerar_insert_produto(conta['produtos'][0], conta, conglomerado, data_base, cod_agencia)
                insert_endereco = gerar_insert_endereco(conta['endereco'], conta, data_base, cod_agencia, conglomerado)

                sql_folder = "sql"
                sql_name = "inserts.sql"

                if not os.path.exists(sql_folder):
                    os.makedirs(sql_folder)

                sql_filepath = os.path.join(sql_folder, sql_name)

                with open(sql_filepath, 'a') as f:
                    f.write(insert_titular + '\n')
                    f.write(insert_conta + '\n')
                    f.write(insert_produto + '\n')
                    f.write(insert_endereco + '\n')


print("Inserts criado com sucesso!!!")
