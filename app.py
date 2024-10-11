import os
from flask import Flask, render_template, request, redirect, url_for, flash,g
from flask_mail import Mail, Message
import sqlite3



app = Flask(__name__)

DATABASE = 'blog.sqlite'  # Chemin vers la base de données


app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'une_cle_secrete_aleatoire'

# Configuration sécurisée de Flask-Mail avec des variables d'environnement
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # Stocke ton email dans les variables d'environnement
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  # Stocke ton mot de passe dans les variables d'environnement
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

mail = Mail(app)

# Route pour la page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Route pour la page Agence
@app.route('/agence')
def agence():
    return render_template('agence.html')

@app.route('/voir-agence')
def voir_agence(): 
    return render_template('voir-agence.html')

# Route pour la page Projets
@app.route('/projets')
def projets():
    return render_template('projets.html')

# Route pour la page Carrières
@app.route('/carrieres')
def carrieres():
    return render_template('carrieres.html')

# Fonction pour se connecter à la base de données
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Fermer la connexion à la base de données
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Routes existantes...

# Route pour la page Blog
@app.route('/blog')
def blog():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, content, image, author FROM blogs')
    blogs = cursor.fetchall()
    # Transformer les données en une liste de dictionnaires
    blog_list = []
    for blog in blogs:
        blog_dict = {
            'id': blog[0],
            'title': blog[1],
            'content': blog[2],
            'image': blog[3],
            'author': blog[4]
        }
        blog_list.append(blog_dict)
    return render_template('blog.html', blogs=blog_list)

# Route pour afficher un blog spécifique
@app.route('/blog/<int:blog_id>')
def show_blog(blog_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, content, image, author FROM blogs WHERE id = ?', (blog_id,))
    blog = cursor.fetchone()
    if blog is None:
        return "Blog non trouvé", 404
    blog_dict = {
        'id': blog[0],
        'title': blog[1],
        'content': blog[2],
        'image': blog[3],
        'author': blog[4]
    }
    return render_template('voir-blog.html', blog=blog_dict)


# Route pour la page Contactez-nous
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/envoyer_contact', methods=['POST'])
def envoyer_contact():
    nom = request.form['nom']
    email = request.form['email']
    telephone = request.form['telephone']
    sujet = request.form['sujet']
    message = request.form['message']
    
    # Création du message email
    msg = Message(sujet, sender=email, recipients=[os.environ.get('MAIL_USERNAME')])
    msg.body = f"""
    Nom: {nom}
    Email: {email}
    Téléphone: {telephone}
    
    Message:
    {message}
    """
    
    # Envoi de l'email
    try:
        mail.send(msg)
        flash('Message envoyé avec succès', 'success')
    except Exception as e:
        flash(f"Une erreur s'est produite lors de l'envoi : {e}", 'danger')
    
    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True)
