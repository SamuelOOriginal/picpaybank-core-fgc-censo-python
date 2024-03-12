import json
import os.path
import shutil

from inserts import gerar_insert_titular, gerar_insert_conta, gerar_insert_produto, gerar_insert_endereco
from datetime import datetime

folder = 'file'
sql_folder = "sql"
sql_processed = "processed"
sql_name = "inserts.sql"

sql_filepath = os.path.join(sql_folder, sql_name)


def move_sql_processed():
    proc_arch = os.listdir(sql_folder)

    for proc_arch in proc_arch:
        if proc_arch.endswith('.sql'):
            date_now = datetime.now()
            format_date = date_now.strftime("%d%m%Y%H%M%S")
            new_sql_name = sql_name.split('.')[0] + "_" + format_date + '.sql'
            new_path = os.path.join(sql_processed, new_sql_name)
            shutil.move(sql_filepath, new_path)


def runCode():
    for archive in os.listdir(folder):

        if archive.endswith('.json'):
            path_archive = os.path.join(folder, archive)

            if not os.path.exists(sql_processed):
                os.makedirs(sql_processed)

            if not os.path.exists(sql_folder):
                os.makedirs(sql_folder)

            move_sql_processed()

            with open(path_archive, 'r') as f:
                data = json.load(f)

            for conta in data['data']['emissores'][0]['contas']:
                cod_agencia = conta['agencia']
                data_base = data['data']['dataBase']

                data_base = datetime.strptime(data_base, "%Y%m%d").strftime("%Y-%m-%d")

                conglomerado = data['data']['cnpjConglomerado']
                nro_conta = conta['numeroConta']

                insert_conta = gerar_insert_conta(conta, data_base, cod_agencia, conglomerado)
                insert_titular = gerar_insert_titular(conta['titulares'][0], data_base, cod_agencia, conglomerado,
                                                      nro_conta)
                insert_produto = gerar_insert_produto(conta['produtos'][0], conta, conglomerado, data_base, cod_agencia)
                insert_endereco = gerar_insert_endereco(conta['endereco'], conta, data_base, cod_agencia, conglomerado)

                with open(sql_filepath, 'a') as f:
                    f.write(insert_conta + '\n')
                    f.write(insert_titular + '\n')
                    f.write(insert_produto + '\n')
                    f.write(insert_endereco + '\n')

        print("Inserts criado com sucesso!!!")
