import random as rd
import time
from timeit import default_timer as timer

txt = open("Generation.txt","ab")

prenom = ["Bulbizarre","Herbizarre","Florizarre","Salamèche","Reptincel","Dracaufeu","Carapuce","Carabaffe","Tortank","Chenipan","Chrysacier","Papilusion","Aspicot","Coconfort","Dardargnan","Roucool","Roucoups","Roucarnage","Rattata","Rattatac","Piafabec","Rapasdepic","Abo","Arbok","Pikachu","Raichu","Sabelette","Sablaireau","Nidoran♀","Nidorina","Nidoqueen","Nidoran♂","Nidorino","Nidoking","Mélofée","Mélodelfe","Goupix","Feunard","Rondoudou","Grodoudou","Nosferapti","Nosferalto","Mystherbe","Ortide","Rafflesia","Paras","Parasect","Mimitoss","Aéromite","Taupiqueur","Triopikeur","Miaouss","Persian","Psykokwak","Akwakwak","Férosinge","Colossinge","Caninos","Arcanin","Ptitard","Têtarte","Tartard","Abra","Kadabra","Alakazam","Machoc","Machopeur","Mackogneur","Chétiflor","Boustiflor","Empiflor","Tentacool","Tentacruel","Racaillou","Gravalanch","Grolem","Ponyta","Galopa","Ramoloss","Flagadoss","Magnéti","Magnéton","Canarticho","Doduo","Dodrio","Otaria","Lamantine","Tadmorv","Grotadmorv","Kokiyas","Crustabri","Fantominus","Spectrum","Ectoplasma","Onix","Soporifik","Hypnomade","Krabby","Krabboss","Voltorbe","Électrode","Noeunoeuf","Noadkoko","Osselait","Ossatueur","Kicklee","Tygnon","Excelangue","Smogo","Smogogo","Rhinocorne","Rhinoféros","Leveinard","Saquedeneu","Kangourex","Hypotrempe","Hypocéan","Poissirène","Poissoroy","Stari","Staross","M. Mime","Insécateur","Lippoutou","Élektek","Magmar","Scarabrute","Tauros","Magicarpe","Léviator","Lokhlass","Métamorph","Évoli","Aquali","Voltali","Pyroli","Porygon","Amonita","Amonistar","Kabuto","Kabutops","Ptéra","Ronflex","Artikodin","Électhor","Sulfura","Minidraco","Draco","Dracolosse","Mewtwo","Mew","Germignon","Macronium","Méganium","Héricendre","Feurisson","Typhlosion","Kaiminus","Crocrodil","Aligatueur","Fouinette","Fouinar","Hoothoot","Noarfang","Coxy","Coxyclaque","Mimigal","Migalos","Nostenfer","Loupio","Lanturn","Pichu","Mélo","Toudoudou","Togepi","Togetic","Natu","Xatu","Wattouat","Lainergie","Pharamp","Joliflor","Marill","Azumarill","Simularbre","Tarpaud","Granivol","Floravol","Cotovol","Capumain","Tournegrin","Héliatronc","Yanma","Axoloto","Maraiste","Mentali","Noctali","Cornèbre","Roigada","Feuforêve","Zarbi","Qulbutoké","Girafarig","Pomdepik","Foretress","Insolourdo","Scorplane","Steelix","Snubbull","Granbull","Qwilfish","Cizayox","Caratroc","Scarhino","Farfuret","Teddiursa","Ursaring","Limagma","Volcaropod","Marcacrin","Cochignon","Corayon","Rémoraid","Octillery","Cadoizo","Démanta","Airmure","Malosse","Démolosse","Hyporoi","Phanpy","Donphan","Porygon2","Cerfrousse","Queulorior","Debugant","Kapoera","Lippouti","Élekid","Magby","Écrémeuh","Leuphorie","Raikou","Entei","Suicune","Embrylex","Ymphect","Tyranocif","Lugia","Ho-Oh","Celebi","Arcko","Massko","Jungko","Poussifeu","Galifeu","Braségali","Gobou","Flobio","Laggron","Medhyèna","Grahyèna","Zigzaton","Linéon","Chenipotte","Armulys","Charmillon","Blindalys","Papinox","Nénupiot","Lombre","Ludicolo","Grainipiot","Pifeuil","Tengalice","Nirondelle","Hélédelle","Goélise","Bekipan","Tarsal","Kirlia","Gardevoir","Arakdo","Maskadra","Balignon","Chapignon","Parecool","Vigoroth","Monaflèmit","Ningale","Ninjask","Munja","Chuchmur","Ramboum","Brouhabam","Makuhita","Hariyama","Azurill","Tarinor","Skitty","Delcatty","Ténéfix","Mysdibule","Galekid","Galegon","Galeking","Méditikka","Charmina","Dynavolt","Élecsprint","Posipi","Négapi","Muciole","Lumivole","Rosélia","Gloupti","Avaltout","Carvanha","Sharpedo","Wailmer","Wailord","Chamallot","Camérupt","Chartor","Spoink","Groret","Spinda","Kraknoix","Vibraninf","Libégon","Cacnea","Cacturne","Tylton","Altaria","Mangriff","Séviper","Séléroc","Solaroc","Barloche","Barbicha","Écrapince","Colhomard","Balbuto","Kaorine","Lilia","Vacilys","Anorith","Armaldo","Barpau","Milobellus","Morphéo","Kecleon","Polichombr","Branette","Skelénox","Téraclope","Tropius","Éoko","Absol","Okéoké","Stalgamin","Oniglali","Obalie","Phogleur","Kaimorse","Coquiperl","Serpang","Rosabyss","Relicanth","Lovdisc","Draby","Drackhaus","Drattak","Terhal","Métang","Métalosse","Regirock","Regice","Registeel","Latias","Latios","Kyogre","Groudon","Rayquaza","Jirachi","Deoxys","Tortipouss","Boskara","Torterra","Ouisticram","Chimpenfeu","Simiabraz","Tiplouf","Prinplouf","Pingoléon","Étourmi","Étourvol","Étouraptor","Keunotor","Castorno","Crikzik","Mélokrik","Lixy","Luxio","Luxray","Rozbouton","Roserade","Kranidos","Charkos","Dinoclier","Bastiodon","Cheniti","Cheniselle","Papilord","Apitrini","Apireine","Pachirisu","Mustébouée","Mustéflott","Ceribou","Ceriflor","Sancoki","Tritosor","Capidextre","Baudrive","Grodrive","Laporeille","Lockpin","Magirêve","Corboss","Chaglam","Chaffreux","Korillon","Moufouette","Moufflair","Archéomire","Archéodong","Manzaï","Mime Jr.","Ptiravi","Pijako","Spiritomb","Griknot","Carmache","Carchacrok","Goinfrex","Riolu","Lucario","Hippopotas","Hippodocus","Rapion","Drascore","Cradopaud","Coatox","Vortente","Écayon","Luminéon","Babimanta","Blizzi","Blizzaroi","Dimoret","Magnézone","Coudlangue","Rhinastoc","Bouldeneu","Élekable","Maganon","Togekiss","Yanmega","Phyllali","Givrali","Scorvol","Mammochon","Porygon-Z","Gallame","Tarinorme","Noctunoir","Momartik","Motisma","Créhelf","Créfollet","Créfadet","Dialga","Palkia","Heatran","Regigigas","Giratina","Cresselia","Phione","Manaphy","Darkrai","Shaymin","Arceus","Victini","Vipélierre","Lianaja","Majaspic","Gruikui","Grotichon","Roitiflam","Moustillon","Mateloutre","Clamiral","Ratentif","Miradar","Ponchiot","Ponchien","Mastouffe","Chacripan","Léopardus","Feuillajou","Feuiloutan","Flamajou","Flamoutan","Flotajou","Flotoutan","Munna","Mushana","Poichigeon","Colombeau","Déflaisan","Zébibron","Zéblitz","Nodulithe","Géolithe","Gigalithe","Chovsourir","Rhinolove","Rototaupe","Minotaupe","Nanméouïe","Charpenti","Ouvrifier","Bétochef","Tritonde","Batracné","Crapustule","Judokrak","Karaclée","Larveyette","Couverdure","Manternel","Venipatte","Scobolide","Brutapode","Doudouvet","Farfaduvet","Chlorobule","Fragilady","Bargantua","Mascaïman","Escroco","Crocorible","Darumarond","Darumacho","Maracachi","Crabicoque","Crabaraque","Baggiguane","Baggaïd","Cryptéro","Tutafeh","Tutankafer","Carapagos","Mégapagos","Arkéapti","Aéroptéryx","Miamiasme","Miasmax","Zorua","Zoroark","Chinchidou","Pashmilla","Scrutella","Mesmérella","Sidérella","Nucléos","Méios","Symbios","Couaneton","Lakmécygne","Sorbébé","Sorboul","Sorbouboul","Vivaldaim","Haydaim","Emolga","Carabing","Lançargot","Trompignon","Gaulet","Viskuse","Moyade","Mamanbo","Statitik","Mygavolt","Grindur","Noacier","Tic","Clic","Cliticlic","Anchwatt","Lampéroie","Ohmassacre","Lewsor","Neitram","Funécire","Mélancolux","Lugulabre","Coupenotte","Incisache","Tranchodon","Polarhume","Polagriffe","Hexagel","Escargaume","Limaspeed","Limonde","Kungfouine","Shaofouine","Drakkarmin","Gringolem","Golemastoc","Scalpion","Scalproie","Frison","Furaiglon","Gueriaigle","Vostourno","Vaututrice","Aflamanoir","Fermite","Solochi","Diamat","Trioxhydre","Pyronille","Pyrax","Cobaltium","Terrakium","Viridium","Boréas","Fulguris","Reshiram","Zekrom","Démétéros","Kyurem","Keldeo","Meloetta","Genesect","Marisson","Boguérisse","Blindépique","Feunnec","Roussil","Goupelin","Grenousse","Croâporal","Amphinobi","Sapereau","Excavarenne","Passerouge","Braisillon","Flambusard","Lépidonille","Pérégrain","Prismillon","Hélionceau","Némélios","Flabébé","Floette","Florges","Cabriolaine","Chevroum","Pandespiègle","Pandarbare","Couafarel","Psystigri","Mistigrix","Monorpale","Dimoclès","Exagide","Fluvetin","Cocotine","Sucroquin","Cupcanaille","Sepiatop","Sepiatroce","Opermine","Golgopathe","Venalgue","Kravarech","Flingouste","Gamblast","Galvaran","Iguolta","Ptyranidur","Rexillius","Amagara","Dragmara","Nymphali","Brutalibré","Dedenne","Strassie","Mucuscule","Colimucus","Muplodocus","Trousselin","Brocélôme","Desséliande","Pitrouille","Banshitrouye","Grelaçon","Séracrawl","Sonistrelle","Bruyverne","Xerneas","Yveltal","Zygarde","Diancie","Hoopa","Volcanion","Brindibou","Efflèche","Archéduc","Flamiaou","Matoufeu","Félinferno","Otaquin","Otarlette","Oratoria","Picassaut","Piclairon","Bazoucan","Manglouton","Argouste","Larvibule","Chrysapile","Lucanon","Crabagarre","Crabominable","Plumeline","Bombydou","Rubombelle","Rocabot","Lougaroc","Froussardine","Vorastérie","Prédastérie","Tiboudet","Bourrinos","Araqua","Tarenbulle","Mimantis","Floramantis","Spododo","Lampignon","Tritox","Malamandre","Nounourson","Chelours","Croquine","Candine","Sucreine","Guérilande","Gouroutan","Quartermac","Sovkipou","Sarmuraï","Bacabouh","Trépassable","Concombaffe","Type:0","Silvallié","Météno","Dodoala","Boumata","Togedemaru","Mimiqui","Denticrisse","Draïeul","Sinistrail","Bébécaille","Écaïd","Ékaïser","Tokorico","Tokopiyon","Tokotoro","Tokopisco","Cosmog","Cosmovum","Solgaleo","Lunala","Zéroïd","Mouscoto","Cancrelove","Câblifère","Bamboiselle","Katagami","Engloutyran","Necrozma","Magearna","Marshadow","Vémini","Mandrillon","Ama-Ama","Pierroteknik","Zeraora","Meltan","Melmetal","Ouistempo","Badabouin","Gorythmic","Flambino","Lapyro","Pyrobut","Larméléon","Arrozard","Lézargus","Rongourmand","Rongrigou","Minisange","Bleuseille","Corvaillus","Larvadar","Coléodôme","Astronelle","Goupilou","Roublenard","Tournicoton","Blancoton","Moumouton","Moumouflon","Khélocrok","Torgamord","Voltoutou","Fulgudog","Charbi","Wagomine","Monthracite","Verpom","Pomdrapi","Dratatin","Dunaja","Dunaconda","Nigosier","Embrochet","Hastacuda","Toxizap","Salarsen","Grillepattes","Scolocendre","Poulpaf","Krakos","Théffroi","Polthégeist","Bibichut","Chapotus","Sorcilence","Grimalin","Fourbelin","Angoliath","Ixon","Berserkatt","Corayôme","Palarticho","M. Glaquette","Tutétékri","Crèmy","Charmilly","Hexadron","Wattapik","Frissonille","Beldeneige","Dolman","Bekaglaçon","Wimessir","Morpeko","Charibari","Pachyradjah","Galvagon","Galvagla","Hydragon","Hydragla","Duralugon","Fantyrm","Dispareptil","Lanssorien","Zacian","Zamazenta","Éthernatos","Wushours","Shifours","Zarude","???","???","???","???","???","Cerbyllin","Hachécateur","Ursaking","Paragruel","Farfurex","Qwilpik","Amovénus","Poussacha","Matourgeon","Miascarade","Chochodile","Crocogril","Flâmigator","Coiffeton","Canarbello","Palmaval","Gourmelet","Fragroin","Tissenboule","Filentrappe","Lilliterelle","Gambex","Pohm","Pohmotte","Pohmarmotte","Compagnol","Famignol","Pâtachiot","Briochien","Olivini","Olivado","Arboliva","Tapatoès","Selutin","Amassel","Gigansel","Charbambin","Carmadura","Malvalame","Têtampoule","Ampibidou","Zapétrel","Fulgulairo","Grondogue","Dogrino","Gribouraigne","Tag-Tag","Virovent","Virevorreur","Terracool","Terracruel","Craparoi","Pimito","Scovilain","Léboulérou","Bérasca","Flotillon","Cléopsytra","Forgerette","Forgella","Forgelina","Taupikeau","Triopikeau","Lestombaile","Dofin","Superdofin","Vrombi","Vrombotor","Motorizard","Ferdeter","Germéclat","Floréclat","Toutombe","Tomberro","Flamenroule","Piétacé","Balbalèze","Délestin","Oyacata","Nigirigon","Courrousinge","Terraiste","Farigiraf","Deusolourdo","Scalpereur","Fort-Ivoire","Hurle-Queue","Fongus-Furie","Flotte-Mèche","Rampe-Ailes","Pelage-Sablé","Roue-de-Fer","Hotte-de-Fer","Paume-de-Fer","Têtes-de-Fer","Mite-de-Fer","Épine-de-Fer","Frigodo","Cryodo","Glaivodo","Mordudor","Gromago","Chongjian","Baojian","Dinglu","Yuyu","Rugit-Lune","Garde-de-Fer","Koraidon","Miraidon"]

class Individu:
	def __init__(self,sexe,ancetres = [], age = 0):
		self.prenom = rd.choice(prenom)
		self.sexe = sexe
		self.age = age
		self.ancetres = ancetres
		self.partenaires = []
		self.partenaires_possibles = []
		self.repos = 0


	def update(self,population):
		if self.age >= 18:
			self.partenaires_possibles = [x for x in population 
			if x not in self.ancetres and
			self.partage_ancetres(x) and
			self.sexe != x.sexe and
			x.age > 18 and
			not x == self and
			x not in self.partenaires
			]

	def partage_ancetres(self,partenaire):
		for x in self.ancetres:
			if x in partenaire.ancetres:
				return False
		return True

	def majeur(self):
		return self.age >= 18
	
	def apercu(self):
		return "Prénom : " + self.prenom + ", Age : " + str(self.age) + ", Sexe : " + self.sexe + ", Ancetres : " + str(self.ancetres) + ", Partenaires potentiels : " + str([x.prenom for x in self.partenaires_possibles])


class Population:
	def __init__(self,nbr_couples_initial):
		self.population = [Individu("Male",[],25) for k in range(nbr_couples_initial)] + [Individu("Femelle",[],25) for k in range(nbr_couples_initial)]
		self.morts = []
		self.update()

	def update(self):
		self.population = [x for x in self.population if not x in self.morts]
		for x in self.population:
			x.update(self.population)

	def temps(self,annees):
		for k in range(annees):
			for x in self.population:
				x.age += 1
				if x.repos > 0:
					x.repos += -1
				if x.age > 50:
					self.morts.append(x)
			self.update()

	def apercu(self):
		out = ""
		for x in self.population:
			out += x.apercu() + "\n"
		return out

	def generation(self, repos):
		for x in self.population:
			if x.sexe == "Femelle" and x.repos == 0 and x.partenaires_possibles != []:
				self.population += [Individu(rd.choice(["Male","Femelle"]),x.ancetres + x.partenaires_possibles[0].ancetres + [x.prenom,x.partenaires_possibles[0].prenom])]
				x.repos = repos
				x.partenaires.append(x.partenaires_possibles[0])
				x.partenaires_possibles[0].partenaires.append(x)
			self.update()

	def testPartenaires(self):
		for x in self.population:
			if x.partenaires_possibles != [] or not x.majeur():
				return True
		return False



def test(années,nbr_couples_initial,repos,sauts_années = 1):
	t0 = timer()
	pop = Population(nbr_couples_initial)
	txt.write(("Années 0\n").encode("utf8"))
	txt.write((pop.apercu()).encode("utf8"))
	if années == -1:
		compteur = 1
		while pop.testPartenaires() or compteur > 150:
			pop.temps(1)
			t1 = timer()
			pop.generation(repos)
			print(str("%.3f" % (timer() - t1)) + " secondes.")
			if compteur % sauts_années == 0:
				txt.write(("\n\nAnnée " + str(compteur) + ", " + str("%.3f" % (timer() - t1)) + " secondes." + "\n\n").encode("utf8"))
				txt.write((pop.apercu()).encode("utf8"))
			compteur += 1
		txt.write(("\n\nAnnée " + str(compteur) + "\n\n").encode("utf8"))
		txt.write((pop.apercu()).encode("utf8"))
		txt.write(("\n\nIl n'y a pas de consanguinité avant " + str(compteur) + " années avec une population vivante de " + str(len(pop.population)) + " individus et une population totale de " + str(len(pop.population) + len(pop.morts)) + " individus.").encode("utf8"))
	else:
		for k in range(1,années + 1):
			pop.temps(1)
			pop.generation(repos)
			if k % sauts_années == 0:
				txt.write(("Année " + str(k) + ", " + str("%.3f" % (timer() - t0)) + "\n").encode("utf8"))
				txt.write((pop.apercu()).encode("utf8"))
	print("Temps global : " + str("%.3f" % (timer() - t0)) + " secondes.")



test(-1,3,2,10)

txt.close()

"""
pop = Population(3)
pop.generation(2)
print(pop.apercu())
pop.temps(30)
print(pop.apercu())
pop.temps(20)
print(pop.apercu())
print(pop.testPartenaires())
print(pop.morts)
"""