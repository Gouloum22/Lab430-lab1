Dyaa Abou Arida 

## Rapport Labo 01
-----------------------------

**Question 1** : Quelles commandes avez-vous utilisées pour effectuer les opérations UPDATE et DELETE dans MySQL ? Avez-vous uniquement utilisé Python ou également du SQL ? Veuillez inclure le code pour illustrer votre réponse.


- Commandes MySQL:
 UPDATE: "UPDATE users SET email= %s, name= %s where id = %s"
 DELETE: "DELETE FROM users where id = %s"
 DELETE ALL: "DELETE FROM users"

- Il faut utiliser du code python pour ajouter les différentes options que l'utilisateur peut choisir. Ensuite il faut récuperer les informations entrées. Finalement, il faut envoyer ses informations et utiliser SQL pour modifier la base de donnée.

![alt text](image.png)
*Image 1.1 Code python du choix d'options*
![alt text](image-1.png)
*Image 1.2 Code python de l'entrée de l'utilisateur*
![alt text](image-2.png)
*Image 1.3 Code Python + SQL pour modifier la Base de donnée*

-------------------------------
**Question 2** : Quelles commandes avez-vous utilisées pour effectuer les opérations dans MongoDB ? Avez-vous uniquement utilisé Python ou également du SQL ? Veuillez inclure le code pour illustrer votre réponse.

Les commandes pour les opérations: 
- `find()` pour lire les utilisateurs;
- `insert_one()` pour ajouter un utilisateur;
- `update_one()` pour modifier un utilisateur;
- `delete_one()` pour supprimer un utilisateur;
- `delete_many({})` pour supprimer tous les utilisateurs.

J'ai uniquement utiliser du code python puisque j'ai utiliser la librairie pymongo qui sert d'intérmediaire entre mon code et la base de donnée.

![alt text](image-3.png)
*2.1 Image du code pythong pour modifier MongoDB*

-------------------------------
**Question 3** : Comment avez-vous implémenté votre product_view.py ? Est-ce qu’il importe directement la ProductDAO ? Veuillez inclure le code pour illustrer votre réponse.

product_view a été implémenté de la même façon que le user_view. Une approche MVC a été utilisée. La vue affiche uniquement les options du menu et de récuperer les données de l'utilisateur. Le controlleur est celui qui va intéragir avec le DAO et sert d'intérmediaire entre les deux.

![alt text](image-4.png)
*3.1 Image de l'implémentation de product_view.py*

![alt text](image-5.png)
*3.2 Image du Controlleur*

![alt text](image-6.png)
*3.3 Image du DAO*


**Question 4** : Si nous devions créer une application permettant d’associer des achats d'articles aux utilisateurs (Users → Products), comment structurerions-nous les données dans MySQL par rapport à MongoDB ?

Pour les structurer dans MySQL, il faudrait creer une table pour les utilisateurs, une pour les produits ainsi qu'une table pour les transactions (ou achats).

Exemple:

    CREATE TABLE purchases (

    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    purchase_date DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
    );


Pour MongoDB, il faudrait utiliser des collections séparées, et de garder en mémoire les identifiants qui sont liés.


## Partie Deploiement + CI/CD


La partie CI a été configurée sur Gitlab pour avoir un pipeline et donc execute automatiquement les tests lors d'un push.
![alt text](image-7.png)

La partie CD consistait à cloner le repo sur la machine virtuel et ensuite de lancer les conteneurs docker.
![alt text](image-8.png)

Commandes:
`cd /opt`
`git clone https://github.com/Gouloum22/Lab430-lab1.git`
`cd Lab430-lab1`
`nano .env`
`docker network create labo01-network`
`docker-compose down -v`
`docker-compose build`
`docker-compose up -d`
`docker ps`
`docker exec -it store_manager_cli pytest`