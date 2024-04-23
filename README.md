# TRÊS DESAFIOS DE ESTRUTURA DE DADOS
Este desáfio conta com três atividades que testam os conhecimentos dos instruídos em Python sobre Estruturas de Dados, como: funções, listas e dicionários.

## 1º Desafio - Recomendar Plano de Internet
Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude aos seus clientes a escolherem o plano de internet ideal com base em seu consumo mensal de dados. Para a resolução, você pode solicitar ao usuário que insira o seu consumo, sendo este um valor 'float'. Crie uma função chamada recomendar_plano para receber o consumo médio mensal de dados informado pelo cliente, além de utilizar estruturas condicionais para fazer a verificação e retornar o plano adequado.

### Planos Oferecidos
- Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.
- Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.
- Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.

## 2º Desafio - Criando uma Lista de Equipamentos
Você foi designado para desenvolver um programa para gerenciar os equipamentos de uma empresa. O objetivo é criar um solução que permita aos usuários inserir informações sobre os equipamentos que serão cadastrados na rede, em seguida, exibir essa lista de equipamentos. Crie uma Lista para armazenar esses equipamentos e depois um loop para solicitar ao usuário inserir até três equipamentos.

### Saída esperada
Após a entrada dos itens, o programa exibirá a lista de equipamentos inseridos pelo usuário. Cada equipamento será listado com um prefixo ( - ) de marcação para melhor organização.

| Entrada | Saída |
|---------|-------|
| | Lista de Equipamentos:|
| Antena | - Antena |
| Roteador | - Roteador |
| Switch | - Switch |
|         | Lista de Equipamentos:|
| Servidor | - Servidor |
| Cabinet Rack | - Cabinet Rack |
| Access Point | - Access Point |
|         | Lista de Equipamentos:|
| Edge Routers | - Edge Routers |
| Patch Cord | - Patch Cord |
| UPS | - UPS |

## 3º Desafio - Validando Número de Telefone
Imagine que você trabalha para uma empresa de telecomunicações e é responsável por validar se um número de telefone fornecido pelo cliente está em um formato correto. Para garantir a precisão dos registros, é essencial que os números de telefone estejam no formato padrão. Desenvolva uma função programa que valide se um número de telefone tem o formato correto.

### Planos Oferecidos
O formato aceito para números de telefone é: (XX) 9XXXX-XXXX, onde X representa um dígito de 0 a 9. Lembre-se de respeitar os espaços entre os números quando preciso.

#### Resolução
* Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
* Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html
* Regex simples para o entendimento: https://pt.stackoverflow.com/questions/46672/como-fazer-uma-express%C3%A3o-regular-para-telefone-celular
