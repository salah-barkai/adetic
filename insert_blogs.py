import sqlite3

def insert_blogs():
    conn = sqlite3.connect('blog.sqlite')
    cursor = conn.cursor()
    blogs = [
        {
            'title': "Visite de travail entre l'ADETIC et la CNAS",
            'content': "Ce vendredi 29 mars 2024, le Directeur général de l’ADETIC, Adoum Djimet Saboun entouré de ses proches, a reçu une forte délégation de la Caisse Nationale d’Assurance Santé (CNAS). Laquelle délégation est conduite par le Directeur général, Singnyabé Barnabas et son adjoint Dr. Abdelsalam Hammad Djamouss.Au cœur des échanges, la délégation est venue solliciter l’accompagnement technique de l’ADETIC dans la mise œuvre effective de la couverture santé universelle au Tchad.Ainsi, dans les propos du Directeur général de la CNAS, l’on apprend qu’il y aura trois régimes à savoir l’Assurance santé des salariés, l’Assurance santé des indépendants et l’Assurance maladie des personnes démunies. C’est apporter un soin de qualité et équitable à toute la population sans aucune forme de discrimination, telle est la raison de la création de la Caisse Nationale d’Assurance Santé.",
            'image': "visite-cnas/n-dg.jpeg",
            'author': "Admin"
        },
        {
            'title': "L'ADETIC en visite au siège de Huawei à Shen Zen",
            'content': "Sur invitation du groupe Huawei , le Ministre des communications, de l’économie numérique et de la digitalisation de l’administration Dr Boukar Michel accompagné de ses proches collaborateurs séjourne depuis la date du 31 juillet dans la ville de shen Zen dans le cadre de la coopération numérique Sino-africaine .La délégation tchadienne a profité de son séjour pour visiter le siège de la géante société Huawei à Shen zen. Cette rencontre a consisté une opportunité prestigieuse pour la délégation tchadienne d’exposer des projets coopératifs auxquels les deux parties travailleront pour renforcer leurs capacités dans le domaine du numérique et aider le Tchad à implanter le modèle prometteur des Tic en faveur de l’accélération digitale et d’une économie prospère.Suite à cette rencontre un mémorandum M O U d’assistance technique pour la mise en exploitation du data center national ainsi que son backup, la formation et le transfert des compétences aux techniciens a été signé sous la supervision du ministre Dr Boukar Michel. La partie tchadienne était représenté par le DG de l’ADETIC Adoum djimet saboun et la partie Huawei par son vice-président LI JUNFENG.",
            'image': "chine/chine1.jpeg",
            'author': "Admin"
        },

        { 

            'title':"Une Visite de Terrain pour Constater l'Arrivée de 12 Pylones à Goudji" ,
            'content':"Informés de l’arrivée des 12 pylônes en provenance de l’entrepôt de la douane de Nguéli, le Secrétaire général du Ministère, Hissein Brahim Directeur général, Adoum Djimet Saboun et le Directeur de la Communication, Hissein Issa Rozi de l’Adetic se sont rendus à Goudji pour constater de visu l’arrivée desdits matériels.Il s’agit de 12 des 17 pylônes chargés dans cinq gros porteurs. Ces équipements de télécommunication sont commandés dans le cadre du projet du service universel. Une fois installés, ces pylônes vont desservis les zones du nord du pays non couvert par les opérateurs.Après la visite, le Directeur général de l’Adetic, Adoum Djimet Saboun est visiblement satisfait. Car dit-il se sent soulagé avec l’arrivée de ces pylônes dans la cour de l’entrepôt de Goudji.Pour ce faire, les techniciens en charge de la réalisation du projet ont été instruits par le Directeur général à l’effet à se mettre résolument au travail pour faire aboutir le projet dans un délai très raisonnable.Le Secrétaire général du Ministère, Hissein Brahim Abdelkérime, a abondé dans le même sens que le Directeur général en qui concerne l’accélération des travaux." ,
            'image': "terrain/visite1.jpeg",
            'author': "admin", 

        }, 

        { 
           'title': "Installation du nouveau DG de L'ADETIC",
           'content':"Le nouveau DG de l’ADETIC, Adoum Djimet Saboun, est installé.La cérémonie de passation de service présidée par l’Inspectrice générale du Ministère, a eu lieu ce mardi 12 mars 2024 dans les locaux de l’Agence de Développent des Technologies de l’Information et de la Communication (ADETIC), entre le Directeur général sortant, Ali Sidick Adam et Adoum Djimet Saboun. Nommé il y a juste une semaine, c’est-à-dire le 6 mars 2024 aux termes du décret N°0196/PT/PMT/MTEN/2024", 
           'image':"installation/dg.jpeg", 
           'author':"admin",

        },

        # Ajoute d'autres blogs ici
    ]

    for blog in blogs:
        cursor.execute('''
            INSERT INTO blogs (title, content, image, author)
            VALUES (?, ?, ?, ?)
        ''', (blog['title'], blog['content'], blog['image'], blog['author']))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    insert_blogs()
