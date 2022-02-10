import dash_bootstrap_components as dbc
from dash import html


# Page de présentation
def presentation():
    return html.Div([
        html.H4("Présentation"),
        html.P("Les cellules sanguines sont divisées en 3 catégories : "),
        html.Ul([html.Li(["Les Globules Rouges appelés aussi hématies ou érythrocytes",
                          html.Ul([html.Li("ce sont les cellules les plus nombreuses du sang (5 millions/mm3)"),
                                   html.Li("Le rôle principal de ces cellules est d'assurer le transport de l'oxygène et du gaz carbonique entre les alvéoles pulmonaires et les tissus.")
                                    ]),
                          ]),
                html.Li(["Globules blancs  : Leucocytes",
                         html.Ul([html.Li("ils sont au nombre d'environ 8 000/mm3."),
                                  html.Li("ces cellules participent aux défenses spécifiques de l'organisme, aident à combattre les bactéries et les virus"),
                                  ]),
                         ]),
                html.Li(["Plaquettes ou thrombocytes",
                         html.Ul([html.Li("elles sont au nombre de 150 000 à 450 000/mm3"),
                                  html.Li("les plaquettes sont des fragments cytoplasmiques d'un mégacaryocyte"),
                                  html.Li("elles jouent un rôle fondamental dans les phénomènes initiaux de coagulation")
                                  ])

                        ])
                 ]),
        html.Div(dbc.Card([
                    dbc.CardBody([html.Img(src="./assets/frottis.jfif",style={"width": "23rem"})]),
                    dbc.CardFooter("Frottis sanguin"),
                    ],style={"width": "25rem","margin":"auto","margin-bottom":"20px"}),
                style= {"text-align":"center"}),
        html.P("La numération globulaire (% de globules rouges, blancs et plaquettes) dans le sang permet de révéler des problèmes de santé : anémie, infection, hémorragie..."),
        html.P("Certaines cellules vont également se retrouver dans le sang, alors qu'elles devraient être présentes uniquement dans la moêlle osseuse (là où sont fabriquées les cellules)."),
        html.Img(src="./assets/hematopoiese.png", width="100%", style={"margin-top":"2rem"}),
        html.P("La présence de ces types de cellules (promyelocyte, myelocyte... ) dans le sang en quantité importante peut être le signe de problèmes de santé, tel que des leucémies."),
        html.P("Il est donc utile de pouvoir identifier différents types de cellules afin d'en connaitre la présence dans un frottis sanguin, un préalable à l'identification de certaines maladies."),
        html.H5("Problèmatique"),
        html.P("Actuellement, des automates permettent d'identifier une quinzaine de cellules sanguines en utilisant des algorithmes de traitement d'images : définition de caractéristiques telles que diamètre/périmètre de la cellule et du noyau, couleur, textures (granularités) ..."),
        html.P("Les processus actuels permettent également d'isoler les leucocytes et platelets de l'échantillon pour obtenir une image par cellule."),
        html.P("L'idée était donc d'utiliser l'intelligence artificielle, notament le Deep Learning, pour essayer d'améliorer la reconnaissance des différentes types de cellules sanguines.")

    ])

# Onglet 1 de la page Data
tab1_data = dbc.Card(dbc.CardBody([
                html.P(["Le dataset est disponible sur le site de partage de ressource Mendeley: « A dataset for microscopic peripheral blood cell images for development of automatic recognition systems » ",
                    html.A("https://data.mendeley.com/datasets/snkd93bnjr/1",href="https://data.mendeley.com/datasets/snkd93bnjr/1")]),
                html.P("Elle contient 17092 images de cellules sanguines de 8 types différents : "),
                html.Ul([html.Li("Leucocytes (globules blancs) : basophil, eosinophil, erythroblast, ig, lymphocyte, monocyte, neutrophil. Les IG (immatures granulocytes) regroupent : métamyelocytes, myelocytes et promyelocytes"),
                        html.Li("Plaquettes (platelet) ")]),
                html.Div([html.Img(src="./assets/8types.jpg")],style={"width":"100%","text-align":"center"}),
                html.P("Les plaquettes (platelets) sont facilement identifiables car plus petits. Les eosinophils semblent avoir un noyau d’une autre couleur. Les autres types sont plus difficilement différentiables."),
                html.Div([html.Img(src="./assets/repartition_mendeley.jpg")],className="div_img"),
                html.P("Au moins 1200 images pour chaque type : jeu de données assez équilibré."),
                html.P("Uniformité du format des images: "),
                html.Div([html.Img(src="./assets/repartition_format.png")],className="div_img"),
                html.P("Luminosité différente pour quelques images: images au format 369x366 et 360x360 "),
                html.Div([html.Img(src="./assets/luminosite.png")],className="div_img"),
                html.P("Images avec luminosité plus faible, réparties dans les 7 types de cellules"),
                html.Div([html.Img(src="./assets/repartition_luminosite.png")],className="div_img"),
                html.P("Doublons : 17 doublons ont été identifiés, dont une image classée dans 2 catégories différentes. Ceci révèle la difficulté, même pour le biologiste de classifier les différents types de cellules.  "),
                html.P("Cellules centrées: sur toutes les images, les leucocytes ou platelets sont bien centrées. Les images peuvent être rognées au format 256*256 à partir du centre, sans perte d’information sur la cellule"),
                html.P("L’intégralité des images a été conservée."),

            ]),style={"margin":"auto","margin-bottom":"20px"}
            )

# Onglet 2 de la page Data
tab2_data = dbc.Card(dbc.CardBody([
                html.P(["Le dataset est disponible sur le site de partage de ressource Kaggle: « Acute Promyelocytic Leukemia » ",
                    html.A("https://www.kaggle.com/eugeneshenderov/acute-promyelocytic-leukemia-apl", href="https://www.kaggle.com/eugeneshenderov/acute-promyelocytic-leukemia-apl")]),
                html.P("Les images proviennent de 106 patients atteints de leucémie aigue promyélocytaire (APL) ou leucémie aigue myéloïde (AML)."),
                html.Div([html.Img(src="./assets/apl_aml_gender.png"),html.Img(src="./assets/apl_aml_age.png")],className="div_img"),
                html.P("Le dataset contient 15517 images de cellules labellisées en 20 catégories différentes"),
                html.Div([html.Img(src="./assets/repartition_kaggle_all.jpg")],className="div_img"),
                html.P("En moyenne, 110 images par patient sont identifiées"),
                html.Div([html.Img(src="./assets/nb_par_patient.png")], className="div_img"),
                html.P("Doublons : 28 doublons ont été identifiés. Pour chacun, ils ont été classées dans des catégories différentes, révélant là encore les confusions possibles."),
                html.P("Nettoyage : les doublons, ainsi que certaines images buggés ont été supprimées, des catégories ont été regroupées et d'autres non conservées. La base contient, après nettoyage, 14643 images réparties en 10 catégories."),
                html.Div([html.Img(src="./assets/repartition_kaggle.jpg")], className="div_img"),
                html.P("Certaines catégories comprenant peu de cellules, cette base n’a pas été utilisée seule pour entrainer un modèle mais en complément de la base Mendeley.")


            ]))

# Page data
def data():
    return html.Div([
            dbc.Tabs([
                dbc.Tab(tab1_data, label="Base Mendeley"),
                dbc.Tab(tab2_data, label="Base Kaggle"),
            ])
        ])


# Page présentation premiers modèles
def first_model():
    return html.Div([html.H4("Premiers modèles"),
                     html.P("Utilisation de la base Mendeley uniquement: classification de 8 types de cellules, cellules recadrées en 256x256 à partir du centre"),
                     html.H5("Machine Learning"),
                     html.P("Utilisation de 4000 images en Noir et Blanc, prises aléatoirement  et réparties uniformément sur les 8 catégories : 3200 pour l'entrainement, 800 pour validation "),
                     html.P("Modèle Machine à vecteurs de support (SVC) : taux de prédiction correcte (accuracy) de 80% "),
                     html.P("Modèle Random Forest : meilleur score à 84%"),
                     html.Div([html.Img(src="./assets/random_forest.jpg")], className="div_img"),
                     html.P("Deux types de cellules donnent des scores nettement plus faibles : 67% pour les IG et 77% pour les monocytes."),
                     html.H5("Deep Learning"),
                     html.P("Sur cette même base de 4000 images, un modèle convolutif type LeNet donne une accuracy à 74% avec des images en Noir et Blanc et 87% avec des images en couleurs. Le modèle est cependant en overfitting avec une accuracy de 99% sur les données d’entrainement."),
                     html.Div([html.Img(src="./assets/lenet_4000images.jpg")], className="div_img"),
                     html.P("Les cellules de type IG ont là encore du mal à être correctement identifiées : précision à 66% et rappel à 69%."),
                     html.H5("Réduction de dimension"),
                     html.P("Afin d’essayer d’identifier des caractéristiques sur les images, j’ai utilisé un modèle de Manifold Learning pour visualiser les données."),
                     html.Div([html.Img(src="./assets/reduction_dim.jpg")], className="div_img"),
                     html.P("Trois types de cellules sont facilement identifier sur le graphique (groupés) : erythroblast, platelet et lymphocyte. Ces types de cellules obtiennent effectivement des scores supérieurs à 92% et même 99% pour les platelets."),
                     ])


# Modèles deep Learning
def deep_model():
    return html.Div([html.H4("Modèles Deep Learning"),
                     html.P("Reprise du modèle type LeNet sur la totalité des images: 11000 images pour l’entrainement, 2700 pour les tests et 3400 pour la validation."),
                     html.Div([html.Img(src="./assets/lenet_tot_images.jpg")], className="div_img"),
                     html.P("En augmentant ainsi les données d’entrainement, l’accuracy s’améliore pour passer de 87 à 93%. Le type de cellule IG obtient toujours un score plus faible de 85%."),
                     html.H5("Transfer Learning"),
                     html.P("Le principe du Transfer Learning est d’exploiter des modèles complexes et performant de Deep Learning, nécessitant des temps de calcul élevés et des ressources importantes. Ces modèles pré-entrainés sur de grandes quantités de données vont être utilisés comme point de départ de nouveaux modèles pour un apprentissage plus rapide."),
                     html.H6("Fine-tuning", style={"text-decoration":"underline"}),
                     html.P("Certaines couches du modèle de base vont être « dégelées », c’est-à-dire réentraînées avec la nouvelle base (poids recalculés pendant l’entrainement du modèle)."),
                     html.P("Utilisation du modèle VGG16 en Transfer Learning (base imagenet) :  sur la même base d'image, le résultat s'améliore passant à 96%."),
                     html.P("En testant différents paramètres (nombre de couches 'dégelées', algorithme d'optimisation de descente de gradient, différentes couches de neurones), une accuracy de 98% est ainsi obtenue."),
                     html.Div([html.Img(src="./assets/vgg16_best.jpg")], className="div_img"),
                     html.P("Meilleur score avec les paramètres suivants : 8 dernières couches de VGG16 dégelées, utilisation de Adam puis SGD, couches  de 1024, 512 et 256 neurones."),
                     html.H6("Features extraction", style={"text-decoration": "underline"}),
                     html.P("La dernière couche de neurones du modèle de réseau convolutif va être utilisé comme entrée d’un nouveau modèle de Machine Learning. "),
                     html.P("En réutilisant le modèle précédent en Features extraction avec un modèle SVC, le résultat monte à 98.5% de prédictions correctes")
                    ])

# Page d'analyse
def analysis():
    return html.Div([html.H4("Analyse"),
                html.P("Scores obtenus élevés : indice d'un biais dans les données?"),
                html.P("Prédiction sur 2727 images provenant de la base Kaggle : seulement 45% de bonnes prédictions"),
                html.H5("Grad-CAM"),
                html.P("La carte d’activation de classe pondérée par le gradient (Grad-CAM) produit une carte thermique qui met en évidence les régions importantes d’une image en utilisant les gradients de la cible de la couche convolutive finale. "),
                dbc.Table([html.Tbody([
                                html.Tr([html.Th("Basophil"), html.Td(html.Img(src="./assets/gc_basophil_8.jpg"))]),
                                html.Tr([html.Th("Eosinophil"), html.Td(html.Img(src="./assets/gc_eosinophil_8.jpg"))]),
                                html.Tr([html.Th("Erythroblast"), html.Td(html.Img(src="./assets/gc_erythroblast_8.jpg"))]),
                                html.Tr([html.Th("IG"), html.Td(html.Img(src="./assets/gc_ig_8.jpg"))]),
                                html.Tr([html.Th("Lymphocyte"), html.Td(html.Img(src="./assets/gc_lymphocyte_8.jpg"))]),
                                html.Tr([html.Th("Monocyte"), html.Td(html.Img(src="./assets/gc_monocyte_8.jpg"))]),
                                html.Tr([html.Th("Neutrophil"), html.Td(html.Img(src="./assets/gc_neutrophil_8.jpg"))]),
                                html.Tr([html.Th("Platelet"), html.Td(html.Img(src="./assets/gc_platelet_8.jpg"))]),
                        ])
                    ],size="sm"),
                html.P("L’utilisation du Grad-CAM n’a pas permis d'identifier de biais."),
                html.H5("Score faible des IG"),
                html.P("IG : cellules immatures d’autres types (basophil, neutrophil, eosinophil. Problème de caractéristiques commmunes à ces classes?"),
                html.P("Entrainement du modèle sur seulement 7 classes, étude de la classification des cellules IG dans ces 7 classes"),
                html.Div([html.Img(src="./assets/ig_class.jpg")], className="div_img"),
                html.P("Les Ig prédits principalement dans la classe monocyte et non dans les classes basophil, neutrophil et eosinophil comme attendu."),
                html.P("Caractéristiques communes IG/ Monocyte?"),
                html.H5("Ajout de données avec la base Kaggle"),
                html.P("25530 images sur les 8 types de cellules"),
                html.Div([html.Img(src="./assets/repartition_8_2bases.jpg")], className="div_img"),
                html.P("Modèle type LeNet sur images originales redimensionnées en 256x256 : accuracy à 88% (93% avec la seule base Mendeley"),
                html.Div([html.Img(src="./assets/lenet_2bases.jpg")], className="div_img"),
                html.P("Score plus faible avec les 2 bases, montrant une disparité dans les images provenant des 2 bases.")
            ])

# Page Segmentation
def segmentation():
    return html.Div([html.H4("Segmentation"),
                     html.P("Idée : détourer la cellule pour supprimer les informations non utiles autour (globules rouges)"),
                     html.P("Difficulté pour des images contenant des globules rouges agglutinés autour de la cellule."),
                     html.P("Detection de contour pour 1400 images sans globules rouges agglutinés : algorithme avec OpenCV"),
                     html.P("Définition de modèle Deep Learning de segmentation (Unet et FCN) avec entrainement sur ces 1400 images."),
                     html.P("Bon résulat obtenu pour détecter les contours des cellules avec FCN"),
                     html.Div([html.Img(src="./assets/segmentation_model.jpg")], className="div_img"),
                     html.P("Sur de nouvelles images avec des globules rouges agglomérés, bon détourage de la cellule"),
                     html.Div([html.Img(src="./assets/detourage_agglo.jpg")], className="div_img"),
                     html.H5("Modèle LeNet sur images détourées"),
                     html.P("Nouvelle base d'images, avec fond noir autour de la cellule, recadrées en 256x256 à partir du centre."),
                     html.P("Résultat du modèle LeNet entrainé sur cette nouvelle base : pas de réelle amélioration."),
                     html.Div([html.Img(src="./assets/res_lenet_detourage.jpg")], className="div_img"),
                     ])