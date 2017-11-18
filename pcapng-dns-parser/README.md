# pcapng-dns-parser
Il s'agit d'un petit script python pouvant parser un fichier .pcap/.pcapng, en extraire les réponses DNS et les formater dans un fichier .csv afin de pouvoir facilement les visualiser.
Il est basé sur le package python [scapy](http://scapy.readthedocs.io/en/latest/introduction.html).

## Requirements
Afin de pouvoir rapidement mettre ce script en oeuvre, un fichier `requirements.txt` est fourni. Il est possible d'utiliser l'utilitaire `pip` de python de la manière suivante:
```python
pip install -r requirements.txt
```
> NB: Il est vivement conseillé, mais pas obligatoire, d'utiliser `virtualenv` lors de l'installation des dépendances.

## Usage
Voici un exemple d'usage du script:
```python
python pcapng-dns-parser.py test.pcapng test.csv
```

Le premier argument est le fichier .pcap/.pcapng à parser et le second le chemin vers le fichier de sortie.

Le fichier de sortie sera semblable à ceci:
```text
www.example.net,A,,
,www.example.net.,1example.net
,1example.net.,XXX.XXX.XXX.XXX
,1example.net.,XXX.XXX.XXX.XXX
www.example.net,AAAA,,
,www.example.net.,XXXX:XXXX:XXXX:XXXX
```

Visualisation sous Gnumeric:

![alt text](example2.png)

La première ligne reprend le nom de domaine contenu dans la requête DNS associée à la réponse ainsi que le type de requête.
Les lignes suivantes contiennent les adresses IP ainsi que les éventuels alias.

Des informations utiles sont également affichées dans le terminal dans lequel le script est lancé. On y retrouve, entre autres, le nombre total de paquets trouvés dans le fichier de capture ansi que le nombre total de réponses DNS lues et écrites dans le fichier de sortie.

> /!\ Le nombre total de réponses DNS peut varier par rapport à celui repris dans le fichier de capture ! En effet, seules les requêtes ayant abouti sont reprises.

> NB: Cette version du script est suffisante pour la première étape du projet, mais une petite adaptation à venir est nécessaire pour la seconde étape.
