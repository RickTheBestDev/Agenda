from sqlite3 import Cursor
from typing import Self, Any, Optional
from models.database import Database

class Tarefa:
    """Classe que representa uma tarefa, com títulométodos para salvar, obter, escluir e atualizar
    tarefas em um banco nde dados usando a classe 'DataBase'.
    """

    def __init__(self: Self, titulo_tarefa: Optional[str], data_conclusao: Optional[str] = None,
      encerrado: Optional[int] = 0, id_tarefa: Optional[int]= None)-> None:
        self.titulo_tarefa: Optional[str] = titulo_tarefa
        self.data_conclusao: Optional[str] = data_conclusao
        self.encerrado: Optional[int] = encerrado
        self.id_tarefa: Optional[int] = id_tarefa

    @classmethod
    def id(cls, id: int)-> Self:
        with Database() as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao, encerrado FROM tarefas WHERE id = ?;'
            params: tuple = (id,)
            resultado = db.buscar_tudo(query, params)
            print(resultado)

            #desenpacotamento de coleção
            [[titulo, data, encerrado]] = resultado

        return cls(id_tarefa=id, titulo_tarefa=titulo, data_conclusao=data, encerrado=encerrado)
        
    def salvar_tarefa(self: Self)-> None:
        with Database() as db:
            query: str = " INSERT INTO tarefas (titulo_tarefa, data_conclusao, encerrado) VALUES (?, ?, ?);"
            params: tuple = (self.titulo_tarefa, self.data_conclusao, self.encerrado)
            db.executar(query, params)

    @classmethod
    def obter_tarefas(cls) -> list[Self]:
        with Database() as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao, encerrado, id FROM tarefas;'
            resultados: list[Any] = db.buscar_tudo(query)
            tarefas: list[Self] = [cls(titulo, data, encerrado, id) for titulo, data, encerrado, id in resultados]
            return tarefas
    
    
    def excluir_tarefa(self) -> Cursor:
        with Database() as db:
            query: str = 'DELETE FROM tarefas WHERE id = ?;'
            params: tuple = (self.id_tarefa,)
            resultado: Cursor = db.executar(query, params)
            return resultado

    def terminar_tarefa(self) -> Cursor:
        with Database() as db:
            query: str = 'UPDATE tarefas SET encerrado = 1 WHERE id = ?;'
            params: tuple = (self.id_tarefa,)
            resultado: Cursor = db.executar(query, params)
            return resultado    
        
    def abrir_tarefa(self) -> Cursor:
        with Database() as db:
            query: str = 'UPDATE tarefas SET encerrado = 0 WHERE id = ?;'
            params: tuple = (self.id_tarefa,)
            resultado: Cursor = db.executar(query, params)
            return resultado    

    def atualizar_tarefa(self) -> Cursor:
        with Database() as db:
            query: str = 'UPDATE tarefas SET titulo_tarefa = ?, data_conclusao = ?, encerrado = 0 WHERE id = ?;'
            params: tuple = (self.titulo_tarefa, self.data_conclusao, self.id_tarefa)
            resultado: Cursor = db.executar(query, params)
            return resultado 