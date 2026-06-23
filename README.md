
### Nome: Sabrina Figueiredo Ferraz de Almeida
### Disciplinas: Análise e Projeto de Sistemas e Linguagem de Programação Orientada a Objetos

# Sistema de Gerenciamento Acadêmico
### Objetivo do Projeto

O objetivo do projeto é simular um sistema de gerenciamento acadêmico voltado para uma instituição de ensino. O sistema será responsável pelo gerenciamento de alunos, professores, disciplinas, avaliações e frequência, permitindo acompanhar o desempenho acadêmico dos estudantes.

Além disso, o sistema realizará o cálculo da média final dos alunos, exibirá informações como disciplinas cursadas, frequência, avaliações e resultados obtidos em cada disciplina. Também enviará notificações quando notas forem lançadas e quando o status final do aluno estiver disponível, podendo ser aprovado, em recuperação ou reprovado.

## Diagrama de Classes
<div align="center">
<img width="658" height="764" alt="image" src="https://github.com/user-attachments/assets/63e221fc-7a72-4455-9993-1377a7489b79" />
</div>

## Instruções de execução
O sistema é dividido em duas áreas principais: o painel de Administração/Professores e o Portal do Aluno. 

1. Cadastros Iniciais 

No menu superior, acesse Administração/Professores > "Professores" para cadastrar os docentes. Acesse "Alunos" para registrar os estudantes. É necessário informar Nome, Matrícula e E-mail (o e-mail será usado para envio do boletim). Acesse "Disciplinas" para criar as matérias. Você precisará vincular o professor responsável.

2. Matrículas

Vá em Administração/Professores > Matrículas. Selecione um Aluno e uma Disciplina para criar o vínculo entre eles no sistema.

3. Criação de Avaliações 

Acesse Criar Avaliações. Selecione a disciplina desejada e crie as avaliações.

4. Lançamento de Notas 

Acesse Registrar Notas dos Alunos. Selecione a matrícula do aluno. O sistema carregará automaticamente as avaliações pendentes daquela disciplina. Digite a nota obtida pelo aluno e clique em Salvar.

5. Fechamento de Boletim

Ao final do semestre, acesse Fechamento de Boletim. Selecione a matrícula do aluno e informe o número total de presenças que ele teve. Clique em "Calcular Fechamento". O sistema verificará se o aluno atingiu 75% de frequência e média 6.0, definindo se ele está Aprovado, em Recuperação ou Reprovado.

6. Portal do Aluno

O estudante deve acessar o menu Portal do Aluno > Acessar Portal. Basta digitar o seu número de matrícula. O sistema exibirá uma tela somente leitura com os dados do aluno.

### Conclusão
Durante o desenvolvimento do projeto, um dos principais desafios foi a etapa de análise e modelagem do sistema. Foi necessário identificar corretamente os requisitos funcionais, requisitos não funcionais e regras de negócio para que o sistema atendesse às necessidades de um ambiente acadêmico.

Outro desafio foi a elaboração dos diagramas UML, especialmente o diagrama de classes. Foi preciso revisar diversas vezes os relacionamentos entre as classes para garantir que a modelagem estivesse coerente com os requisitos definidos.

O desenvolvimento da modelagem ajudou a compreender melhor a estrutura do sistema antes da implementação, e como essa fase é importante para garantir uma implementação coerente. Diagramas bem elaborados ajudam a evitar retrabalho no futuro. 

Como melhorias futuras, o sistema pode ser expandido com novas funcionalidades e refinamentos. Por exemplo, abranger a segurança do sistema, criando uma obrigatoriedade de incluir senha e login para acessar o perfil e mostrar notas. 

### Declaração de uso de IA

ChatGPT: Utilizado para revisar os diagramas e detectar falhas ou melhorias.



