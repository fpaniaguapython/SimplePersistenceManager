from datetime import datetime
from model.Usuario import Usuario
from persistence import UsuarioDAOFactory

if __name__ == '__main__':
    print("Iniciando la ejecución...")
    try:
        usuarioDAO = UsuarioDAOFactory.get_usuario_dao_impl()

        #APERTURA DE LA CONEXIÓN
        usuarioDAO.open_connection()

        # CREATE
        nuevo_usuario = Usuario(None, "Fernando", datetime.now(), 10023)
        usuarioDAO.create(nuevo_usuario)

        # READ ONE
        primer_usuario = usuarioDAO.read_one()
        print(primer_usuario)


        # READ_ALL
        usuarios = usuarioDAO.read_all()
        for usuario in usuarios:
            print(usuario)


        # UPDATE
        primer_usuario = usuarioDAO.read_one()
        primer_usuario.nombre += "_Mod"
        usuarioDAO.update(primer_usuario)

        #DELETE
        primer_usuario = usuarioDAO.read_one()
        usuarioDAO.delete(primer_usuario)

        #CIERRE DE LA CONEXIÓN
        usuarioDAO.close_connection()

    except Exception as e:
        print(type(e))
        print(f"Ha ocurrido un error de base de datos: {e}")