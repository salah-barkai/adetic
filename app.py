import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)

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

# Route pour la page Blog
@app.route('/blog')
def blog():
    return render_template('blog.html')

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
