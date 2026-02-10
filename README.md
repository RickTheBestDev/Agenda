# Agenda em python usando Flask

Este projeto foi feito para adquirir aprendizado, como conceitos padrões de MC (Model-View-Controller), framework Flask e seus componentes, variaveis de ambiente, paradigma de programação orientado a objetos e reforço de fundamentos da linguagem de programação python.

Para implementar este projeto localmente, siga os seguintes passos:

1. Faça um fork desse repositorio, clicando no botao 'Fork'

2. Clone este repositorio localmente:

~~~~bash 
git clone<url_repositorio>
~~~~

3. abra o projeto utilizando seu IDE preferido

4. Crie, preferencialmente, um ambiente virtual utilizando uma versão do python
>3.12.10:

~~~bash
python -m venv .venv
~~~

5. Ative seu ambiente virtual. 

No bash:

~~~bash 
source .venv/Scripts/activate
~~~

No PowerShell:

~~powershell
.\.venv\Scripits\Activate.ps1

6. Instale todas as dependencias constantes no arquivo `requirements.txt`:

~~~python 
pip install -r requirements.txt
~~~

7. copie o arquivo `.env.example`, cole na raiz do projeto e renomeie a copia para `.env`.

8. Edite o arquivo `.env` para definir o caminho do seu banco de dados na constante `DATABASE`.exemplo:

~~env
DATABASE='./data/meubanco.db'

9. Rode a aplicação no python utilizando o comando 

~~~bash
flask run 
~~~

10. Acesse a aplicação no endereço e porta indicados no terminal. Exemplo 
`http://127.0.0.1:500`