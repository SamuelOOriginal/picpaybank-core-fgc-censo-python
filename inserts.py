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
        '{sistema}',
        '{cod_agencia}',
        '{nro_conta}',
        '{titular['documentoCliente']}',
        '{titular['nomeCliente']}',
        '{titular['isencaoIR']}',
        '{titular['dataNascimentoCriacaoFundacao']}',
        '{user}',
        {getDate}
    );
    """


def gerar_insert_conta(conta, data_base, cod_agencia, cnpjConglomerado):
    identificacao_cliente = conta['identificacaoCliente'] if conta['identificacaoCliente'] else ""
    return f"""
    INSERT INTO FGC_CONTAS (
        DATA_BASE,
        CNPJ_IF,
        SISTEMA,
        CODAGENCIA,
        NROCONTA,
        DG_CONTA,
        USUARIO,
        TIPO_CONTA,
        QTD_TITULAR,
        TIPO_TITULARIDADE,
        IDENTIFICACAO_CLIENTE,
        DATAATUALIZACAO
    ) VALUES (
        '{data_base}',
        '{cnpjConglomerado}',
        '{sistema}',
        '{cod_agencia}',
        '{conta['numeroConta']}',
        '{conta['digitoConta']}',
        '{user}',
        '{conta['tipoConta']}',
        {conta['quantidadeTitulares']},
        {conta['idTipoTitularidade']},
        '{identificacao_cliente}',
        {getDate}

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
        '{sistema}',
        '{cod_agencia}',
        '{conta['numeroConta']}',
        {produto['idProduto']},
        '{produto[inst_fin][0]['codigoInstrumentoFinanceiro']}',
        '{produto[inst_fin][0]['dataAquisicao']}',
        {produto[inst_fin][0]['dataVencimento']},
        {produto[inst_fin][0]['quantidadeEmitida']},
        {produto[inst_fin][0]['quantidadeDataBase']},
        {produto[inst_fin][0]['valorEmitido']},
        {produto[inst_fin][0]['valorAtualDataBase']},
        {produto[inst_fin][0]['valorBloqueio']},
        '{user}',
        {getDate}
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
        '{sistema}',
        '{cod_agencia}',
        '{conta['numeroConta']}',
        '{endereco['logradouro']}',
        '{endereco['numero']}',
        '{endereco['bairro']}',
        '{endereco['cidade']}',
        '{endereco['estado']}',
        '{endereco['cep']}',
        '{user}',
        {getDate}
    );
  """
