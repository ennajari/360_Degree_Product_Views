import os

def print_directory_structure(path, indent=0):
    """
    Affiche la structure du répertoire de manière récursive.
    :param path: Le chemin du répertoire à afficher.
    :param indent: Niveau d'indentation pour la présentation.
    """
    try:
        # Liste les fichiers et répertoires dans le répertoire courant
        items = os.listdir(path)
        for item in items:
            # Crée le chemin complet
            item_path = os.path.join(path, item)
            # Affiche le nom de l'élément avec indentation
            print(' ' * indent + item)
            # Si l'élément est un répertoire, appelle récursivement la fonction
            if os.path.isdir(item_path):
                print_directory_structure(item_path, indent + 4)
    except PermissionError:
        print(' ' * indent + '[Accès refusé]')
    except FileNotFoundError:
        print(' ' * indent + '[Répertoire non trouvé]')

# Chemin du répertoire à afficher
directory_path = r'C:\Users\abdel\Desktop\360_Degree_Product_ViewsC'

# Affiche la structure du répertoire
print_directory_structure(directory_path)
