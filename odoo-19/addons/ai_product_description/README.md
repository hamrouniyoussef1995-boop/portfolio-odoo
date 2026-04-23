Odoo AI Product Assistant

Ce module est développé sur Odoo 19 Community.

Il permet d’intégrer l’intelligence artificielle dans Odoo afin de générer automatiquement des descriptions produits professionnelles et optimisées.


Objectif : 

Automatiser la création de contenu produit grâce à l’IA afin de :
- gagner du temps sur la saisie manuelle
- améliorer la qualité des descriptions produits
- standardiser les contenus dans l’ensemble du catalogue


Fonctionnement : 

Le module utilise une API d’intelligence artificielle pour générer les descriptions à partir des informations du produit (nom, catégorie, etc.).

Configuration de la clé API : 

Pour utiliser ce module, vous devez générer une clé API depuis OpenAI :

1. Créez un compte sur la plateforme OpenAI  
2. Générez votre clé API depuis la section API Keys
3. Copiez la clé générée  

Ensuite, dans Odoo :

1. Activez le mode développeur  
2. Allez dans :  
   Paramètres → Technique → Paramètres système
3. Ajoutez une nouvelle entrée :

| Clé | Valeur |
| `openai_api_key` | votre_clé_api |

Utilisation :

1. Ouvrir une fiche produit  
2. Cliquer sur "Générer description IA"
3. La description est automatiquement générée et enregistrée dans Odoo  


Stack technique :

- Odoo 19 Community  
- Python  
- API REST  
- Intelligence Artificielle (LLM)

Sécurité : 

- La clé API n’est pas stockée dans le code  
- Elle est gérée via les paramètres système Odoo  
- Compatible environnement production  

 Auteur : 

Développé par Youssef Hamrouni