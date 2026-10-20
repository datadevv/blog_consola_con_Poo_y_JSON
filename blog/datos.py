import json
import os

from .modelos import Blog, Post


def cargar_posts(ruta="posts.json"):
    if not os.path.exists(ruta):
        return Blog()

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        if not isinstance(datos, list):
            return Blog()

        posts = [Post.from_dict(post) for post in datos]
        return Blog(posts)

    except (json.JSONDecodeError, TypeError, ValueError):
        return Blog()


def guardar_posts(blog, ruta="posts.json"):
    try:
        datos = [post.to_dict() for post in blog.posts]
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Error al guardar: {e}")
        return False