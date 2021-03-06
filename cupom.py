nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"


def imprime_dados_loja():
    global numero
    # Implemente aqui

    if nome_loja == "":
        return "O campo nome da loja é obrigatório"

    if logradouro == "":
        return 'O campo logradouro do endereço é obrigatório'

    if numero == 0:
        numero = "s/n"

    if municipio == "":
        return 'O campo município do endereço é obrigatório'

    if estado == "":
        return 'O campo estado do endereço é obrigatório'
    
    if cnpj == "":
        return 'O campo CNPJ da loja é obrigatório'
    
    if inscricao_estadual == "":
        return 'O campo inscrição estadual da loja é obrigatório'

    output = f"{nome_loja}\n"
    output += f"{logradouro}, {numero} {complemento}\n"
    output += f"{bairro} - {municipio} - {estado}\n"
    output += f"CEP:{cep} Tel {telefone}\n"
    output += f"{observacao}\n"
    output += f"CNPJ: {cnpj}\n"
    output += f"IE: {inscricao_estadual}\n"

    return output
