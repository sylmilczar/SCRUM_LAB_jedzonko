from django.db import migrations
from jedzonko.models import Recipe


def populate(apps, schema_editor):
    Recipe.objects.create(name="Składana tortilla", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Placki tortilli składane na 4 to hit TikToka 2021 roku. Cały patent polega na nacięciu placka do połowy, rozłożeniu składników na każdej ćwiartce i złożeniu ich po kolei jedną na drugą.")
    Recipe.objects.create(name="Ciasto na słodkie naleśniki", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Naleśniki na słodko są idealnym pomysłem na deser. Teoretycznie zazwyczaj tę samą recepturę ciast..."
                          )
    Recipe.objects.create(name="Dip z awokado i jajek", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Kremowy, łagodny dip lub pasta do chleba z awokado i jajek. Szybki, łatwy do przygotowania i bardzo smaczny. Pasuje do wędlin, mięs np. z grilla, jajek na twardo, serów, warzyw, na przyjęcie do chipsów tortilla i po prostu na chleb."
                          )
    Recipe.objects.create(name="Buraczki na ciepło do obiadu", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Podsmażane buraki na ciepło to pyszny i wartościowy dodatek do obiadu. Bardzo proste do przygotowania. W szybkiej wersji można sięgnąć po gotowane buraki ze sklepu, pakowane hermetycznie. Jednak najbardziej aromatyczne są upieczone w piekarniku. Polecam podawać z mięsem i ziemniakami."
                          )
    Recipe.objects.create(name="Zupa- krem z dyni", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Przepis na pyszną zupę krem z dyni. Uwielbiam tę zupę. Pora jesienna to okazja do jej przygotowania. Jest bardzo delikatna, kremowa, łagodna, a cytryna i imbir nadają jej ciekawego smaku."
                          )
    Recipe.objects.create(name="Koktajl jagodowo- bananowy na mleku kokosowym", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Szybki koktajl z jagód, bez cukru i nabiału, osłodzony dodatkiem bananów. Prosty i ekspresowy do przygotowania. Jako przekąska lub na śniadanie."
                          )
    Recipe.objects.create(name="Krokiety z pieczarkami, jajkiem i żółtym serem", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Krokiety z farszem z usmażonych pieczarek, jajek na twardo, natki pietruszki i startego, żółtego sera. Bardzo smaczny obiad, prosty do przygotowania, ale nieco pracochłonny. Krokiety można podawać z filiżanką czerwonego barszczu."
                          )
    Recipe.objects.create(name="Kopytka", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Podstawowy przepis na kopytka. Można je jeść jako samodzielne danie np. polane podsmażoną cebulką, skwarkami, stopionym masłem lub ulubionym sosem, albo jako dodatek do pieczeni, czy gulaszu."
                          )
    Recipe.objects.create(name="Spaghetti carbonara ze śmietaną", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Spaghetti Carbonara to błyskawiczne do przygotowania, a jednocześnie bardzo smaczne danie kuchni włoskiej. To makaron z kremowym sosie jajecznym z dodatkiem boczku. W tym przepisie przedstawiam Wam wersję z dodatkiem śmietany. Wiem, że to kwestia sporna, ale spróbujcie również takiej wersji i przekonajcie się, że jest bardzo smaczna. Danie smakuje całej rodzinie, również dzieciom. Jeśli ktoś szuka pomysłu na smaczne danie a'la carbonara to go tutaj znajdzie ;)"
                          )
    Recipe.objects.create(name="Bigos", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Przepis na najlepszy bigos staropolski. Przygotowuje się go z kiszonej i białej kapusty. Zawiera mięso, kiełbasę, boczek, grzyby, śliwki i czerwone wino. Powinien być długo gotowany, a następnie odgrzewany. Wtedy jest najsmaczniejszy i aromatyczny. Palce lizać."
                          )
    Recipe.objects.create(name="Wigilijna kapusta z fasolą", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Proste, sycące danie nie tylko na Wigilię. Poza Wigilią można zaserwować taką kapustę np. z usmażonymi udkami kurczaka. Kapusta kiszona w tej potrawie nie powinno być kwaśna. Dlatego, jeśli po spróbowaniu okaże się kwaśna, należy ją wypłukać. Danie powinno mieć maślany smak, dlatego nie szczędźmy tutaj prawdziwego masła. 3 łyżki masła to minimum ;)"
                          )
    Recipe.objects.create(name="Zupa ogórkowa", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Najlepsza zupa ogórkowa z ziemniakami. Tradycyjna, polska zupa. Każdy z nas ją zna i pewnie przygotowuje w podobny sposób. Jeśli jednak ktoś chciałby przygotować ją według tego przepisu to polecam, bo zupa wychodzi naprawdę pyszna. Jest trochę pracochłonna, ale łatwa do przygotowania. Można ugotować ją na wywarze z dowolnego mięsa, ale ja polecam szczególnie żeberka wieprzowe."
                          )
    Recipe.objects.create(name="Kurczak po chińsku z orzeszkami ziemnymi", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Soczyste kawałki mięsa z piersi kurczaka usmażone z cebulą i chrupiącymi orzeszkami ziemnymi, doprawione sosem sojowym i ostrymi przyprawami jak chili lub chiński pieprz. Kurczak powinien być dobrze przyprawiony, aby był wyraźny w smaku i ostry. Tak przygotowane mięso można podawać z ryżem lub makaronem."
                          )
    Recipe.objects.create(name="Ryba zapiekana z pieczarkami i jabłkiem", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Panierowana ryba, zapiekana z pieczarkami, plasterkami jabłka i serem żółtym. Pożywny, bogaty obiad. Polecam podawać z ryżem wymieszanym z ziołami świeżymi lub mrożonymi."
                          )
    Recipe.objects.create(name="Zupa pomidorowa z pomidorów z puszki", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Zupa pomidorowa przygotowana na rosole, z pomidorami z puszki i koncentratem pomidorowym. Zupa jest łagodna, kremowa i bardzo smaczna. Lubiana bardzo przez dzieci."
                          )
    Recipe.objects.create(name="Kalafior panierowany", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Zwykły, dość mdły kalafior ugotowany w wodzie nabierze wyrazistości, jeśli obtoczymy go w jajku i bułce tartej, a następnie usmażymy na złoty kolor. Taki kalafior pasuje jako dodatek do głównego dania. Można serwować go np. zamiast mięsa z ziemniakami i surówką. Można jeść go również samego, jako przekąskę, na zimno lub ciepło."
                          )
    Recipe.objects.create(name="Kalafior pieczony", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Ciepły, chrupiący kalafior z piekarnika z przyprawami. Upieczony jest w piekarniku bez dodatku oleju. Różyczki kalafiora obtoczone są w przyprawach wymieszanych w wodzie, dzięki której przykleją się one do warzywa. Bardzo smaczny i jakże prosty do przygotowania. Polecam podawać z surówką z marchewki i jabłka."
                          )
    Recipe.objects.create(name="Kotlety ziemniaczano- kalafiorowo- brokułowe", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Warzywne kotlety z ziemniaków, kalafiora i brokuła. Smaczne, lekkie, a zarazem pożywne."
                          )
    Recipe.objects.create(name="Krem kalafiorowy", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Gęsta, sycąca zupa- krem z kalafiora. Jest prosta, smaczna i pożywna."
                          )
    Recipe.objects.create(name="Zapiekanka kalafiorowo- makaronowa", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Makaron zapiekany z kalafiorem, marchewką i papryką. Przykryty pyszną warstwą migdałowo- serową."
                          )
    Recipe.objects.create(name="Ciasto z mięsa mielonego", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Ładnie podane mięso mielone z dodatkiem warzyw, zawinięte w ciasto francuskie. Sycące danie obiadowe. Do potrawy pasuje sos cebulowy lub tzatziki."
                          )
    Recipe.objects.create(name="Cukinia faszerowana mięsem mielonym", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Lekki i zdrowy obiad, który jest bezglutenowy, bezmleczny, bezjajeczny i niskowęglowodanowy. Tak przygotowane cukinie są soczyste, lekkie, a zarazem sycące."
                          )
    Recipe.objects.create(name="Cukinia i bakłażan w jajku", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Plastry cukinii i bakłażana obtoczone w jajku i usmażone na oleju. Mogą stanowić przekąskę lub dodatek na ciepło do dania głównego. Szczególnie polecam tak przygotowane warzywa osobom będącym na diecie low carb."
                          )
    Recipe.objects.create(name="Curry z cukinii, ciecierzycy i pieczarek", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Cukinia z ciecierzycą i pieczarkami z mlekiem kokosowym. Szybkie danie jednogarnkowe, bezglutenowe, niskowęglowodanowe i jeśli użyjecie bulionu warzywnego również wegańskie. Jest sycące, kremowe i pikantne (w zależności od ilości dodanej pasty curry). Danie jest proste do przygotowania i gotowe w 40 minut. Jeśli danie nie musi być niskowęglowodanowe, to możecie podawać go z ryżem, ale nie jest to konieczne, bo jest treściwe samo w sobie ;)"
                          )
    Recipe.objects.create(name="Gniazdka makaronowe", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Takie gniazdka makaronowe nadają się jako przystawka na ciepło lub też na obiad."
                          )
    Recipe.objects.create(name="Jak przygotować kwiaty cukinii", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Kwiaty cukinii przywiozłam z Włoch. Są one tam bardzo popularne i można je dostać zarówno na bazarze jak i w supermarkecie. W Polsce niestety nie są aż tak popularne. Jeśli uda Wam się je dostać na targu lub macie je na działce to zachęcam do ich przygotowania, bo są bardzo smaczne."
                          )
    Recipe.objects.create(name="Krem z cukinii", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Dietetyczny krem z cukinii, bez dodatku śmietany, ani oleju do smażenia cebuli. Przepis jest zgodny z dietą dr Dąbrowskiej, a zupa- krem z cukinii jest bardzo smaczna. Można ją wzbogacić smakowo, posypując rzeżuchą lub szczypiorkiem."
                          )
    Recipe.objects.create(name="Kwiaty cukinii w tempurze", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Pyszna, wykwintna i chrupiąca przekąska. Należy podawać ją na ciepło, od razu po usmażeniu. Jest wówczas chrupiąca na zewnątrz, a w środku delikatna. Polecam podawać z sałatą i świeżym pieczywem np. focaccią."
                          )
    Recipe.objects.create(name="Lasagne z łososiem i cukinią", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Ciekawa alternatywa dla klasycznej lasagne. Makaron, łosoś wędzony, młode cukinie i sos beszamelowy to dobrze dobrany zestaw smakowy. Do tego dość szybki do przygotowania."
                          )
    Recipe.objects.create(name="Leczo z cukinii", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Lekkie danie, którego głównym składnikiem jest cukinia. Można przygotowywać je przez cały rok. W sezonie letnim można skorzystać ze świeżych pomidorów, a w zimie z pomidorów z puszki. Polecam podawać leczo z bagietką."
                          )
    Recipe.objects.create(name="Placki z cukinii", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Delikatne, lekkie i bardzo smaczne placki z cukinii. Można serwować je jako główne danie tylko z dodatkiem kwaśnej śmietany lub sosu tzatziki, albo jako dodatek do mięsa, czy ryby.",
                          )
    Recipe.objects.create(name="Ratatouille", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Warzywne, jednogarnkowe, dietetyczne danie wywodzące się z kuchni francuskiej. Składa się z samych przysmażonych i podduszonych warzyw, przyprawionych ziołami prowansalskimi. Można podawać je zarówna na zimno, jak i na ciepło. W skład Ratatouille wchodzi: bakłażan, cukinia, pomidor, papryka, cebula i czosnek. Warzywa krojone są na kawałki i smażone na oliwie z oliwek. Polecam smażyć warzywa oddzielnie, a na końcu połączyć i chwilę razem poddusić. W ten sposób warzywa zachowają swój kształt.",
                          )
    Recipe.objects.create(name="Risotto z kurczakiem", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Risotto z kurczakiem, cukinią i pomidorami to proste, aromatyczne i sycące danie jednogarnkowe. Przygotowanie jest bardzo proste. Wymaga jedynie trochę cierpliwości i spokoju ;). Ryż bowiem nie gotujemy tradycyjnie, a podsmażamy na patelni, aż zrobi się szklisty. Następnie dodajemy stopniowo wino i wywar. Pod koniec gotowania dodajemy warzywa i mięso.",
                          )
    Recipe.objects.create(name="Sałatka warzywna na ciepło", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Bogata, kolorowa i smaczna sałatka przygotowana na ciepło. Może być serwowana, jako ciepła przystawka lub też stanowić samodzielne, lekkie danie. Pyszna z czosnkowymi grzankami tostowymi.",
                          )
    Recipe.objects.create(name="Sałatka z kawowym winegret", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Lekka sałatka z zielonej sałaty, smażonych plastrów cukinii i pieczarek z kawowym sosem winegret. Smażona cukinia i pieczarki świetnie harmonizują z aromatem kawowym. Sałatka smaczna sama. Pasuje również do smażonych warzyw i mięs.",
                          )
    Recipe.objects.create(name="Spaghetti Carbonara z cukinią", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Spaghetti z sosem Carbonara, przygotowanym na samych żółtkach i wzbogaconym o kawałki cukinii.",
                          )
    Recipe.objects.create(name="Tarta z kwiatami cukinii", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Tarta na bogato, przygotowana z ciasta francuskiego, sera ricotta i kwiatów cukinii. Wykwintne, nietuzinkowe danie. Tarta najlepiej smakuje podana lekko ciepła w towarzystwie sałaty.",
                          )
    Recipe.objects.create(name="Warzywa pieczone", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Pieczone warzywa z piekarnika smakują wyśmienicie same, ale stanowią również idealny dodatek do mięsa, czy też ryby.",
                          )
    Recipe.objects.create(name="Zapiekane kwiaty cukinii z mozzarellą", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Kolejna propozycja na przygotowanie pysznej potrawy z wykorzystaniem kwiatów cukinii. Tym razem wybrałam kwiaty żeńskie z małymi cukiniami, ale nic nie stoi na przeszkodzie, aby wybrać same kwiaty. Można podawać je jako przystawkę na ciepło lub w towarzystwie sałatki i świeżego pieczywa jako samodzielne, lekkie danie.",
                          )
    Recipe.objects.create(name="Zupa krem z ziemniaka i cukinii", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Zdrowa, lekka, kremowa zupa z cukinii. Szybka, łatwa, a do tego aromatyczna. Podałam ją z kleksem gęstej śmietany, jako pierwsze danie. Jeśli ma być bardziej konkretna to można podać ją z grzankami lub świeżym pieczywem.",
                          )
    Recipe.objects.create(name="Cannelloni z dynią pod beszamelem", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Rurki cannelloni nadziewane puree z dyni, zapiekane pod sosem beszamelowym i startym serem. Delikatne, kremowe, lekko słodkie i bardzo smaczne danie. Polecam dobrze doprawić puree i sos, aby potrawa nabrała wyrazistego smaku. Pasuje szczególnie na obiad lub jako danie dla gości.",
                          )
    Recipe.objects.create(name="Tagliatelle z sosem dyniowym", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Makaron z kremowym sosem dyniowym. Sos polany jest olejem z pestek dyni i posypany  uprażonymi pestkami z dyni, rukolą i parmezanem. Proste, szybkie a w smaku pyszne.",
                          )
    Recipe.objects.create(name="Zupa dyniowa z mlekiem kokosowym i pomarańczą", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Kremowa zupa dyniowa z mlekiem kokosowym i pomarańczą. Pyszna, kremowa, aromatyczna, sycąca i rozgrzewająca. Podałam ją ze smażonymi, drobno pokrojonymi ziemniakami, zieloną cebulką i ziarnami słonecznika.",
                          )
    Recipe.objects.create(name="Zupa z dyni z mięsem mielonym", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Smaczna, kremowa i pikantna zupa ugotowana na wytrawnym winie. Świetna alternatywa do lekko słodkiego kremu z dyni. (Przepis tutaj: „Zupa- krem z dyni”). ",
                          )
    Recipe.objects.create(name="Zupa- krem z dyni", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Przepis na pyszną zupę krem z dyni. Uwielbiam tę zupę. Pora jesienna to okazja do jej przygotowania. Jest bardzo delikatna, kremowa, łagodna, a cytryna i imbir nadają jej ciekawego smaku.",
                          )
    Recipe.objects.create(name="Sałatka z pomidorami, awokado i mozzarellą", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Bardzo szybka do przygotowania, lekka sałatka z małych pomidorków, mini mozzarelli i awokado z dodatkiem pesto z bazylii. Można podać ją do mięsa z grilla, jako przekąskę, czy lekką kolację samą lub z pieczywem.",
                          )
    Recipe.objects.create(name="Sałatka ze szpinakiem i kurczakiem", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Zdrowa sałatka bez węglowodanów ze świeżych warzyw i smażonego kurczakiem. Kawałki usmażonej piersi z kurczaka ze świeżym szpinakiem, pomidorami, oliwkami i awokado, polane sosem czosnkowym to propozycja na lekki, dietetyczny, prosty i szybki obiad lub kolację.",
                          )
    Recipe.objects.create(name="Sałatka jajeczna", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Prosta i szybka sałatka z jajek i majonezu. Wzbogacona dodatkiem ogórków korniszonych. Można dodać również zieloną cebulkę lub szczypiorek. Dla dzieci robię same jajka z ogórkiem, a dla nas jeszcze z zieleniną ;) Można podawać ją jako pastę do chleba lub samą, jak każdą sałatkę majonezową.",
                          )
    Recipe.objects.create(name="Bawarska obazda", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Obazda bawarska to pasta serowa z sera Camembert, cebuli i papryki w proszku. Klasyk na Bawarii. Pastę serwuje się z preclem. W klasycznej wersji dodaje się kminek. Możecie go dodać jeśli lubicie, ja za nim nie przepadam ;).",
                          )
    Recipe.objects.create(name="Bezglutenowe naleśniki gryczane", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Naleśniki z mąki gryczanej. Można podawać je zarówno z nadzieniem słodkim, jak również wytrawnym. W przypadku słodkiego nadzienia można do ciasta naleśnikowego dodać jeszcze 1- 2 łyżeczki cukru.",
                          )
    Recipe.objects.create(name="Biała kiełbasa pieczona z cebulą i jabłkami", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Pieczona biała kiełbasa z cebulą i kawałkami jabłek to pomysł na świąteczne śniadanie wielkanocne. Jest to wersja lekko słodka z soczystymi, słodkawymi jabłkami i delikatną cebulą. Aromatyczne, proste i szybkie do przygotowania danie nie tylko na Wielkanoc.",
                          )
    Recipe.objects.create(name="Bruschetta z pomidorami", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Typowa włoska przystawka, składająca się z grzanki posmarowanej czosnkiem i oliwą. W wersji klasycznej podawana jest z pomidorami pokrojonymi w kostkę i bazylią lub cebulką.",
                          )
    Recipe.objects.create(name="Buraczano- ananasowe smoothie", preparation_description="otworz opakowanie, wysyp skladniki", ingredients="skladnik1, skladnik2", description="Czerwona bomba witaminowa. Odżywcze smoothie z ananasa i buraków. W smaku zarówno ananas jak i burak są mocno wyczuwalne.",
                          )


class Migration(migrations.Migration):
    dependencies = [
        ('jedzonko', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate),
    ]
