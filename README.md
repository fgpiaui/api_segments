# api_segments
### Instalação
1. Clone o projeto: https://github.com/fgpiaui/api_segments.git
2. Instale o python: https://www.python.org/downloads/
3. Crie uma Virtual Environment: 
   - No Pycharm: https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env
   - No Terminal: https://docs.python.org/3/library/venv.html
4. Rode pip install -r setup/requirements.txt no terminal, dentro do diretório do projeto
5. Verifique se a instalação ocorreu corretamente executando no terminal python manage.py runserver

### Estrutura de Dados
**Para execução dos endpoints fez-se necessário a definição de estrutura de dados para o carregamento deles.**
1. Cadastrar um objeto
   - Para cadastrar um objeto é necessário que seja feito um post nos endpoints definidos com a estrutura de dados do objeto a ser cadastrado:
     - Exemplo para objeto User:
     ```
     {
            'first_name': 'Filipe',
            'last_name': 'Rodrigues',
            'email': 'fgpiaui@gmail.com',
            'birth_date': date.today(),
            'admission_date': date.today(),
            'last_sign_in': datetime.now(),
            'is_active': True,
            'sex': MALE
     }
     ```
     - Exemplo para objeto Tag:
     ```
     {
            'name': 'Projeto',            
     }
     ```
     - Exemplo para objeto UserTag(Segments):
     ```
     {
            'user':1,
            'tag':1,
     }
     ```
2. Editar um objeto 
   - Para editar um objeto deve utilizar a seguinte estrutura em um POST a ser feito no endpoint definido.
   ```
   {
        'id':{ID},
        'field':{FIELD},
        'value':{VALUE},
   }
   ```
   **Onde {ID} é o id do objeto a ser atualizado,{FIELD} é um field a ser atualizado e {VALUE} é o value a ser atualizado**
3.  Deletar um objeto
    - Para deletar um objeto, deve-se passar o id dele, também via POST:
    ```
    {
        'id':{ID}
    }
    ```
4. Filtrar um objeto
   - Para filtrar um objeto e considerando que o filtro pode ser feito em qualquer campo e com qualquer tipo de filtragem, foi usado a seguinte estrutura de dados que satisfaz todo o universo:
   ```
     estrutura = [
      {
          'fields':[
              {
                  'field': {FIELD},
                  'value':{VALUE},
                  'type':{TYPE},
                  'operator':{OPERATOR},
              },
              ...
          ]
      },
      ...
    ]
   ```
   **{FIELD} corresponde a tabela concatenada com o field(formato tabela__field) que será filtrado, {VALUE} corresponde ao valor da condição, {TYPE} é uma lista de como será feito o filtro, {OPERATOR} é uma lista que informará a operação que o filtro será somada a outro filtro.**
   - Valores que {TYPE} pode conter
     - exact: Filtrará de modo que o valor passado deve corresponder exatamente ao valor do filtro
     - contains: Filtrará de modo que retornará valores que contenham o valor do filtro
     - starts_with: Filtrará os valores que comecem com o valor do filtro
     - ends_with: Filtrará os valores que terminam com o valor do filtro
     - date: Filtrará as datas, o valor aqui é um json que terá as chaves min_date e max_date. Caso não haja necessidade de filtrar um intervalo, so passar os valores iguais.
   - {OPERATOR}
     - and: Usará o operador lógico AND para concatenar o filtro anterior
     - or: Usará o operador lógico OR para concatenar o filtro anterior
     - not: Neste caso, o filtro será um AND e a negação do próximo filtro
     - nor: Neste caso, o filtro será um OR e a negação do próximo filtro
   - Exemplo: (Filtrar usuário que o first_name começa com A ou o last_name termina com A) ou (Filtrar usuario que nasceu antes de 2000)
   ```
   estrutura = [
      {
          'fields':[
              {
                  'field': 'user__first_name',
                  'value':'A',
                  'type':'starts_with',
                  'operator':'and',
              },
              {
                  'field': 'user__last_name',
                  'value':'A',
                  'type':'ends_with',
                  'operator':'or',
              },              
          ]
      },      
          'fields':[
              {
                  'field': 'user__birth_data',
                  'value':{'max_date':'1/1/2000'},
                  'type':'date',
                  'operator':'and',
              },        
          ]
      },
    ]
   ```

### URLs
1. localhost:8000/create_user/
    
    **Cria um usuario e deve passar no post a estrutura de dados de cadastro de usuario**
2. localhost:8000/create_tag/
    **Cria uma tag e deve passar no post a estrutura de dados de cadastro de tags**
3. localhost:8000/create_segments/
    **Cria um segmento e deve passar no post a estrutura de dados de cadastro de segmento**
4. localhost:8000/delete_user/
    **Deleta um usuario e deve passar a estrutura de dados de deleção de objeto**
5. localhost:8000/delete_tag/
    **Deleta um tag e deve passar a estrutura de dados de deleção de objeto**
6. localhost:8000/delete_segments/
    **Deleta um segmento e deve passar a estrutura de dados de deleção de objeto**
7. localhost:8000/edit_user/
    **Edita um usuario e deve passar a estrutura de dados de edição de objeto**
8. localhost:8000/edit_tag/
    **Edita um tag e deve passar a estrutura de dados de edição de objeto**
9. localhost:8000/edit_segments/
    **Edita um segmentos e deve passar a estrutura de dados de edição de objeto**
10. localhost:8000/filter/
    **Filtra um segmento e deve passar a estrutura de dados de filtragem, observando os detalhes de cada campo**

### Classes, Métodos e Arquivos
1. Models
    **Neste arquivo temos os modelos de cada entidade que serão mapeadas para o banco de dados. São 3 entidades criadas, User, Tag e UserTag que é a relação entre User e Tag (relação nxn)**
    
2. Views
    **Aqui temos os controllers de cada endpoint que irá redirecionar para as classes e métodos necessários para tratar a informação e retornar a resposta para o cliente**

3. Constantes
    **Aqui temos um arquivo com todos as constantes utilizadas para o código**

4. Serializers
    **Aqui criamos as classes que vão serializar os models e assim retornar as informações via post. Herda do models.Serializer do Django.**
  
5. Urls
    **Cria as urls e endpoints para redirecionar para uma view**
    
6. QueryBuilder
    **Cria as queries. Possui o método de update_query que vai atualizar o filtro a cada nova condição e concat_query que irá concatenar dois ou mais filtros **
7. QueryController
    **É o controller das queries, ou seja, quem irá chamar o construtor (querybuilder) e passar as informações necessárias para construir a query.**
8. EditData
    **Classe que serve para atualizar um objeto específico. Qualquer objeto será atualizado da mes**
9. Tests
    - **Aqui possui todos os testes, tanto unitários, quanto integrais. Os testes de views são integrais e pegam desde a entrada dos dados até a resposta da aplicação.**
    - **Temos também uma pasta que cria um cenário de teste (no caso dessa aplicação foi usado 500 usuarios e 15 tags). Os usuarios foram criados usando a bilioteca Faker do django. Foi usado um singleton para que todo o cenario de teste base seja o mesmo usado para os demais cenários de teste base, inclusive os de integração.
