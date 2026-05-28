## Projeto Final de APS e LPOO

# Sistema de Gerenciamento Acadêmico
### Objetivo do Projeto

O objetivo do projeto é simular um sistema de gerenciamento acadêmico voltado para uma instituição de ensino. O sistema será responsável pelo gerenciamento de alunos, professores, disciplinas, avaliações e frequência, permitindo acompanhar o desempenho acadêmico dos estudantes.

Além disso, o sistema realizará o cálculo da média final dos alunos, exibirá informações como disciplinas cursadas, frequência, avaliações e resultados obtidos em cada disciplina. Também enviará notificações quando notas forem lançadas e quando o status final do aluno estiver disponível, podendo ser aprovado, em recuperação ou reprovado.

### Requisitos Funcionais
RF001 – O sistema deve permitir o cadastro de disciplinas.

RF002 – O sistema deve permitir vincular professores às disciplinas ministradas.

RF003 – O sistema deve permitir o cadastro de avaliações para cada disciplina.

RF004 – O sistema deve permitir a criação, leitura, atualização e exclusão dos dados cadastrados.

RF005 – O sistema deve listar todos os alunos cadastrados em uma disciplina.

RF006 – O sistema deve exibir todas as avaliações previstas em cada disciplina.

RF007 – O sistema deve permitir o registro e a consulta de presenças dos alunos.

RF008 – O sistema deve permitir que professores lancem notas dos alunos.

RF009 – O sistema deve calcular a média dos alunos da disciplina.

RF010 – O sistema deve permitir que o aluno visualize suas notas, médias, frequência e situação final na disciplina.

### Requisitos Não Funcionais
RNF001 – O sistema deve notificar o aluno quando notas forem postadas.

RNF002 – O sistema deve notificar o aluno quando o status final estiver disponível.

RNF003 – Apenas usuários cadastrados como professores podem criar, atualizar ou excluir dados acadêmicos.

RNF004 – O tempo de resposta do sistema deve ser inferior a 3 segundos para qualquer operação.

RNF005 – O sistema deve estar disponível para acesso durante o período letivo.

### Regras de Negócio
RNE001 – A média mínima para aprovação é 6,0. Alunos com média igual ou superior a 6,0 serão considerados aprovados. Alunos com média inferior a 6,0 ficarão em recuperação.

RNE002 – Alunos em recuperação terão direito a realizar uma avaliação de recuperação. A média mínima para aprovação após a recuperação também será 6,0. Alunos com média inferior a 6,0 após a recuperação serão considerados reprovados.

RNE003 – O aluno deve possuir frequência mínima de 75% para aprovação na disciplina.
