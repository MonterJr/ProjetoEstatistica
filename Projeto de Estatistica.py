novo_arquivo = open('teste.txt', 'w')
novo_arquivo.write(
    'Nome' + ' , ' + 'Idade' + ' , ' + 'Sexo' + ' , ' + 'Peso' + ' , ' + 'Cidade' + ' , ' + 'Estado Civil' + ' , ' + 'QTD Filhos' + ' , '
                                                                                                                                    'Escolaridade' + ' , ' + 'Emprego Formal' + ' , ' + 'Renda' + ' , ' + 'Imovel' + ' , ' + 'Tipo de Imovel' +
    ' , ' + 'Pegou Covid' + ' , ' + 'Imunização Completa' + '\n')
op = 0
while (op != 1):

    nome = input('1- Qual o seu nome e sobrenome? EX.: Elias Monteiro ')
    novo_arquivo.write(nome + ' , ')

    idade = input('2- Digite qual sua idade? EX.: 21 ')
    novo_arquivo.write(idade + ' , ')

    sexo = input('3- Qual sexo você se identifica? Podendo ser somente: (Masculino), (Feminino) ou (Trânsgero) ')
    novo_arquivo.write(sexo + ' , ')

    peso = input('4- Qual o seu peso atual? EX.: 90.0, 74.3, 86.7 ')
    novo_arquivo.write(peso + ' , ')

    cidade = input('5- Qual cidade você mora atualmente? EX.: Recife, Olinda, Jaboatão dos Guararapes ')
    novo_arquivo.write(cidade + ' , ')

    est_civil = input(
        '6- Qual o seu estado civil? Podendo ser somente: (Solteiro), (Casado), (Separado), (Viúvo) ou (Divorciado) ')
    novo_arquivo.write(est_civil + ' , ')

    qtd_filhos = input('7- Quantos filhos você tem? Podendo ser somente: (0), (1), (2), ou (3+) ')
    novo_arquivo.write(qtd_filhos + ' , ')

    nivel_escolar = input('8- Qual o seu nível de escolaridade? EX.: Analfabeto, Funtamental Completo ou Incompleto ')
    novo_arquivo.write(nivel_escolar + ' , ')

    emprego = input('9- Você tem emprego formal? Podendo ser somente: (SIM) ou (NÃO) ')
    novo_arquivo.write(emprego + ' , ')

    renda = input(
        '10- Qual sua renda atual? Podendo ser somente: (Sem renda), (Menos 1.212), (1.212 - 2.424), (2.424 - 4.848), (Acima 4.848) ou (Prefiro não informar) ')
    novo_arquivo.write(renda + ' , ')

    onde_mora = input('11- Onde você mora o imóvel é próprio ou alugado? Podendo ser somente: (Próprio) ou (Alugado) ')
    novo_arquivo.write(onde_mora + ' , ')

    mora_em = input('12- Você mora em casa ou apartamento? Podendo ser somente: (Casa) ou (Apartamento) ')
    novo_arquivo.write(mora_em + ' , ')

    covid = input('13- Você já pegou Covid-19? Podendo ser somente: (SIM) ou (NÃO) ')
    novo_arquivo.write(covid + ' , ')

    vacina = input('14- Você já tomou todas as doses da vacina? Podendo ser somente: (SIM) ou (NÃO) ')
    novo_arquivo.write(vacina)

    novo_arquivo.write('\n')

    r = input('Você quer adicionar mais alguma resposta? ')
    if r == 'não' or r == 'NÃO' or r == 'Não' or r == 'NAO' or r == 'nao' or r == 'Nao':
        op = 1

novo_arquivo.close()