# Projeto Myentertainmen List

__________________________________________________________________________
### Resumo

Diante da dificuldade em escolher o que assistir, e com uma lista de espera crescente, decidi aplicar o que venho estudando e desenvolver um aplicativo que armazena essa lista e realiza um sorteio aleatório de títulos a serem assistidos, sempre que solicitado. O aplicativo foi desenvolvido em **Python**, utilizando as bibliotecas **Pandas, tkinter, customtkinter e sqlite3.**

Escolhi o **SQLite** como banco de dados pela praticidade, mas a solução poderia ser adaptada para outros bancos. Também criei um executável, utilizando o **PyInstaller**, para que amigos possam usar o aplicativo sem a necessidade de instalar o Python.

## Diagrama

- O primeiro passo no desenvolvimento do aplicativo foi a modelagem do banco de dados. Iniciei com mais de 10 tabelas, e fui removendo as redundâncias. Ao final, cheguei a uma solução com apenas 4 tabelas.



## Operações

- Menu: A estrutura do menu principal foi dividida em cinco opções: **Cadastrar, Sortear, Alterar, Exportar e Sair. **

#### Cadastrar  
  - No menu de cadastro, são inseridos os dados dos programas a serem armazenados no banco de dados: nome, categoria, gênero, status, duração e responsável pelo cadastro. O **ID** foi configurado com autoincremento no SQLite, garantindo que a numeração seja gerada automaticamente, evitando erros.

#### Sorteador
  - A funcionalidade de sorteio realiza a escolha aleatória de um programa para ser assistido. O usuário tem seis opções de sorteio por categoria: *Aleatório (todas as categorias), Filme, Série, Anime, Dorama e Documentário.* Apenas programas com status "não assistido" são incluídos no sorteio, e, uma vez sorteados, o status é automaticamente alterado para "assistindo".

#### Alterar Status
  - Nesta função, o usuário pode alterar o status dos programas cadastrados.
 

#### Exportar Listas
  - A opção de exportação oferece cinco tipos de listas, baseadas no status dos programas, que podem ser exportadas para Excel: Completa(Todos status), Na fila, Assistindo, Assistido, Dropado. O sistema realiza uma consulta SQL automática, cujo retorno é armazenado em um data frame por meio da biblioteca Pandas, e posteriormente exportado para um arquivo Excel.


#### Sair
  - Esta opção encerra o programa.



  ### Conclusão

  Desenvolver este projeto foi uma experiência muito divertida. Consegui aplicar meus conhecimentos e lidar com erros inesperados, o que aprimorou meu raciocínio. Resolver todos os problemas encontrados foi bastante gratificante. Esta é apenas a primeira versão do aplicativo. Embora simples, atende à proposta inicial, e no futuro pretendo implementar novas funcionalidades.

![Screenshot_4](https://github.com/user-attachments/assets/68654000-fe63-48e3-ab98-75393f4f737d) 
![diagrama](https://github.com/user-attachments/assets/daa52a81-eaa5-40f2-bf7b-a51da1a7d210)

  


