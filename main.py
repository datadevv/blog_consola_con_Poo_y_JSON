from blog.datos import cargar_posts, guardar_posts
from blog.modelos import Autor, Post


def mostrar_menu():
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")


def mostrar_posts(posts):
    if not posts:
        print("No hay posts para mostrar.")
        return

    for post in posts:
        print(f"\nTítulo: {post.titulo}")
        print(f"Autor: {post.autor.nombre}")
        print(f"Estado: {post.estado}")
        print(f"Tags: {', '.join(post.tags)}")
        print(f"Contenido: {post.contenido}")


def crear_post(blog):
    titulo = input("Título: ").strip()
    contenido = input("Contenido: ").strip()
    nombre_autor = input("Autor: ").strip()
    bio = input("Bio: ").strip()
    tags_input = input("Tags (separados por coma): ").strip()
    estado = input("Estado (publicado/borrador/archivado): ").strip().lower()

    tags = [tag.strip().lower() for tag in tags_input.split(",") if tag.strip()] if tags_input else []

    autor = Autor(nombre_autor, bio)
    nuevo_post = Post(
        id=len(blog.posts) + 1,
        titulo=titulo,
        contenido=contenido,
        autor=autor,
        tags=tags,
        estado=estado
    )
    blog.agregar_post(nuevo_post)
    print("Post creado correctamente.")


def main():
    blog = cargar_posts()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_posts(blog.listar_posts())

        elif opcion == "2":
            termino = input("Ingrese el título a buscar: ").strip()
            mostrar_posts(blog.buscar_por_titulo(termino))

        elif opcion == "3":
            tag = input("Ingrese el tag: ").strip()
            mostrar_posts(blog.filtrar_por_tag(tag))

        elif opcion == "4":
            crear_post(blog)

        elif opcion == "5":
            resultados = blog.validar_posts()
            for item in resultados:
                print(f"\nTítulo: {item['titulo']}")
                if item["valido"]:
                    print("✅ Válido")
                else:
                    print("❌ Errores:")
                    for error in item["errores"]:
                        print(f"   - {error}")

        elif opcion == "6":
            if guardar_posts(blog):
                print("Posts guardados en posts.json.")
            else:
                print("No se pudo guardar.")

        elif opcion == "7":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()