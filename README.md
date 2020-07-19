Plateforme du concours
==============

Interface web pour des concours de programmation.

## Origine
Clonée depuis la plate-forme utilisée par IP7 (association d'informatique de Paris Diderot / Université de Paris) le 19/07/2020.

Pour cette raison des mentions de IP7 ou de membres d'IP7 peuvent apparaître dans le dépôt.

## Comment utiliser ?
Une (très grosse) image docker a été prévue pour déployer le site partout. Pour lancer l'image et accéder au site sur le port `8080`:

```sh
$ docker build -t jpriou/ip7_concours .
$ docker run -p 8080:8080 --rm -d --privileged -v `pwd`/save:/home/ip7/save --name ip7_concours jpriou/ip7_concours
$ # Stop it : docker stop ip7_concours
$ # Remove save/ : docker exec --privileged ip7_concours sudo rm -rf /home/ip7/save
$ # Give good rights : docker exec --privileged ip7_concours sudo chown -R ip7:ip7 /home/ip7/save
```

### Tools

* Enter in shell
```
docker exec -it ip7_concours bash
```

* Set time /!\ Fonctionne en UTC (ie. Il faut mettre toute les heures - 1)
```
node update_data.js contest_start hours mins
node update_data.js contest_deadline hours mins
```

* Add a team
```
node insert_user.js name mdp
```
