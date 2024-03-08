from variablesAux import getDate, user, sistema


def gerar_insert_titular(titular, data_base, cod_agencia, cnpjConglomerado, nro_conta):
    return f"""
    INSERT INTO FGC_TITULARES (
        DATA_BASE,
        CNPJ_IF,
        SISTEMA,
        CODAGENCIA,
        NROCONTA,
        CPF_CNPJ,
        NOMECLIENTE,
        ISENTO_IR,
        DATA_NASCIMENTO,
        USUARIO,
        DATAATUALIZACAO
    ) VALUES (
        '{data_base}',
        '{cnpjConglomerado}',
        'sistema',
        '{cod_agencia}',
        '{nro_conta}',
        '{titular['documentoCliente']}',
        '{titular['nomeCliente']}',
        '{titular['isencaoIR']}',
        '{titular['dataNascimentoCriacaoFundacao'] if titular['dataNascimentoCriacaoFundacao'] else 'NULL'},
        '{user}',
        '{getDate}'
    );
    """


def gerar_insert_conta(conta, data_base, cod_agencia, cnpjConglomerado):
    return f"""
    INSERT INTO FGC_CONTAS (
        DATA_BASE,
        CNPJ_IF,
        SISTEMA,
        CODAGENCIA,
        NROCONTA,
        DIGITO_CONTA,
        USUARIO,
        TIPO_CONTA,
        QTD_TITULAR,
        TIPO_TITULARIDADE,
        DATAATUALIZACAO,
        IDENTIFICACAO_CLIENTE
    ) VALUES (
        '{data_base}',
        '{cnpjConglomerado}',
        '{sistema}',
        '{cod_agencia}',
        '{conta['numeroConta']}',
        '{conta['digitoConta']}',
        '{user}',
        '{conta['tipoConta']}',
        '{conta['quantidadeTitulares']}',
        '{conta['idTipoTitularidade']}',
        '{getDate}',
        '{conta['identificacaoCliente']}'
    );
    """


def gerar_insert_produto(produto, conta, cnpjConglomerado, data_base, cod_agencia):
    inst_fin = 'instrumentosFinanceiros'
    return f"""
    INSERT INTO FGC_PRODUTOS (
        DATA_BASE,
        CNPJ_IF,
        SISTEMA,
        CODAGENCIA,
        NROCONTA,
        PRODUTO,
        COD_INSTRUMENTO,
        DATA_AQUISICAO,
        DATA_VENCIMENTO,
        QTD_EMITIDA,
        QTD_DATABASE,
        VALOR_EMITIDO,
        VALOR_DATABASE,
        VALOR_BLOQUEIO,
        USUARIO,
        DATAATUALIZACAO
    ) VALUES (
        '{data_base}',
        '{cnpjConglomerado}',
        'sistema',
        '{cod_agencia}',
        '{conta['numeroConta']}',
        '{produto['idProduto']}',
        '{produto[inst_fin][0]['codigoInstrumentoFinanceiro']}',
        '{produto[inst_fin][0]['dataAquisicao'] if produto[inst_fin][0]['dataAquisicao'] else 'NULL'},
        '{produto[inst_fin][0]['dataVencimento'] if produto[inst_fin][0]['dataVencimento'] else 'NULL'},
        '{produto[inst_fin][0]['quantidadeEmitida'] if produto[inst_fin][0]['quantidadeEmitida'] else 'NULL'},
        '{produto[inst_fin][0]['quantidadeDataBase'] if produto[inst_fin][0]['quantidadeDataBase'] else 'NULL'},
        '{produto[inst_fin][0]['valorEmitido'] if produto[inst_fin][0]['valorEmitido'] else 'NULL'},
        '{produto[inst_fin][0]['valorAtualDataBase'] if produto[inst_fin][0]['valorAtualDataBase'] else 'NULL'},
        '{produto[inst_fin][0]['valorBloqueio'] if produto[inst_fin][0]['valorBloqueio'] else 'NULL'},
        '{user}',
        '{getDate}'
    );
    """


def gerar_insert_endereco(endereco, conta, data_base, cod_agencia, cnpjConglomerado):
    return f"""
    INSERT INTO FGC_ENDERECOS (
        DATA_BASE,
        CNPJ_IF,
        SISTEMA,
        CODAGENCIA,
        NROCONTA,
        LOGRADOURO,
        NUMERO,
        BAIRRO,
        CIDADE,
        ESTADO,
        CEP,
        USUARIO,
        DATAATUALIZACAO
    ) VALUES (
        '{data_base}',
        '{cnpjConglomerado}',
        'sistema',
        '{cod_agencia}',
        '{conta['numeroConta']}',
        '{endereco['logradouro'] if endereco['logradouro'] else 'NULL'}',
        '{endereco['numero'] if endereco['numero'] else 'NULL'}',
        '{endereco['bairro'] if endereco['bairro'] else 'NULL'}',
        '{endereco['cidade'] if endereco['cidade'] else 'NULL'}',
        '{endereco['estado'] if endereco['estado'] else 'NULL'}',
        '{endereco['cep'] if endereco['cep'] else 'NULL'}',
        '{user}',
        '{getDate}',
    );
  """
