from persistence.UsuarioDAOPostgreSQL import UsuarioDAOPostgreSQL
from persistence.UsuarioDAOSQLite import UsuarioDAOSQLite


def get_usuario_dao_impl():
    return UsuarioDAOPostgreSQL()
    #return UsuarioDAOSQLite()