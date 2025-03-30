from sqlalchemy.orm import Session

class Controller:
    def __init__(self, model,) -> None:
        self.model = model

    def delete_register_crud(self, id: str, db: Session) -> bool:
        """
        Deleta um registro específico pelo ID.
        Retorna True se o registro foi deletado, False se não foi encontrado.
        """

        try:
            # Verifica se o registro existe antes de deletar
            query = db.query(self.model).filter(self.model.id == id)
            if not query.first():
                return False 

            query.delete()
            db.commit() 
            return True 
        
        except Exception as e:
            db.rollback()  # Reverte mudanças em caso de erro
            return False
        

    
        