# Projeto - TaskList (Done in 24:11🕐)
> Esse programa deve: criar e apagar tarefas, marcar e desmarcar como concluido. O programa deve salvar todas as alterações automaticamente.
> As tarefas possuem Título, Descrição e um Check.

## Tecnologias <img width="20" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" />
<div>  
  
    > Linguagem: Python

    > Bibliotecas: Flet (interface), sqlite3 (manipulação de banco de dados)

    > Banco de Dados: SQLite -> (armazenamento local)
</div>



## Funcionamento
Bom, o código começa na main; lá é feita a primeira configuração da página, é instanciada a classe AppWindow e inicializada a janela. 

A classe AppWindow constrói a interface principal, onde aparecem as tarefas e onde é possível adicionar novas tarefas. Nela, há eventos para adicionar, deletar, salvar e cancelar tarefas. 

A classe AddWindow mostra a interface para adicionar, ou não, alguma tarefa, bem simples mesmo.

A classe Task constrói o corpo das tarefas, onde guarda as informações como título, descrição e check, além dos eventos de editar, salvar, cancelar e checkar. 

A classe TaskDataManager (eita nome feio) possui todos os métodos necessários para manipular o banco de dados SQLite pelo Python, em resumo, encapsulamento. Também é a única classe que utilizei try/except; fiz isso por vários motivos, como falta de costume com try, medo de exagerar colocando muitos try pelo código e por eu não achar necessário usar try em outros casos, já que, se eles não funcionarem, o problema fui eu e não algum outro fator qualquer.


## Experiência
  Está funcionando. Demorei bastante, tive que ler bastante a documentação do Flet e quebrar bastante a cabeça em certas partes. Como eu não tinha muita prática com eventos, foi um pouco difícil entender o funcionamento de tudo e aplicar de uma forma minimamente agradável. Também há alguns problemas com o banco de dados; caso eu crie algo e rapidamente apague ou apenas tente mudar alguma informação, ele não atualiza. Não entendo e nem tive tempo de entender o porquê. 
  
> Note¹: Consegui resolver o problema e agora está funcionando corretamente. Basicamente adicionei um timer na classe TaskDataManager, que sempre que houver qualquer alteração no app ele espera um pouco antes de fechar a conexão e atualizar a interface. Além disso, criei um método privado na classe AppWindow que atualiza as tasks na interface a cada mudança. Assim, se por algum motivo não for possível deletar, adicionar, marcar ou editar uma task, ela simplesmente não será atualizada para o usuário. Essas duas mudanças eliminaram a necessidade de atualizar o app para que as alterações sejam aplicadas.
  

## Problemas
  Além do citado acima, tive alguns problemas envolvendo bugs complicados. Inicialmente, eu queria fazer com packeges separados para melhor organização. Entretanto, o Python ficava teimando que os arquivos não existiam, mesmo eu fazendo de tudo. Deve ter um detalhe muito específico que eu deixei passar, mas como eu não tinha tempo, deixei pra lá.

> Note²: acredito que consegui resolver, não fiz testes muito "profundos", mas parece funcionar da forma que deixei.
  
  Outro problema foi entender como funcionava o Flet, mais especificamente a organização na janela. Bugou bastante na primeira vez, mas acho que compreendi um pouco de como funciona. 
Também tive problemas para entender os eventos(e) no geral e ralei um pouco para resolvê-los.


## Uso de IA
  Utilizei o ChatGPT para me ajudar definir o projeto, as tecnologias, o corpo do código, tirar dúvidas e pedir ajuda sobre certas partes do código, como eu estou aprendendo e não tenho um professor para me guiar utilizei a IA e as documentações para concluir o projeto. 
  
  Fiquei copiando código do Chat? Não, só pedia a explicação e eu me virava com aquilo, utilizer a IA somente como ferramenta para entender melhor o que eu iria fazer.
  
  Até quis usar mais, mas o GitHub Copilot simplesmente não entendia nada de Flet, então só atrapalhava e me deixava ainda mais confuso. Entretanto, quando fui fazer os métodos da classe TaskDataManager, ele me poupou muito tempo, mas não porque eu não sabia o que fazer, mas porque era muita repetição. O próprio Copilot já sabia o que eu queria e, em um clique, eu já tinha o método. Claramente, não foi perfeito, mas era só ajustar melhor o método, corrigir uns detalhes e já estava funcionando.


## Conclusão
  Foi um resultado legal, nada muito bonito nem muito próximo do que eu imaginei, mas também eram só 24 horas. Acho que posso, e vou, melhorar meu entendimento geral em lógica; deixei a desejar em certos momentos e me perdi em vários. Isso provavelmente se deve ao fato de eu não querer simplesmente copiar qualquer projeto da internet, mas fazer um próprio, o que deu um certo grau de complexidade ao app. 
  
  Aprendi bastante coisa e, como primeiro projeto, acredito estar bom.


## Referências (as relevantes ao menos)
Documentação do Flet: https://flet.dev/docs/

Gerenciando banco de dados SQLite3 com Python by Regis da Silva: https://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html#conectando-e-desconectando-do-banco

Convert GUI App to Real Program - Python to exe to setup wizard by Python Simplifield: https://www.youtube.com/watch?v=p3tSLatmGvU

Icons: https://icons8.com/
