'''

'''

'''
1. Conceitos Básicos

1.1 Introdução à POO

001 Crie uma classe Pessoa com atributos nome e idade, e um método para exibir essas informações.

002 Instancie objetos da classe Pessoa e teste a impressão dos dados.

003 Adicione um atributo email e um método para alterá-lo.

004 Crie um método falar() que exibe "Olá, meu nome é {nome}".

005 Crie um método aniversario() que aumenta a idade da pessoa em 1 ano.

006 Modifique a classe para que o atributo idade seja privado e acessado via métodos.

007 Utilize propriedades (@property) para acessar idade e email.

008 Crie um construtor alternativo que receba apenas o nome e defina a idade padrão como 18.

009 Adicione um método estático que retorna a quantidade total de objetos Pessoa criados.

010 Modifique a classe para incluir um atributo de classe total_pessoas que conte quantos objetos foram instanciados.

2. Herança e Polimorfismo

2.1 Criando Hierarquias de Classes

Crie uma classe Aluno que herda de Pessoa e tem um atributo matricula.

Modifique Aluno para ter um método estudar() que imprime uma mensagem personalizada.

Crie uma classe Professor que herda de Pessoa e tem um atributo disciplina.

Modifique Professor para ter um método ensinar() que imprime "Ensinando {disciplina}".

Crie uma classe Funcionario que herda de Pessoa e tem um atributo salario.

Adicione um método em Funcionario que calcula um aumento de 10% no salário.

Torne o atributo salario protegido e forneça um getter e um setter.

Modifique Funcionario para que o aumento de salário seja dinâmico (valor percentual passado como argumento).

Crie uma classe Gerente que herda de Funcionario e tem um atributo departamento.

Modifique Gerente para que o aumento de salário seja de 20% por padrão.

3. Encapsulamento e Abstração

Modifique Pessoa para tornar nome um atributo privado.

Crie uma interface Animal (classe abstrata) com um método fazer_som().

Crie classes Cachorro e Gato que herdam de Animal e implementam fazer_som().

Crie uma classe Veiculo com um método abstrato mover().

Implemente Carro e Bicicleta herdando de Veiculo.

Modifique Veiculo para incluir um atributo velocidade_maxima.

Adicione um método em Carro e Bicicleta que retorna a velocidade atual.

Crie uma classe ContaBancaria com métodos depositar() e sacar().

Modifique ContaBancaria para que o saldo seja privado e acessado por métodos.

Adicione um método transferir() entre contas.

4. Composição e Agregação

Crie uma classe Endereco e utilize-a dentro da classe Pessoa.

Adicione um atributo telefone na classe Pessoa.

Crie uma classe Pedido com uma lista de itens.

Adicione uma classe Item e relacione com Pedido.

Modifique Pedido para calcular o total dos itens.

Crie uma classe Turma que contém uma lista de alunos.

Adicione métodos para adicionar e remover alunos da turma.

Crie uma classe Empresa com uma lista de funcionários.

Adicione um método que retorna o total de funcionários da empresa.

Modifique Empresa para permitir busca de funcionários por nome.

5. Trabalhando com Arquivos

Crie um método para salvar dados de Pessoa em um arquivo.

Leia os dados salvos de um arquivo e instancie objetos Pessoa.

Modifique ContaBancaria para salvar histórico de transações em um arquivo.

Adicione um método para exportar pedidos de Pedido em CSV.

Leia os dados do CSV e instancie objetos Pedido e Item.

6. Projetos para Portfólio

Desenvolva um sistema de gerenciador de tarefas com CRUD.

Crie um sistema de autenticação com usuários e senhas criptografadas.

Implemente um sistema de controle de estoque para um pequeno negócio.

Desenvolva um gerenciador de clientes e pedidos para um restaurante.

Construa um sistema de reservas de hotel com classes Quarto, Cliente e Reserva.

Crie um bot de Telegram que responde a comandos personalizados.

Desenvolva um sistema de gestão de biblioteca com empréstimos de livros.

Construa uma API REST para um sistema de gerenciamento de vendas.

Desenvolva um sistema de monitoramento de sensores IoT com armazenamento de dados.

Implemente um sistema de marketplace simples com catálogo de produtos e carrinho de compras.
'''