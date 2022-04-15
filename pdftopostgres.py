import os
import sys
import getopt

# https://pypi.org/project/psycopg2/
import psycopg2

def setFilename(file):
    try:
        if file.lower().find(".pdf") == -1:
            filename = file.lower()
        else :
            filename = file[0:file.find(".pdf")].lower()

        return filename
    except:
        print("Unexpected error:", sys.exc_info()[0])
        sys.exit(2)

# lien_deliberation
def set_lien_deliberation(conn,file):
    
    # 1. Recupérer gid_adresse_nommage
    cursor_gid_adresse_nommage = conn.cursor()
    cursor_gid_adresse_nommage.execute("SELECT adresse_nommage.gid FROM bar.adresse_nommage, bar.adresse_bal WHERE lower(adresse_bal.lien_deliberation) like '" + setFilename(file) + "' " + \
                "AND adresse_nommage.nom_source like adresse_bal.voie_nom " + \
                "AND adresse_nommage.etat_suppression is false " + \
                "AND adresse_nommage.code_insee like adresse_bal.commune_insee " + \
                "GROUP BY adresse_nommage.gid")
    
    # 2. Insérer dans adresse_nommage_media
    cursor_insert = conn.cursor()
    for record in cursor_gid_adresse_nommage:

        print(record[0])
        
        cursor_insert.execute(
            "INSERT INTO bar.adresse_nommage_media(nom_du_fichier,media,type,mediab,id_objet) " + \
            "VALUES (%(nom_du_fichier)s, 'Délibération','application/pdf', %(mediab)s, %(id_objet)s)",
            {
                "nom_du_fichier": file,
                "mediab": open('pj_to_integrate\\'+file,mode='rb').read(),
                "id_objet": record[0]
            }
        )

        conn.commit()
    
    cursor_gid_adresse_nommage.close()
    cursor_insert.close()

# lien_plan
def set_lien_plan(conn,file):

    # 1. Recupérer gid_adresse_nommage
    cursor_gid_adresse_nommage = conn.cursor()
    cursor_gid_adresse_nommage.execute("SELECT adresse_nommage.gid FROM bar.adresse_nommage, bar.adresse_bal WHERE lower(adresse_bal.lien_plan) like '" + setFilename(file) + "' " + \
                "AND adresse_nommage.nom_source like adresse_bal.voie_nom " + \
                "AND adresse_nommage.etat_suppression is false " + \
                "AND adresse_nommage.code_insee like adresse_bal.commune_insee " + \
                "GROUP BY adresse_nommage.gid")
    
    # 2. Insérer dans adresse_nommage_media
    cursor_insert = conn.cursor()
    for record in cursor_gid_adresse_nommage:

        print(record[0])
        
        cursor_insert.execute(
            "INSERT INTO bar.adresse_nommage_media(nom_du_fichier,media,type,mediab,id_objet) " + \
            "VALUES (%(nom_du_fichier)s, 'Plan','application/pdf', %(mediab)s, %(id_objet)s)",
            {
                "nom_du_fichier": file,
                "mediab": open('pj_to_integrate\\'+file,mode='rb').read(),
                "id_objet": record[0]
            }
        )

        conn.commit()
    
    cursor_gid_adresse_nommage.close()
    cursor_insert.close()

def set_lien_arrete_voie(conn,file):
    
    # 1. Recupérer gid_adresse_point
    cursor_gid_adresse_nommage = conn.cursor()
    cursor_gid_adresse_nommage.execute("SELECT adresse_nommage.gid FROM bar.adresse_nommage, bar.adresse_bal WHERE lower(adresse_bal.lien_arrete_voie) like '" + setFilename(file) + "' " + \
                "AND adresse_nommage.nom_source like adresse_bal.voie_nom " + \
                "AND adresse_nommage.etat_suppression is false " + \
                "AND adresse_nommage.code_insee like adresse_bal.commune_insee " + \
                "GROUP BY adresse_nommage.gid")
    
    # 2. Insérer dans adresse_point_media
    cursor_insert = conn.cursor()
    for record in cursor_gid_adresse_nommage:

        print(record[0])
        
        cursor_insert.execute(
            "INSERT INTO bar.adresse_nommage_media(nom_du_fichier,media,type,mediab,id_objet) " + \
            "VALUES (%(nom_du_fichier)s, 'Arrêté','application/pdf', %(mediab)s, %(id_objet)s)",
            {
                "nom_du_fichier": file,
                "mediab": open('pj_to_integrate\\'+file,mode='rb').read(),
                "id_objet": record[0]
            }
        )

        conn.commit()
        
    cursor_gid_adresse_nommage.close()
    cursor_insert.close()

def set_lien_arrete_num(conn,file):
    
    # 1. Recupérer gid_adresse_point
    cursor_gid_adresse_point = conn.cursor()
    cursor_gid_adresse_point.execute("SELECT adresse_point.gid FROM bar.adresse_nommage, bar.adresse_point, bar.adresse_bal " + \
                "WHERE adresse_nommage.gid = adresse_point.gid_adresse_nommage " + \
                "AND (adresse_bal.numero = adresse_point.numero " + \
	                "and ((adresse_bal.suffixe is null and  adresse_point.repetition is null) or (lower(adresse_bal.suffixe) like lower(adresse_point.repetition))) " + \
                    "and adresse_bal.voie_nom like adresse_nommage.nom_source " + \
                    "and adresse_bal.commune_insee like adresse_nommage.code_insee " + \
	            ") " + \
                "AND adresse_point.etat_suppression is false " + \
                "AND lower(adresse_bal.lien_arrete_num) = '" + setFilename(file) + "' " + \
                "GROUP BY adresse_point.gid")
    
    # 2. Insérer dans adresse_point_media
    cursor_insert = conn.cursor()
    for record in cursor_gid_adresse_point:

        print(record[0])
        
        cursor_insert.execute(
            "INSERT INTO bar.adresse_point_media(nom_du_fichier,media,type,mediab,id_objet) " + \
            "VALUES (%(nom_du_fichier)s, 'Arrêté','application/pdf', %(mediab)s, %(id_objet)s)",
            {
                "nom_du_fichier": file,
                "mediab": open('pj_to_integrate\\'+file,mode='rb').read(),
                "id_objet": record[0]
            }
        )

        conn.commit()

    # obsolète - deliberation_lien2
    cursor_gid_adresse_point = conn.cursor()
    cursor_gid_adresse_point.execute("SELECT adresse_point.gid FROM bar.adresse_nommage, bar.adresse_point, bar.adresse_bal " + \
                "WHERE adresse_nommage.gid = adresse_point.gid_adresse_nommage " + \
                "AND (adresse_bal.numero = adresse_point.numero " + \
	                "and ((adresse_bal.suffixe is null and  adresse_point.repetition is null) or (lower(adresse_bal.suffixe) like lower(adresse_point.repetition))) " + \
                    "and adresse_bal.voie_nom like adresse_nommage.nom_source " + \
                    "and adresse_bal.commune_insee like adresse_nommage.code_insee " + \
	            ")" + \
                "AND adresse_point.etat_suppression is false " + \
                "AND lower(adresse_bal.deliberation_lien2) = '" + setFilename(file) + "' " + \
                "GROUP BY adresse_point.gid")
    cursor_insert = conn.cursor()
    for record in cursor_gid_adresse_point:

        print(record[0])
        
        cursor_insert.execute(
            "INSERT INTO bar.adresse_point_media(nom_du_fichier,media,type,mediab,id_objet) " + \
            "VALUES (%(nom_du_fichier)s, 'Arrêté','application/pdf', %(mediab)s, %(id_objet)s)",
            {
                "nom_du_fichier": file,
                "mediab": open('pj_to_integrate\\'+file,mode='rb').read(),
                "id_objet": record[0]
            }
        )

        conn.commit()
        
    cursor_gid_adresse_point.close()
    cursor_insert.close()

def set_lien_certificat_num(conn,file):
    
    # 1. Recupérer gid_adresse_point
    cursor_gid_adresse_point = conn.cursor()
    cursor_gid_adresse_point.execute("SELECT adresse_point.gid FROM bar.adresse_nommage, bar.adresse_point, bar.adresse_bal " + \
                "WHERE adresse_nommage.gid = adresse_point.gid_adresse_nommage " + \
                "AND (adresse_bal.numero = adresse_point.numero " + \
	                "and ((adresse_bal.suffixe is null and  adresse_point.repetition is null) or (lower(adresse_bal.suffixe) like lower(adresse_point.repetition))) " + \
                    "and adresse_bal.voie_nom like adresse_nommage.nom_source " + \
                    "and adresse_bal.commune_insee like adresse_nommage.code_insee " + \
	            ")" + \
                "AND adresse_point.etat_suppression is false " + \
                "AND lower(adresse_bal.lien_certificat_num) = '" + setFilename(file) + "' " + \
                "GROUP BY adresse_point.gid")
    
    # 2. Insérer dans adresse_point_media
    cursor_insert = conn.cursor()
    for record in cursor_gid_adresse_point:

        print(record[0])
        
        cursor_insert.execute(
            "INSERT INTO bar.adresse_nommage_media(nom_du_fichier,media,type,mediab,id_objet) " + \
            "VALUES (%(nom_du_fichier)s, 'Certificat de numérotage','application/pdf', %(mediab)s, %(id_objet)s)",
            {
                "nom_du_fichier": file,
                "mediab": open('pj_to_integrate\\'+file,mode='rb').read(),
                "id_objet": record[0]
            }
        )

        conn.commit()
        
    cursor_gid_adresse_point.close()
    cursor_insert.close()

#################################################
# Main body of the program


def main(argv):

    print('')
    print('*** Start execution : PDF to PostgreSQL Database ***')
    print('')

    # Hostname postgres
    host = ''
    # Database postgres
    dbname = ''
    # User postgres
    user = ''
    # Password postgres
    password = ''

    print('----------------')
    print('1. Get arguments')
    # 1. Get arguments
    try:
        opts, args = getopt.getopt(argv, "h:d:u:p:", [
                                   "host=", "dbname=", "user=", "password="])
    except getopt.GetoptError as err:
        print(err)
        print(
            'usage : pdfopostgres.py -h <host> -d <dbname> -u <user> -p <password>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--host"):
            host = arg
        elif opt in ("-d", "--dbname"):
            dbname = arg
        elif opt in ("-u", "--user"):
            user = arg
        elif opt in ("-p", "--password"):
            password = arg

    print('host is', host)
    print('dbname is', dbname)
    print('user is', user)
    print('password is', password)

    print('----------------')
    print('2. Connect to database')
    # 2. Connect at database
    try:
        conn = psycopg2.connect(
            "host="+host+" dbname="+dbname+" user="+user+" password="+password)
    except psycopg2.OperationalError as err:
        print("Unable to connect at database")
        sys.exit(2)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        sys.exit(2)

    print('----------------')
    print('3. Read PJ to integrate')
    # 3. Lecture du répertoire à intégrer
    try :
        files = os.listdir('pj_to_integrate')
        print(files)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        sys.exit(2)

    print('----------------')
    print('4. Intégration en media GEO')
    # 4. Intégration en media GEO
    for file in files:

        print('### ' + file + ' ###')

    # Déliberation 
        print("---> Déliberation")
        set_lien_deliberation(conn,file)

    # Plan 
        print("---> Plan")
        set_lien_plan(conn,file)

    # Arrêté Voie 
        print("---> Arrêté Voie")
        set_lien_arrete_voie(conn,file)

    # Numérotation 
        print("---> Arrêté Numérotation")
        set_lien_arrete_num(conn,file)

    # Certificat de Numérotation 
        print("---> Certificat de Numérotation")
        set_lien_certificat_num(conn,file)

    # 5. Fermer la connexion
    try:
        conn.close()
    except:
        print("Unexpected error:", sys.exc_info()[0])

    print('')
    print('*** End execution ***')
    print('')

if __name__ == "__main__":
    main(sys.argv[1:])