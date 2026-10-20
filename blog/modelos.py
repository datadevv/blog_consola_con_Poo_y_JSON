class Autor:
    def __init__(self, nombre, bio=""):
        self.nombre = nombre
        self.bio = bio

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio
        }

    @classmethod
    def from_dict(cls, data):
        if not isinstance(data, dict):
            return cls("Sin autor", "")
        return cls(
            data.get("nombre", "Sin autor"),
            data.get("bio", "")
        )


class Post:
    def __init__(self, id, titulo, contenido, autor, tags, estado):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict(),
            "tags": self.tags,
            "estado": self.estado
        }

    @classmethod
    def from_dict(cls, data):
        autor = Autor.from_dict(data.get("autor", {}))
        return cls(
            data.get("id", 0),
            data.get("titulo", ""),
            data.get("contenido", ""),
            autor,
            data.get("tags", []),
            data.get("estado", "borrador")
        )


class Blog:
    def __init__(self, posts=None):
        self.posts = posts if posts is not None else []

    def listar_posts(self):
        return self.posts

    def buscar_por_titulo(self, texto):
        texto = texto.strip().lower()
        return [post for post in self.posts if texto in post.titulo.lower()]

    def filtrar_por_tag(self, tag):
        tag = tag.strip().lower()
        return [post for post in self.posts if any(t.lower() == tag for t in post.tags)]

    def agregar_post(self, post):
        self.posts.append(post)

    def validar_post(self, post):
        errores = []

        if not isinstance(post, Post):
            return ["El post no es válido."]

        if not post.titulo or not post.titulo.strip():
            errores.append("Falta título.")

        if not post.contenido or not post.contenido.strip():
            errores.append("Falta contenido.")

        if not isinstance(post.autor, Autor) or not post.autor.nombre.strip():
            errores.append("Falta autor.")

        if not isinstance(post.tags, list):
            errores.append("Los tags deben estar en una lista.")

        if post.estado not in ("publicado", "borrador", "archivado"):
            errores.append("Estado inválido.")

        return errores

    def validar_posts(self):
        resultados = []
        for post in self.posts:
            errores = self.validar_post(post)
            resultados.append({
                "titulo": post.titulo,
                "valido": len(errores) == 0,
                "errores": errores
            })
        return resultados