from flask import Flask, render_template
import feedparser

# Creamos la app
app = Flask(__name__)

# Ruta principal (la web)
@app.route("/")
def index():

    # RSS del periódico
    url = "https://www.diariodealmeria.es/rss/"

    # Leer RSS
    feed = feedparser.parse(url)

    noticias = []

    # Recorrer noticias
    for entry in feed.entries:
        print(entry.link)
        noticias.append({
            "titulo": entry.title,
            "link": entry.link,
            "resumen": entry.summary
        })

    # Enviar datos al HTML
    return render_template("index.html", noticias=noticias)


# Ejecutar servidor
if __name__ == "__main__":
    app.run(debug=True)