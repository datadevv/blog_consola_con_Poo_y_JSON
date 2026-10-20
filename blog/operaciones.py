# blog/operaciones.py

def listar_posts(lista):
    if not lista:
        print("No hay posts para mostrar.")
        return []

    print("\nPosts disponibles:")
    for post in lista:
        autor = post.get("autor", {})
        if isinstance(autor, dict):
            nombre_autor = autor.get("nombre", "Desconocido")
        else:
            nombre_autor = "Desconocido"

        titulo = post.get("titulo", "Sin título")
        estado = post.get("estado", "Sin estado")
        print(f"- {titulo} | Autor: {nombre_autor} | Estado: {estado}")

    return lista


def buscar_por_titulo(lista, termino):
    if not termino:
        print("Debe ingresar un término de búsqueda.")
        return []

    termino = termino.strip().lower()
    resultados = []

    for post in lista:
        titulo = post.get("titulo", "")
        if isinstance(titulo, str) and termino in titulo.lower():
            resultados.append(post)

    if not resultados:
        print("No se encontraron resultados.")
        return []

    print("\nResultados por título:")
    for post in resultados:
        autor = post.get("autor", {})
        if isinstance(autor, dict):
            nombre_autor = autor.get("nombre", "Desconocido")
        else:
            nombre_autor = "Desconocido"

        print(f"- {post.get('titulo', 'Sin título')} | Autor: {nombre_autor} | Estado: {post.get('estado', 'Sin estado')}")

    return resultados


def filtrar_por_tag(lista, tag):
    if not tag:
        print("Debe ingresar un tag.")
        return []

    tag = tag.strip().lower()
    resultados = []

    for post in lista:
        tags = post.get("tags", [])
        if isinstance(tags, list):
            for tag_post in tags:
                if isinstance(tag_post, str) and tag_post.lower() == tag:
                    resultados.append(post)
                    break

    if not resultados:
        print("No se encontraron posts con ese tag.")
        return []

    print("\nPosts filtrados por tag:")
    for post in resultados:
        autor = post.get("autor", {})
        if isinstance(autor, dict):
            nombre_autor = autor.get("nombre", "Desconocido")
        else:
            nombre_autor = "Desconocido"

        print(f"- {post.get('titulo', 'Sin título')} | Autor: {nombre_autor} | Estado: {post.get('estado', 'Sin estado')}")

    return resultados