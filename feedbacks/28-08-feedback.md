# Parabéns Pedrinho! Ótima primeira versão. 

Claro, precisamos de alguns ajustes.

Começando por um detalhe importante:

1. Não há .gitignore o banco de dados não precisa ir pro git. Já criei um pra começar. Mas como o db.sqlite3 está dentro do git, você vai ter que fazer o git parar de trackear ele, e só então adicionar ele no .gitignore

## Bugs:

1. Na pasta de feedback há uma outra de prints. o 2 e 3 mostram bugs importantes. Vou deixar você quebrar a cabeça um pouco até segunda-feira.
2. O meraki_id pode ter letras, não pode ser IntegerField
3. Algumas entidades tem view ou urls de update e delete, mas não tem template... (inclusive bugou os delete por causa disso)

## Boas práticas:

1. Classe deviceAdmin no padrão Javascript. Faltou o D maiúsculo
2. As urls que criam objetos estão .../add/ - o padrão é /create/
3. Pode ajudar bastante em apps mais complexos colocar o context_object_name em views de update e detail também, como nas list view. Mas claro, no singular.
4. Os name das urls de create estão como "entidade_form" o padrão é "entidade_create"
5. O related_name nos campos que tem ForeignKey tem um padrão diferente do que usou. No fim das contas pode usar o que quiser, mas vou deixar vc encontrar o padrão ao longo do curso, não precisa arrumar agora.

## Melhorias:

1. Nos updates, os IDs aparecem como "título" do card. Deixa o app mais inseguro, o usuário final não precisa saber os ids da aplicação (apesar de estar na url também, anyway haha). O ideal é o nome do objeto mesmo, fica mais bonito.
2. O campo id no Django já é automático, os campos created_at e updated_at também, se precisar usar eles. Não precisa escrever ele na unha. Só detalhe, em desafios próximos você vai tratar isso de forma mais legal.
3. O Django admin ajuda muito, principalmente durante os testes em desenvolvimento. Vale investir um tempinho para aumentar as opções de busca por lá, por exemplo. produtos por categoria, devices por produtos, categoria, brand, etc...
4. Você criou um template "entidade_form.html" e usou ele para create e para update. Em apps mais complexos isso pode dar zica, ou na verdade você vai querer usar templates diferentes, campos diferentes e pa...
5. Besteira de frontend no Screenshot1, nem eu sei arrumar hahaha

### Lembrando que o próximo desafio é cumulativo, então continua nesse projeto mesmo!