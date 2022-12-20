class IUsuarioDAO:
    def open_connection(self, host, port, database, user, password):
        raise NotImplementedError

    def close_connection(self):
        raise NotImplementedError

    def create(self, usuario):
        raise NotImplementedError

    def read_one(self):
        raise NotImplementedError

    def read_all(self):
        raise NotImplementedError

    def update(self, usuario):
        raise NotImplementedError

    def delete(self, usuario):
        raise NotImplementedError