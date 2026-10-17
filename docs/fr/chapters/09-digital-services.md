# Chapitre 9 : Services numériques

**Définition d'un service numérique tirée** **de l'AFNOR Spec :**

*Un service numérique est constitué d'un ensemble de produits logiciels, de terminaux, d'infrastructures (réseaux et centres de données). Il peut lui-même être composé d'autres services numériques. Il permet d'effectuer une ou plusieurs actions sous forme numérique. Par exemple, « réserver une place dans un train », « prendre un rendez-vous chez un médecin », « envoyer un e-mail à des amis », « regarder une vidéo en ligne », « échanger des points de vue sur les réseaux sociaux », « effectuer un transfert d'argent », « planifier des jours de congé », « participer à une vidéoconférence », « remplir une note de frais », « modéliser une pièce mécanique », etc.*

## Questions ouvertes

- Comment prenez-vous en compte l'empreinte environnementale et sociétale des services numériques que vous développez ou utilisez, dans votre organisation ?
- Avez-vous pris des initiatives spécifiques pour lutter contre le développement de l'obésiciel (bloat software) et l'obsolescence ? Sur quelles référentiels d'écoconception et d'accessibilité s'appuie votre initiative ?
- Comment maîtriser les compétences multidisciplinaires et les interdépendances pour créer des synergies entre la cybersécurité, le numérique responsable, l'architecture, la qualité et la stratégie ? Par exemple, en considérant l'Open Source.
- Comment prendre en compte les spécificités induites par la gestion des données et l'intelligence artificielle ?

## 9.1 Comment prenez-vous en compte l'empreinte environnementale et sociétale des services numériques que vous développez ou utilisez, dans votre organisation ? {#q9-1}

### Raison d'être

L'empreinte environnementale des technologies de l'information est clairement due aux équipements, mais le matériel n'a qu'une seule fonction : faire fonctionner les logiciels. Ainsi, en travaillant sur les services numériques, nous pouvons également réduire les besoins en ressources matérielles, lutter contre leur obsolescence et augmenter leur durée de vie.

### Critères d'évaluation

| Critère d'évaluation | Priorité recommandée | Pondération proposée (total = 25 points) |
|---|---|---|
| Le soumissionnaire a lancé une initiative visant à prendre en compte l'empreinte environnementale et sociétale des services numériques dans son processus d'achat ou de développement. | P1 | 5 |
| L'évaluation de l'empreinte est effectuée selon les méthodes d'évaluation du cycle de vie. L'ACV doit être multicritère et faire l'objet d'un examen critique. | P1 | 5 |
| Le lien entre le logiciel et le matériel a été établi, en tenant compte de l'empreinte environnementale du service numérique due au matériel (fabrication et consommation d'énergie), mais aussi du fait que le matériel est utilisé pour faire fonctionner le logiciel, et qu'il est donc obligatoire de travailler sur la sobriété du logiciel pour réduire les besoins en matériel. | P2 | 3 |
| L'évaluation de l'empreinte doit être conforme au PCR des services numériques et à ses dérivés spécifiques. | P2 | 3 |
| Le reporting est réalisé conformément à la CSRD, au niveau du service numérique. | P2 | 3 |
| Les architectes d'entreprise et les architectes informatiques participent à l'initiative numérique responsable. | P2 | 3 |
| Une équipe ou des compétences UX/UI existent dans l'organisation. Elles sont toujours impliquées au début de tout nouveau projet ou développement de service numérique, dès que le client le demande. | P2 | 3 |

## 9.2 Avez-vous pris des initiatives spécifiques pour lutter contre le développement de l'obésiciel (bloat software) et l'obsolescence ? Sur quelles référentiels d'écoconception et d'accessibilité s'appuie votre initiative ? {#q9-2}

### Raison d'être

En s'appuyant sur la loi de Moore, les logiciels peuvent exiger de plus en plus de ressources et de capacités de calcul. Niklaus Wirth a montré que les logiciels demandent de plus en plus de ressources, à une vitesse supérieure à celle que peuvent fournir les évolutions matérielles (loi de Wirth). Cette divergence n'est pas soutenable et la seule façon d'y remédier est d'écoconcevoir les services numériques.

### Critères d'évaluation

| Critère d'évaluation | Priorité recommandée | Pondération proposée (total = 25 points) |
|---|---|---|
| Le soumissionnaire connaît les différents référentiels d'écoconception (au moins deux, par exemple : RGESN, GR491, SDIA, AFNOR Spec) et d'accessibilité (WCAG/RGAA) existants pour les services numériques. | P1 | 4 |
| Le soumissionnaire a lancé une initiative visant à adapter ces référentiels à sa propre organisation informatique, en créant un référentiel spécifique que ses fournisseurs appliquent et qu'il exige dans les appels d'offres. | P1 | 4 |
| L'arrêt et le retrait (decommissioning) est prévu dans le cycle de vie de tout service numérique, y compris une date fixe pour remettre en question la nécessité du service. | P1 | 4 |
| La valeur d'un service numérique pour l'entreprise est examinée et questionnée en termes de retour sur investissement et impacts (ROII). | P2 | 2 |
| Évaluer l'indice de maturité de tout nouveau service numérique, sur la base des exigences demandées dans ce référentiel et des bonnes pratiques des référentiels d'écoconception. | P2 | 3 |
| Des mesures sont prises pour lutter contre l'obsolescence des logiciels et l'obsolescence liée aux effets de mode. | P2 | 3 |
| Des mesures sont prises pour limiter l'augmentation de la demande de ressources informatiques matérielles et pour lutter contre la loi de Wirth. | P2 | 2 |
| La politique des « 3U » est respectée : chaque service numérique doit prouver qu'il est utile, sa capacité à être utilisé par toutes les personnes qui en ont besoin est démontrée et, enfin, son utilisation réelle est fréquemment vérifiée. | P2 | 2 |
| Les ressources informatiques sont sollicitées uniquement pendant l'utilisation du service numérique et l'élasticité des machines virtuelles est favorisée. | P3 | 1 |

## 9.3 Comment maîtriser les compétences multidisciplinaires et les interdépendances pour créer des synergies entre la cybersécurité, le numérique responsable, l'architecture, la qualité et la stratégie ? Par exemple, en considérant l'Open Source. {#q9-3}

### Raison d'être

Lors de la création d'un référentiel d'écoconception, on constate que certaines bonnes pratiques ne sont pas spécifiques au numérique responsable mais sont des fondamentaux des métiers de l'UX/UI, par exemple, ou sont des fondamentaux d'une démarche qualité, elles peuvent aussi être une opportunité pour la cybersécurité en favorisant une réduction de la surface d'attaque, par exemple. Ces synergies doivent être identifiées et utilisées de manière opérationnelle. Les 3 piliers (3P) de la soutenabilité, People, Planet, Prosperity, peuvent devenir 4P avec la Protection.

### Critères d'évaluation

| Critère d'évaluation | Priorité recommandée | Pondération proposée (total = 25 points) |
|---|---|---|
| Tous les services du département numérique de l'organisation contribuent à l'initiative de numérique responsable et à la réduction de l'empreinte des services numériques ; les compétences matérielles et logicielles sont représentées, y compris les équipes de cybersécurité et celles chargées de définir les niveaux de service (SLA). | P1 | 10 |
| Les synergies entre la cybersécurité, la maintenabilité, le coût total de possession et la soutenabilité sont prises en compte dans les décisions techniques. La sécurité et la soutenabilité doivent tous les deux être prises en compte dès la conception et peuvent être fusionnées. Par exemple : disposer d'une CMDB à jour. | P2 | 8 |
| Les possibilités de recours à l'Open Source sont envisagées afin de réduire la dépendance à l'égard de certains fournisseurs et d'accroître l'interopérabilité, la souveraineté et la résilience du département informatique. | P2 | 7 |

## 9.4 Comment prendre en compte les spécificités induites par la gestion des données et l'intelligence artificielle ? {#q9-4}

### Raison d'être

L'intelligence artificielle (IA) reflète souvent l'intelligence humaine, y compris ses différents types de biais. Elle nécessite également beaucoup de données, de serveurs et d'énergie pour ses phases d'apprentissage, et une IA générative populaire peut être utilisée par des millions de personnes, entraînant des effets rebond massifs qui sont déjà visibles dans les rapports de soutenabilité des entreprises des principaux acteurs, menaçant leur engagement en faveur du climat. Des actions spécifiques doivent être lancées pour éviter de compromettre la durabilité de l'ensemble de l'industrie des technologies de l'information.

### Critères d'évaluation

| Critère d'évaluation | Priorité recommandée | Pondération proposée (total = 25 points) |
|---|---|---|
| L'utilisation de l'IA est transparente et remise en question pour tout service numérique, en examinant si des solutions alternatives ayant moins d'impact peuvent la remplacer. | P1 | 6 |
| Les guides et références spécifiques à l'IA sont connus et effectivement utilisés (ex : Guide de l'IA - RIA31 - de l'Institut du Numérique Responsable, AFNOR Spec pour l'IA frugale). | P1 | 6 |
| Une politique de gestion des données est déployée dans l'organisation, respectant la réglementation (RGPD), y compris pour l'utilisation de l'IA, favorisant la qualité des données et limitant leur prolifération, car une augmentation massive de données de mauvaise qualité est un véritable frein au développement durable de l'IA. | P2 | 5 |
| La gouvernance des données prend en compte le type de données et encourage à respecter le besoin réel : par exemple, les formats vidéo sont remis en question au profit des données audio ou écrites, les courriels conservés en boîte de réception ont une durée de conservation limitée. | P2 | 4 |
| La quantité globale et exhaustive de données stockées et la quantité de données utilisées devraient être contrôlées et communiquées au moins une fois par an, tant pour le stockage interne que pour le stockage externe des données. | P2 | 4 |
