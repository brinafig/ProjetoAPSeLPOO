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

RNF003 – Apenas usuários cadastrados como administradores ou professores podem criar, atualizar ou excluir dados acadêmicos.

RFN004- Apenas usuários cadastrados como administradores podem cadastrar disciplinas e vincular alunos e professores às disciplinas.

RNF005 – O tempo de resposta do sistema deve ser inferior a 3 segundos para qualquer operação.

RNF006 – O sistema deve estar disponível para acesso durante o período letivo.

### Regras de Negócio
RNE001 – A média mínima para aprovação é 6,0. Alunos com média igual ou superior a 6,0 serão considerados aprovados. Alunos com média inferior a 6,0 ficarão em recuperação.

RNE002 – Alunos em recuperação terão direito a realizar uma avaliação de recuperação. A média mínima para aprovação após a recuperação também será 6,0. Alunos com média inferior a 6,0 após a recuperação serão considerados reprovados.

RNE003 – O aluno deve possuir frequência mínima de 75% para aprovação na disciplina.

## Diagrama de Caso de Uso
<img width="700" height="720" alt="image" src="https://github.com/user-attachments/assets/380b1ac6-bce3-4f75-a73c-0851bc8a2bd1" />

### Documentação do Caso de Uso
<img width="542" height="842" alt="image" src="https://github.com/user-attachments/assets/9789d63e-06cb-456b-b76e-00d74e781401" />


<img width="545" height="754" alt="image" src="https://github.com/user-attachments/assets/23cb4a16-46cc-4115-ae63-c531ce540191" />


<img width="553" height="546" alt="image" src="https://github.com/user-attachments/assets/761e8d37-7079-47c6-a60a-f846438b54c1" />


<img width="562" height="844" alt="image" src="https://github.com/user-attachments/assets/20a262f6-e54a-4d8a-ac8c-d6204016ac2a" />


<img width="549" height="418" alt="image" src="https://github.com/user-attachments/assets/b752d31d-4b81-424a-bbc1-308884cd0efc" />







