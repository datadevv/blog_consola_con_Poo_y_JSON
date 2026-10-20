# blog/validaciones.py

from blog.datos import estados_post

def validar_post(post):
    if not isinstance(post, dict):
        return False, "No es un diccionario."

    claves_obligatorias = ["id", "titulo", "contenido", "autor", "tags", "estado"]

    for clave in claves_obligatorias:
        if clave not in post:
            return False, f"Falta la clave '{clave}'."

    if not isinstance(post["titulo"], str) or not post["titulo"].strip():
        return False, "El título está vacío."

    if not isinstance(post["contenido"], str) or not post["contenido"].strip():
        return False, "El contenido está vacío."

    if not isinstance(post["autor"], dict):
        return False, "El autor no es un diccionario."

    if "nombre" not in post["autor"] or not str(post["autor"]["nombre"]).strip():
        return False, "El autor no tiene nombre válido."

    if not isinstance(post["tags"], list):
        return False, "Los tags no son una lista."

    if not all(isinstance(tag, str) for tag in post["tags"]):
        return False, "Los tags deben ser cadenas de texto."

    if post["estado"] not in estados_post:
        return False, "El estado no pertenece a los valores permitidos."

    return True, "válido"


def validar_posts(lista):
    if not lista:
        print("No hay posts para validar.")
        return []

    print("\nValidación de posts:")
    for i, post in enumerate(lista, start=1):
        valido, mensaje = validar_post(post)
        if valido:
            print(f"Post {i}: válido")
        else:
            print(f"Post {i}: error - {mensaje}")

    return lista