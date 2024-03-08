from datetime import datetime

codigoAgencia = 1
isentoIR = 'N'
user = 'INTEGPICPAY'
getDate = datetime.now()
tipoConta = 'I'
qtdTitular = 1
tipoTitular = 2
naoSei = 'sistema'

fields_mapper_FGC_TITULARES = {
    "dataBase": "DATA_BASE",
    "cnpjConglomerado": "CNPJ_IF",
    "naoSei": "SISTEMA",
    codigoAgencia: "CODAGENCIA",
    "numeroConta": "NROCONTA",
    "documentoCliente": "CPF_CNPJ",
    "nomeCliente": "NOMECLIENTE",
    isentoIR: "ISENTO_IR",
    "dataNascimentoCriacaoFundacao": "DATA_NASCIMENTO",
    user: "USUARIO",
    getDate: "DATAATUALIZACAO"
}

fields_mapper_FGC_CONTAS = {

    "dataBase": "DATA_BASE",
    "cnpjConglomerado": "CNPJ_IF",
    naoSei: "SISTEMA",
    "digitoAgencia": "CODAGENCIA",
    "numeroConta": "NROCONTA",
    "digitoConta": "DG_CONTA",
    user: "USUARIO",
    tipoConta: "TIPO_CONTA",
    qtdTitular: "QTD_TITULAR",
    tipoTitular: "TIPO_TITULARIDADE",
    getDate: "DATAATUALIZACAO",
    "identificacaoCliente": "IDENTIFICACAO_CLIENTE"
}

fields_mapper_FGC_ENDERECOS = {
    "dataBase": "DATA_BASE",
    "cnpjConglomerado": "CNPJ_IF",
    naoSei: "SISTEMA",
    "digitoAgencia": "CODAGENCIA",
    "numeroConta": "NROCONTA",
    "logradouro": "LOGRADOURO",
    "numero": "NUMERO",
    "bairro": "BAIRRO",
    "cidade": "CIDADE",
    "estado": "ESTADO",
    "cep": "CEP",
    user: "USUARIO",
    getDate: "DATAATUALIZACAO"
}

fields_mapper_FGC_PRODUTOS = {
    "dataBase": "DATA_BASE",
    "cnpjConglomerado": "CNPJ_IF",
    naoSei: "SISTEMA",
    "digitoAgencia": "CODAGENCIA",
    "numeroConta": "NROCONTA",
    "idProduto": "PRODUTO",
    "codigoInstrumentoFinanceiro": "COD_INSTRUMENTO",
    "dataAquisicao": "DATA_AQUISICAO",
    "dataVencimento": "DATA_VENCIMENTO",
    "quantidadeEmitida": "QTD_EMITIDA",
    "quantidadeDataBase": "QTD_DATABASE",
    "valorEmitido": "VALOR_EMITIDO",
    "valorAtualDataBase": "VALOR_DATABASE",
    "valorBloqueio": "VALOR_BLOQUEIO",
    user: "USUARIO",
    getDate: "DATAATUALIZACAO"
}



















