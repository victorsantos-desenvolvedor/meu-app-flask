from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    mensagem = ""
    if request.method == 'POST':
        nome = request.form.get('usuario')
        mensagem = f"Bem-vindo(a), {nome}! O seu backend em Python está vivo! 🐍"

    html = '''
    <!DOCTYPE html>
    <html lang="pt-PT">
    <head>
        <meta charset="UTF-8">
        <title>Meu Site Python</title>
        <style>
            body { font-family: Arial; background-color: #1e1e2e; color: white; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .container { background-color: #2b2b3d; padding: 30px; border-radius: 12px; text-align: center; }
            input { padding: 10px; border-radius: 5px; border: none; margin-right: 10px; font-size: 16px; }
            button { padding: 10px 20px; background-color: #306998; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🐍 Servidor Web em Python</h1>
            <form method="POST">
                <input type="text" name="usuario" placeholder="Escreva o seu nome" required>
                <button type="submit">Enviar</button>
            </form>
            {% if mensagem %}<p style="color: #FFD43B; font-weight: bold; margin-top: 20px;">{{ mensagem }}</p>{% endif %}
        </div>
    </body>
    </html>
    '''
    return render_template_string(html, mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)
