from flask import Flask, render_template

app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para la página de proyectos
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Ruta para la página de contacto
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)