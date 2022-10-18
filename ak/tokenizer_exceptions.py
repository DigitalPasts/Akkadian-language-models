#This dictionary contains all proper nouns culled from SAA1 (many of which are hyphenated), as well as select inflected forms of common nouns containing hyphens (e.g. sa-resi 'eunuch')

from spacy.lang.tokenizer_exceptions import BASE_EXCEPTIONS
from spacy.symbols import ORTH, NORM, LEMMA
from spacy.util import update_exc

exclusions = [

{
   'Ṭab-šar-Aššur':[{ORTH:    'Ṭab-šar-Aššur'}],
   'Kalha':[{ORTH:    'Kalha'}],
   'Arrapha':[{ORTH:    'Arrapha'}],
   'Sin-ahhe-eriba':[{ORTH:    'Sin-ahhe-eriba'}],
   'Mat-Aššur':[{ORTH:    'Mat-Aššur'}],
   'Kumme':[{ORTH:    'Kumme'}],
   'Ariye':[{ORTH:    'Ariye'}],
   'Ukkaya':[{ORTH:    'Ukkaya'}],
   'Urarṭaya':[{ORTH:    'Urarṭaya'}],
   'Kummaya':[{ORTH:    'Kummaya'}],
   'Eluli':[{ORTH:    'Eluli'}],
   'Aššur-reṣuwa':[{ORTH:    'Aššur-reṣuwa'}],
   'Zikirtaya':[{ORTH:    'Zikirtaya'}],
   'Waisi':[{ORTH:    'Waisi'}],
   'Mannaya':[{ORTH:    'Mannaya'}],
   'Arzabiaya':[{ORTH:    'Arzabiaya'}],
   'Sadudaya':[{ORTH:    'Sadudaya'}],
   'Ahu-lurši':[{ORTH:    'Ahu-lurši'}],
   'Bel':[{ORTH:    'Bel'}],
   'Nabu':[{ORTH:    'Nabu'}],
   'Marduk':[{ORTH:    'Marduk'}],
   'Nisanni':[{ORTH:    'Nisanni'}],
   'dir-Addari':[{ORTH:    'dir-Addari'}],
   'Dur-Šarruken':[{ORTH:    'Dur-Šarruken'}],
   'Babili':[{ORTH:    'Babili'}],
   'Aššur-šarru-uṣur':[{ORTH:    'Aššur-šarru-uṣur'}],
   'Quwe':[{ORTH:    'Quwe'}],
   'Amar-ili':[{ORTH:    'Amar-ili'}],
   'Nabu-deʾiq':[{ORTH:    'Nabu-deʾiq'}],
   'Sikris':[{ORTH:    'Sikris'}],
   'Balṭi-iqbi':[{ORTH:    'Balṭi-iqbi'}],
   'Mannu-ki-Aššur-leʾi':[{ORTH:    'Mannu-ki-Aššur-leʾi'}],
   'Zarana':[{ORTH:    'Zarana'}],
   'Bel-duri':[{ORTH:    'Bel-duri'}],
   'Guzana':[{ORTH:    'Guzana'}],
   'Aridi':[{ORTH:    'Aridi'}],
   'Kubanaše':[{ORTH:    'Kubanaše'}],
   'Kapar-Mariyaba':[{ORTH:    'Kapar-Mariyaba'}],
   'Ilhini':[{ORTH:    'Ilhini'}],
   'Kapar-Amdanu':[{ORTH:    'Kapar-Amdanu'}],
   'Bur-šarri':[{ORTH:    'Bur-šarri'}],
   'Ṭab-ṣil-Ešarra':[{ORTH:    'Ṭab-ṣil-Ešarra'}],
   'Aššur':[{ORTH:    'Aššur'}],
   'Mullissu':[{ORTH:    'Mullissu'}],
   'Libbi-ali':[{ORTH:    'Libbi-ali'}],
   'Mardi':[{ORTH:    'Mardi'}],
   'Ninua':[{ORTH:    'Ninua'}],
   'Mat-Akkadi':[{ORTH:    'Mat-Akkadi'}],
   'Ṭabi':[{ORTH:    'Ṭabi'}],
   'Zeru-ibni':[{ORTH:    'Zeru-ibni'}],
   'Erra-gamil':[{ORTH:    'Erra-gamil'}],
   'Nabu-šumu-uṣur':[{ORTH:    'Nabu-šumu-uṣur'}],
   'Nemed-Issaraya':[{ORTH:    'Nemed-Issaraya'}],
   'Laqaya':[{ORTH:    'Laqaya'}],
   'Ilaʾi-Bel':[{ORTH:    'Ilaʾi-Bel'}],
   'Eber-nāri':[{ORTH:    'Eber-nāri'}],
   'Ṣululu':[{ORTH:    'Ṣululu'}],
   'Bursibi':[{ORTH:    'Bursibi'}],
   'Birate':[{ORTH:    'Birate'}],
   'Birataya':[{ORTH:    'Birataya'}],
   'Henzana':[{ORTH:    'Henzana'}],
   'Henzanana':[{ORTH:    'Henzanana'}],
   'Aššur-bani':[{ORTH:    'Aššur-bani'}],
   'Bet-Issar':[{ORTH:    'Bet-Issar'}],
   'Bet-Kadmuri':[{ORTH:    'Bet-Kadmuri'}],
   'Bet-Sebetti':[{ORTH:    'Bet-Sebetti'}],
   'Bet-Adad-ša-zunni':[{ORTH:    'Bet-Adad-ša-zunni'}],
   'Kiṣir-Aššur':[{ORTH:    'Kiṣir-Aššur'}],
   'Alu-ša-tamkari':[{ORTH:    'Alu-ša-tamkari'}],
   'Šitabni':[{ORTH:    'Šitabni'}],
   'Šamaš':[{ORTH:    'Šamaš'}],
   'Kalhi':[{ORTH:    'Kalhi'}],
   'Aššurate':[{ORTH:    'Aššurate'}],
   'Adia':[{ORTH:    'Adia'}],
   'Bel-iqbi':[{ORTH:    'Bel-iqbi'}],
   'Aššur-ašared':[{ORTH:    'Aššur-ašared'}],
   'Hamataya':[{ORTH:    'Hamataya'}],
   'Ina-šar-Bel-allak':[{ORTH:    'Ina-šar-Bel-allak'}],
   'Šabirešu':[{ORTH:    'Šabirešu'}],
   'Kina':[{ORTH:    'Kina'}],
   'Sanda-pi':[{ORTH:    'Sanda-pi'}],
   'Huli':[{ORTH:    'Huli'}],
   'Kuza':[{ORTH:    'Kuza'}],
   'Bet-Nabu':[{ORTH:    'Bet-Nabu'}],
   'Ubru-Babili':[{ORTH:    'Ubru-Babili'}],
   'Arpadda':[{ORTH:    'Arpadda'}],
   'Nabu-belu-kaʾʾin':[{ORTH:    'Nabu-belu-kaʾʾin'}],
   'Nabu-pašir':[{ORTH:    'Nabu-pašir'}],
   'Marubisi':[{ORTH:    'Marubisi'}],
   'Aššur-reši-išši':[{ORTH:    'Aššur-reši-išši'}],
   'Bit-Barrue':[{ORTH:    'Bit-Barrue'}],
   'Kibabaše':[{ORTH:    'Kibabaše'}],
   'Ašpa-bari':[{ORTH:    'Ašpa-bari'}],
   'Šabaṭi':[{ORTH:    'Šabaṭi'}],
   'Nani':[{ORTH:    'Nani'}],
   'Suhaya':[{ORTH:    'Suhaya'}],
   'Ahu-illika':[{ORTH:    'Ahu-illika'}],
   'Zabina-ili':[{ORTH:    'Zabina-ili'}],
   'Laqe':[{ORTH:    'Laqe'}],
   'Gidgiddani':[{ORTH:    'Gidgiddani'}],
   'Arbail':[{ORTH:    'Arbail'}],
   'Marduk-remanni':[{ORTH:    'Marduk-remanni'}],
   'Libbalaya':[{ORTH:    'Libbalaya'}],
   'Aššur-neše':[{ORTH:    'Aššur-neše'}],
   'Harrani':[{ORTH:    'Harrani'}],
   'Halahhi':[{ORTH:    'Halahhi'}],
   'Ṭebeti':[{ORTH:    'Ṭebeti'}],
   'Sin-ašared':[{ORTH:    'Sin-ašared'}],
   'Arpaddaya':[{ORTH:    'Arpaddaya'}],
   'Aššur-šumu-kaʾʾin':[{ORTH:    'Aššur-šumu-kaʾʾin'}],
   'Tastiate':[{ORTH:    'Tastiate'}],
   'Marduk-šumu-iddina':[{ORTH:    'Marduk-šumu-iddina'}],
   'Taklak-ana-Bel':[{ORTH:    'Taklak-ana-Bel'}],
   'Ilu-iqbi':[{ORTH:    'Ilu-iqbi'}],
   'Šamaš-upahhir':[{ORTH:    'Šamaš-upahhir'}],
   'Habruri':[{ORTH:    'Habruri'}],
   'Nagaha':[{ORTH:    'Nagaha'}],
   'Ilu-piya-uṣur':[{ORTH:    'Ilu-piya-uṣur'}],
   'Taklak-Bel':[{ORTH:    'Taklak-Bel'}],
   'Nabu-dur-maki':[{ORTH:    'Nabu-dur-maki'}],
   'Sin':[{ORTH:    'Sin'}],
   'Nikkal':[{ORTH:    'Nikkal'}],
   'Patti-Illil':[{ORTH:    'Patti-Illil'}],
   'Nabu-bel-šumati':[{ORTH:    'Nabu-bel-šumati'}],
   'Galṣabri':[{ORTH:    'Galṣabri'}],
   'Arbailaya':[{ORTH:    'Arbailaya'}],
   'Tariba-Issar':[{ORTH:    'Tariba-Issar'}],
   'Kummuhaya':[{ORTH:    'Kummuhaya'}],
   'Aplaya':[{ORTH:    'Aplaya'}],
   'Šarru-lu-dari':[{ORTH:    'Šarru-lu-dari'}],
   'Išmanni-Aššur':[{ORTH:    'Išmanni-Aššur'}],
   'Taʾuzi':[{ORTH:    'Taʾuzi'}],
   'Nabu-belu-uṣur':[{ORTH:    'Nabu-belu-uṣur'}],
   'Dinanu':[{ORTH:    'Dinanu'}],
   'Bur-Ṣaruru':[{ORTH:    'Bur-Ṣaruru'}],
   'Marqasi':[{ORTH:    'Marqasi'}],
   'Hindana':[{ORTH:    'Hindana'}],
   'Qurani':[{ORTH:    'Qurani'}],
   'Halzi-atbar':[{ORTH:    'Halzi-atbar'}],
   'Bel-eṭir':[{ORTH:    'Bel-eṭir'}],
   'Nabu-eṭir-napšati':[{ORTH:    'Nabu-eṭir-napšati'}],
   'Nabu-mušallim':[{ORTH:    'Nabu-mušallim'}],
   'Muṣuraya':[{ORTH:    'Muṣuraya'}],
   'Hazzataya':[{ORTH:    'Hazzataya'}],
   'Yaʾuduaya':[{ORTH:    'Yaʾuduaya'}],
   'Maʾabaya':[{ORTH:    'Maʾabaya'}],
   'Ban-Ammanaya':[{ORTH:    'Ban-Ammanaya'}],
   'Udumuaya':[{ORTH:    'Udumuaya'}],
   'Anqarrunaya':[{ORTH:    'Anqarrunaya'}],
   'Quwaya':[{ORTH:    'Quwaya'}],
   'Zabban':[{ORTH:    'Zabban'}],
   'Qappataya':[{ORTH:    'Qappataya'}],
   'Urammu':[{ORTH:    'Urammu'}],
   'Elamaya':[{ORTH:    'Elamaya'}],
   'Sumurzu':[{ORTH:    'Sumurzu'}],
   'Banitu':[{ORTH:    'Banitu'}],
   'Aššur-belu-taqqin':[{ORTH:    'Aššur-belu-taqqin'}],
   'Kapar-Diqarate':[{ORTH:    'Kapar-Diqarate'}],
   'Nabu-duru-uṣur':[{ORTH:    'Nabu-duru-uṣur'}],
   'Tarriki-hallu':[{ORTH:    'Tarriki-hallu'}],
   'Arpaya':[{ORTH:    'Arpaya'}],
   'Hinzani':[{ORTH:    'Hinzani'}],
   'Tartari':[{ORTH:    'Tartari'}],
   'Suhi':[{ORTH:    'Suhi'}],
   'Izalli':[{ORTH:    'Izalli'}],
   'Parak-šimati':[{ORTH:    'Parak-šimati'}],
   'Issar-tašme':[{ORTH:    'Issar-tašme'}],
   'Me-ṭabute':[{ORTH:    'Me-ṭabute'}],
   'Amante':[{ORTH:    'Amante'}],
   'Kasappa':[{ORTH:    'Kasappa'}],
   'Ituʾayeya':[{ORTH:    'Ituʾayeya'}],
   'Sinni':[{ORTH:    'Sinni'}],
   'Keni':[{ORTH:    'Keni'}],
   'Sapirrite':[{ORTH:    'Sapirrite'}],
   'Ekallat':[{ORTH:    'Ekallat'}],
   'Metunu':[{ORTH:    'Metunu'}],
   'Ayari':[{ORTH:    'Ayari'}],
   'Anisu':[{ORTH:    'Anisu'}],
   'Habhu':[{ORTH:    'Habhu'}],
   'Yeri':[{ORTH:    'Yeri'}],
   'Nisannu':[{ORTH:    'Nisannu'}],
   'Marduk-eriba':[{ORTH:    'Marduk-eriba'}],
   'Hunni':[{ORTH:    'Hunni'}],
   'Paqaha':[{ORTH:    'Paqaha'}],
   'Talmusa':[{ORTH:    'Talmusa'}],
   'Ubase':[{ORTH:    'Ubase'}],
   'Ešarra':[{ORTH:    'Ešarra'}],
   'Ekallati':[{ORTH:    'Ekallati'}],
   'Pan-Aššur-lamur':[{ORTH:    'Pan-Aššur-lamur'}],
   'Adad':[{ORTH:    'Adad'}],
   'Buru':[{ORTH:    'Buru'}],
   'Duru':[{ORTH:    'Duru'}],
   'Nergal-balliṭ':[{ORTH:    'Nergal-balliṭ'}],
   'Pilistaya':[{ORTH:    'Pilistaya'}],
   'Luqaše':[{ORTH:    'Luqaše'}],
   'Urabi':[{ORTH:    'Urabi'}],
   'Ituʾaya':[{ORTH:    'Ituʾaya'}],
   'Anum':[{ORTH:    'Anum'}],
   'Gambuli':[{ORTH:    'Gambuli'}],
   'Illipa':[{ORTH:    'Illipa'}],
   'Humbe':[{ORTH:    'Humbe'}],
   'Huziri':[{ORTH:    'Huziri'}],
   'Šarru-emuranni':[{ORTH:    'Šarru-emuranni'}],
   'Adda-hati':[{ORTH:    'Adda-hati'}],
   'Hamate':[{ORTH:    'Hamate'}],
   'Arihi':[{ORTH:    'Arihi'}],
   'Samirnaya':[{ORTH:    'Samirnaya'}],
   'Sili':[{ORTH:    'Sili'}],
   'Šep-Aššur':[{ORTH:    'Šep-Aššur'}],
   'Zaba':[{ORTH:    'Zaba'}],
   'Šulmu-beli':[{ORTH:    'Šulmu-beli'}],
   'Urzanna':[{ORTH:    'Urzanna'}],
   'Gimir':[{ORTH:    'Gimir'}],
   'Urarṭi':[{ORTH:    'Urarṭi'}],
   'Hubuškia':[{ORTH:    'Hubuškia'}],
   'Dada':[{ORTH:    'Dada'}],
   'Adad-iriba':[{ORTH:    'Adad-iriba'}],
   'Ištahup':[{ORTH:    'Ištahup'}],
   'Armaya':[{ORTH:    'Armaya'}],
   'Yaʾudaya':[{ORTH:    'Yaʾudaya'}],
   'Raṣappa':[{ORTH:    'Raṣappa'}],
   'Til-Barsiba':[{ORTH:    'Til-Barsiba'}],
   'Adad-ibni':[{ORTH:    'Adad-ibni'}],
   'Nampigi':[{ORTH:    'Nampigi'}],
   'Qipani':[{ORTH:    'Qipani'}],
   'Samnuha-belu-uṣur':[{ORTH:    'Samnuha-belu-uṣur'}],
   'Šedikannaya':[{ORTH:    'Šedikannaya'}],
   'Mannu-ki-Adad':[{ORTH:    'Mannu-ki-Adad'}],
   'Kurbail':[{ORTH:    'Kurbail'}],
   'Adad-nuri':[{ORTH:    'Adad-nuri'}],
   'Milqia':[{ORTH:    'Milqia'}],
   'Addari':[{ORTH:    'Addari'}],
   'Urzuhina':[{ORTH:    'Urzuhina'}],
   'Ruqahaya':[{ORTH:    'Ruqahaya'}],
   'Birat':[{ORTH:    'Birat'}],
   'Sippar':[{ORTH:    'Sippar'}],
   'Zuhi':[{ORTH:    'Zuhi'}],
   'Simani':[{ORTH:    'Simani'}],
   'Bab-bitqi':[{ORTH:    'Bab-bitqi'}],
   'Upia':[{ORTH:    'Upia'}],
   'Ziziru':[{ORTH:    'Ziziru'}],
   'Zabbua':[{ORTH:    'Zabbua'}],
   'Mardu':[{ORTH:    'Mardu'}],
   'Nabu-zer-ketti-lešir':[{ORTH:    'Nabu-zer-ketti-lešir'}],
   'Gidgiddanu':[{ORTH:    'Gidgiddanu'}],
   'Kislimi':[{ORTH:    'Kislimi'}],
   'Bet-Aššur':[{ORTH:    'Bet-Aššur'}],
   'Halzi':[{ORTH:    'Halzi'}],
   'Nabu-uṣalla':[{ORTH:    'Nabu-uṣalla'}],
   'Ašipa':[{ORTH:    'Ašipa'}],
   'Nabu-šezibanni':[{ORTH:    'Nabu-šezibanni'}],
   'Arahsamni':[{ORTH:    'Arahsamni'}],
   'Bet-Sin':[{ORTH:    'Bet-Sin'}],
   'Bet-Šamaš':[{ORTH:    'Bet-Šamaš'}],
   'Bet-Nikkal':[{ORTH:    'Bet-Nikkal'}],
   'Tašriti':[{ORTH:    'Tašriti'}],
   'Inurta-belu-uṣur':[{ORTH:    'Inurta-belu-uṣur'}],
   'Issar':[{ORTH:    'Issar'}],
   'Gir-Dadi':[{ORTH:    'Gir-Dadi'}],
   'Til-Turi':[{ORTH:    'Til-Turi'}],
   'Seʾ-lukidi':[{ORTH:    'Seʾ-lukidi'}],
   'Tabali':[{ORTH:    'Tabali'}],
   'Dur-Yakini':[{ORTH:    'Dur-Yakini'}],
   'Nergal':[{ORTH:    'Nergal'}],
   'Akbur':[{ORTH:    'Akbur'}],
   'Adda-šumki':[{ORTH:    'Adda-šumki'}],
   'Labarmu':[{ORTH:    'Labarmu'}],
   'Appa':[{ORTH:    'Appa'}],
   'Sinaya':[{ORTH:    'Sinaya'}],
   'Nabataya':[{ORTH:    'Nabataya'}],
   'Til-Bursiba':[{ORTH:    'Til-Bursiba'}],
   'Bel-liqbi':[{ORTH:    'Bel-liqbi'}],
   'Arbaya':[{ORTH:    'Arbaya'}],
   'Barhalza':[{ORTH:    'Barhalza'}],
   'Mutianni':[{ORTH:    'Mutianni'}],
   'Šibirtu':[{ORTH:    'Šibirtu'}],
   'Huhhi':[{ORTH:    'Huhhi'}],
   'Tabalu':[{ORTH:    'Tabalu'}],
   'Meta':[{ORTH:    'Meta'}],
   'Muskaya':[{ORTH:    'Muskaya'}],
   'Urik':[{ORTH:    'Urik'}],
   'Urpalaʾa':[{ORTH:    'Urpalaʾa'}],
   'Kilar':[{ORTH:    'Kilar'}],
   'Atunnaya':[{ORTH:    'Atunnaya'}],
   'Istuandaya':[{ORTH:    'Istuandaya'}],
   'Bit-Paruta':[{ORTH:    'Bit-Paruta'}],
   'Balassu':[{ORTH:    'Balassu'}],
   'Barsip':[{ORTH:    'Barsip'}],
   'Kišaya':[{ORTH:    'Kišaya'}],
   'Nippuraya':[{ORTH:    'Nippuraya'}],
   'Urukaya':[{ORTH:    'Urukaya'}],
   'Deraya':[{ORTH:    'Deraya'}],
   'Samnuhu-belu-uṣur':[{ORTH:    'Samnuhu-belu-uṣur'}],
   'Madaya':[{ORTH:    'Madaya'}],
   'Gurdi':[{ORTH:    'Gurdi'}],
   'Abi':[{ORTH:    'Abi'}],
   'Mannu-ki-Aššur':[{ORTH:    'Mannu-ki-Aššur'}],
   'Aššur-balti-niše':[{ORTH:    'Aššur-balti-niše'}],
   'Urarṭitu':[{ORTH:    'Urarṭitu'}],
   'Gargamisaya':[{ORTH:    'Gargamisaya'}],
   'Duri-Adad':[{ORTH:    'Duri-Adad'}],
   'Adad-abuʾa':[{ORTH:    'Adad-abuʾa'}],
   'Ubru-Libbali':[{ORTH:    'Ubru-Libbali'}],
   'Tarbasibaya':[{ORTH:    'Tarbasibaya'}],
   'Saraga':[{ORTH:    'Saraga'}],
   'Arzabia':[{ORTH:    'Arzabia'}],
   'Puqudaya':[{ORTH:    'Puqudaya'}],
   'Siʾimme':[{ORTH:    'Siʾimme'}],
   'Rahdiaba':[{ORTH:    'Rahdiaba'}],
   'Simanaya':[{ORTH:    'Simanaya'}],
   'Nabu-balliṭ':[{ORTH:    'Nabu-balliṭ'}],
   'Aššur-naʾdi':[{ORTH:    'Aššur-naʾdi'}],
   'Isana':[{ORTH:    'Isana'}],
   'Tabni-ilu':[{ORTH:    'Tabni-ilu'}],
   'Nabu-šezib':[{ORTH:    'Nabu-šezib'}],
   'Izalla':[{ORTH:    'Izalla'}],
   'Tarbusibi':[{ORTH:    'Tarbusibi'}],
   'Tarqunani':[{ORTH:    'Tarqunani'}],
   'Tasi':[{ORTH:    'Tasi'}],
   'Upumu':[{ORTH:    'Upumu'}],
   'Inurta-ilaʾi':[{ORTH:    'Inurta-ilaʾi'}],
   'Hasaya':[{ORTH:    'Hasaya'}],
   'Nemed-Ištar':[{ORTH:    'Nemed-Ištar'}],
   'Sini':[{ORTH:    'Sini'}],
   'Gargamis':[{ORTH:    'Gargamis'}],
   'Dannaya':[{ORTH:    'Dannaya'}],
   'Argite':[{ORTH:    'Argite'}],
   'Ṣupite':[{ORTH:    'Ṣupite'}],
   'Labaʾu':[{ORTH:    'Labaʾu'}],
   'Aššuraya':[{ORTH:    'Aššuraya'}],
   'Išpa-bara':[{ORTH:    'Išpa-bara'}],
   'Lutu':[{ORTH:    'Lutu'}],
   'Aššur-bessunu':[{ORTH:    'Aššur-bessunu'}],
   'Kuluman':[{ORTH:    'Kuluman'}],
   'Samnuhu-bessunu':[{ORTH:    'Samnuhu-bessunu'}],
   'Kannuʾaya':[{ORTH:    'Kannuʾaya'}],
   'Maliasu':[{ORTH:    'Maliasu'}],
   'Saʾili':[{ORTH:    'Saʾili'}],
   'Sadiru':[{ORTH:    'Sadiru'}],
   'Elizki':[{ORTH:    'Elizki'}],
   'Lili':[{ORTH:    'Lili'}],
   'Aššur-nadin-ahhe':[{ORTH:    'Aššur-nadin-ahhe'}],
   'Šamaš-ilaʾi':[{ORTH:    'Šamaš-ilaʾi'}],
   'Attunaya':[{ORTH:    'Attunaya'}],
   'Epa':[{ORTH:    'Epa'}],
   'Aššur-ilaʾi':[{ORTH:    'Aššur-ilaʾi'}],
   'Urdu-Issar':[{ORTH:    'Urdu-Issar'}],
   'Ṣil-Šamaš':[{ORTH:    'Ṣil-Šamaš'}],
   'Bel-deni-amur':[{ORTH:    'Bel-deni-amur'}],
   'Patamu':[{ORTH:    'Patamu'}],
   'Til-Bursibi':[{ORTH:    'Til-Bursibi'}],
   'Naʾdi-ilu':[{ORTH:    'Naʾdi-ilu'}],
   'Lurisite':[{ORTH:    'Lurisite'}],
   'Al-Aššur':[{ORTH:    'Al-Aššur'}],
   'Surimarrat':[{ORTH:    'Surimarrat'}],
   'Muṣaṣir':[{ORTH:    'Muṣaṣir'}],
   'Lapsia':[{ORTH:    'Lapsia'}],
   'Nergal-naṣir':[{ORTH:    'Nergal-naṣir'}],
   'Dugul-pan-ili':[{ORTH:    'Dugul-pan-ili'}],
   'Bel-age':[{ORTH:    'Bel-age'}],
   'Mat-rab-šaqe':[{ORTH:    'Mat-rab-šaqe'}],
   'Tille':[{ORTH:    'Tille'}],
   'Naṣibina':[{ORTH:    'Naṣibina'}],
   'Šuguraya':[{ORTH:    'Šuguraya'}],
   'Aššur-šarru-ibni':[{ORTH:    'Aššur-šarru-ibni'}],
   'Hamudu':[{ORTH:    'Hamudu'}],
   'Šuzubu':[{ORTH:    'Šuzubu'}],
   'Remute':[{ORTH:    'Remute'}],
   'Apku':[{ORTH:    'Apku'}],
   'Ṭabtaya':[{ORTH:    'Ṭabtaya'}],
   'Seʾ-gabbari':[{ORTH:    'Seʾ-gabbari'}],
   'Neribi':[{ORTH:    'Neribi'}],
   'Nur-Sin':[{ORTH:    'Nur-Sin'}],
   'Dadi-ibni':[{ORTH:    'Dadi-ibni'}],
   'Melidi':[{ORTH:    'Melidi'}],
   'Bahianu':[{ORTH:    'Bahianu'}],
   'Belu-lu-balaṭ':[{ORTH:    'Belu-lu-balaṭ'}],
   'Kukibi':[{ORTH:    'Kukibi'}],
   'Bahiani':[{ORTH:    'Bahiani'}],
   'Ubru-Nabu':[{ORTH:    'Ubru-Nabu'}],
   'Haldi-naṣir':[{ORTH:    'Haldi-naṣir'}],
   'Nipuri':[{ORTH:    'Nipuri'}],
   'Ammi-leʾti':[{ORTH:    'Ammi-leʾti'}],
   'Rabla':[{ORTH:    'Rabla'}],
   'Šulmu-beli-lašme':[{ORTH:    'Šulmu-beli-lašme'}],
   'Harranu':[{ORTH:    'Harranu'}],
   'Kuna':[{ORTH:    'Kuna'}],
   'Dur-Ladini':[{ORTH:    'Dur-Ladini'}],
   'Dur-Bilihaya':[{ORTH:    'Dur-Bilihaya'}],
   'Larak':[{ORTH:    'Larak'}],
   'Bit-Ukani':[{ORTH:    'Bit-Ukani'}],
   'Šarru-nuri':[{ORTH:    'Šarru-nuri'}],
   'Ṣimirra':[{ORTH:    'Ṣimirra'}],
   'Marhasaya':[{ORTH:    'Marhasaya'}],
   'Hadina':[{ORTH:    'Hadina'}],
   'Ameri':[{ORTH:    'Ameri'}],
   'Yasubuqi':[{ORTH:    'Yasubuqi'}],
   'Huzaza':[{ORTH:    'Huzaza'}],
   'ʾAtaya':[{ORTH:    'ʾAtaya'}],
   'Ṣupat':[{ORTH:    'Ṣupat'}],
   'Abattu':[{ORTH:    'Abattu'}],
   'Qanni':[{ORTH:    'Qanni'}],
   'Raṣappaya':[{ORTH:    'Raṣappaya'}],
   'Adian':[{ORTH:    'Adian'}],
   'Kalzi':[{ORTH:    'Kalzi'}],
   'Ṣil-Bel':[{ORTH:    'Ṣil-Bel'}],
   'Bel-nuri':[{ORTH:    'Bel-nuri'}],
   'Arraphaya':[{ORTH:    'Arraphaya'}],
   'Lubda':[{ORTH:    'Lubda'}],
   'Kar-Šamaš':[{ORTH:    'Kar-Šamaš'}],
   'Ṣibte':[{ORTH:    'Ṣibte'}],
   'Samerina':[{ORTH:    'Samerina'}],
   'Adad-isseʾa':[{ORTH:    'Adad-isseʾa'}],
   'Bel-lešir':[{ORTH:    'Bel-lešir'}],
   'Abu-lešir':[{ORTH:    'Abu-lešir'}],
   'Šamaš-ahu-iddina':[{ORTH:    'Šamaš-ahu-iddina'}],
   'Barhalzi':[{ORTH:    'Barhalzi'}],
   'Issete':[{ORTH:    'Issete'}],
   'Dadi-suri':[{ORTH:    'Dadi-suri'}],
   'Raʾsunu':[{ORTH:    'Raʾsunu'}],
   'Tarbusibaya':[{ORTH:    'Tarbusibaya'}],
   'Gabbi-amur':[{ORTH:    'Gabbi-amur'}],
   'Remanni-Adad':[{ORTH:    'Remanni-Adad'}],
   'Hamaranaya':[{ORTH:    'Hamaranaya'}],
   'Munuʾ':[{ORTH:    'Munuʾ'}],
   'Dimašqi':[{ORTH:    'Dimašqi'}],
   'Amiri':[{ORTH:    'Amiri'}],
   'Dimašqa':[{ORTH:    'Dimašqa'}],
   'Illabani':[{ORTH:    'Illabani'}],
   'Hallataya':[{ORTH:    'Hallataya'}],
   'Adad-remanni':[{ORTH:    'Adad-remanni'}],
   'Nabu-šumu-iddina':[{ORTH:    'Nabu-šumu-iddina'}],
   'Zari':[{ORTH:    'Zari'}],
   'Labdudu':[{ORTH:    'Labdudu'}],
   'Ariawate':[{ORTH:    'Ariawate'}],
   'Zahe':[{ORTH:    'Zahe'}],
   'Ilu-mušezib':[{ORTH:    'Ilu-mušezib'}],
   'Bel-emuranni':[{ORTH:    'Bel-emuranni'}],
   'Hatarikka':[{ORTH:    'Hatarikka'}],
   'Kubaba-ereš':[{ORTH:    'Kubaba-ereš'}],
   'Ilu-biʾdi':[{ORTH:    'Ilu-biʾdi'}],
   'Tuqunu':[{ORTH:    'Tuqunu'}],
   'Kimumaya':[{ORTH:    'Kimumaya'}],
   'Aššur-ereš':[{ORTH:    'Aššur-ereš'}],
   'Nabu-deni-epuš':[{ORTH:    'Nabu-deni-epuš'}],
   'Gamir':[{ORTH:    'Gamir'}],
   'Kaqqadanu':[{ORTH:    'Kaqqadanu'}],
   'Wazaun':[{ORTH:    'Wazaun'}],
   'Nabu-leʾi':[{ORTH:    'Nabu-leʾi'}],
   'Muṣaṣiraya':[{ORTH:    'Muṣaṣiraya'}],
   'Hubuškaya':[{ORTH:    'Hubuškaya'}],
   'Ahat-abiša':[{ORTH:    'Ahat-abiša'}],
   'Tabal':[{ORTH:    'Tabal'}],
   'Nabu-riba-ahhe':[{ORTH:    'Nabu-riba-ahhe'}],
   'Ṣidunaya':[{ORTH:    'Ṣidunaya'}],
   'Baqar':[{ORTH:    'Baqar'}],
   'Šamaš-belu-uṣur':[{ORTH:    'Šamaš-belu-uṣur'}],
   'Arpaddu':[{ORTH:    'Arpaddu'}],
   'Ullusunu':[{ORTH:    'Ullusunu'}],
   'Hesa':[{ORTH:    'Hesa'}],
   'Nabu-ṣalla':[{ORTH:    'Nabu-ṣalla'}],
   'Yaʾiru':[{ORTH:    'Yaʾiru'}],
   'Sin-iddina':[{ORTH:    'Sin-iddina'}],
   'Sazana':[{ORTH:    'Sazana'}],
   'Ašapi':[{ORTH:    'Ašapi'}],
   'Maniʾ':[{ORTH:    'Maniʾ'}],
   'Aššur-dalal':[{ORTH:    'Aššur-dalal'}],
   'ša-rēšīya':[{ORTH:    'ša-rēšīya'}],
   'ša-rēšāni':[{ORTH:    'ša-rēšāni'}],
   'ša-rēšīšu':[{ORTH:    'ša-rēšīšu'}],
   'ša-rēši':[{ORTH:    'ša-rēši'}],
   'ša-qurbūtu':[{ORTH:    'ša-qurbūtu'}],
   'ša-qurbūti':[{ORTH:    'ša-qurbūti'}],
   'ša-qurbūte':[{ORTH:    'ša-qurbūte'}],
   'ša-bēti-šanie':[{ORTH:    'ša-bēti-šanie'}],
   'šalše-ūme':[{ORTH:    'šalše-ūme'}],
   'šalši-ūme':[{ORTH:    'šalši-ūme'}],
   'šalši-ūmēšu':[{ORTH:    'šalši-ūmēšu'}],
   'ša-muhhi-āli':[{ORTH:    'ša-muhhi-āli'}],
   'ša-muhhi-bēti':[{ORTH:    'ša-muhhi-bēti'}],
   'ša-muhhi-bētāni':[{ORTH:    'ša-muhhi-bētāni'}],
   'ša-pān-ēkalli':[{ORTH:    'ša-pān-ēkalli'}],
   'ša-maṣṣarti':[{ORTH:    'ša-maṣṣarti'}],
   'ša-pēthallāte':[{ORTH:    'ša-pēthallāte'}],
   'ša-pēthallāti':[{ORTH:    'ša-pēthallāti'}],
   'ša-bēti-šaniūte':[{ORTH:    'ša-bēti-šaniūte'}],
   'rab mūgiya':[{ORTH:    'rab mūgiya'}],
   'rab mūgi':[{ORTH:    'rab mūgi'}],
   'rab mūgīka':[{ORTH:    'rab mūgīka'}],
   'rab kiṣrūte':[{ORTH:    'rab kiṣrūte'}],
   'rab kiṣirūte':[{ORTH:    'rab kiṣirūte'}],
   'rab kiṣir':[{ORTH:    'rab kiṣir'}],
   'rab karkadinni':[{ORTH:    'rab karkadinni'}],
   'rab bēti':[{ORTH:    'rab bēti'}],
   'rab bētīya':[{ORTH:    'rab bētīya'}],
   'rab urāte':[{ORTH:    'rab urāte'}],
   'rādi qāti':[{ORTH:    'rādi qāti'}],
   'ṣāb šarri':[{ORTH:    'ṣāb šarri'}],
   'ana mēni':[{ORTH:    'ana mēni'}],
   'ammat šarri':[{ORTH:    'ammat šarri'}],
   'issi ēkalli':[{ORTH:    'issi ēkalli'}],
   'issu maṣin':[{ORTH:    'issu maṣin'}],
   'amat ēkalli':[{ORTH:    'amat ēkalli'}],
   'mar’ē šīmī':[{ORTH:    'mar’ē šīmī'}],
   'kallāp šibirtu':[{ORTH:    'kallāp šibirtu'}],
   'kallāp šibirti':[{ORTH:    'kallāp šibirti'}],
   'rab urāsi':[{ORTH:    'rab urāsi'}],
   'rab urāsāni':[{ORTH:    'rab urāsāni'}],
   'bēt mardīti':[{ORTH:    'bēt mardīti'}],
   'bēt mardītīya':[{ORTH:    'bēt mardītīya'}],
   'bēt rimki':[{ORTH:    'bēt rimki'}],
   'mār kitkittê':[{ORTH:    'mār kitkittê'}],
   'mār šipri':[{ORTH:    'mār šipri'}],
   'mār šiprīya':[{ORTH:    'mār šiprīya'}],
   'mār šīmi':[{ORTH:    'mār šīmi'}],
   'mār damqi':[{ORTH:    'mār damqi'}],
   'mutīr ṭēme':[{ORTH:    'mutīr ṭēme'}],
   '{ 1}x+x':[{ORTH:    '{ 1}x+x'}],
   '{ 1}x':[{ORTH:    '{ 1}x'}],
   '{ d}x':[{ORTH:    '{ d}x'}],
   '{ d}x+x':[{ORTH:    '{ d}x+x'}],
   '{ KUR}x':[{ORTH:    '{ KUR}x'}],
   '{ KUR}x+x':[{ORTH:    '{ KUR}x+x'}],
   '{ URU}x':[{ORTH:    '{ URU}x'}],
   '{ URU}x+x':[{ORTH:    '{ URU}x+x'}],
   '{ 1}{d}x':[{ORTH:    '{ 1}{d}x'}],
   '{ 1}{d}x+x':[{ORTH:    '{ 1}{d}x+x'}],
   '{ LU₂}x':[{ORTH:    '{ LU₂}x'}],
   '{ LU₂}x+x':[{ORTH:    '{ LU₂}x+x'}],
   'x-KAM':[{ORTH:    'x-KAM'}],
   'x-KAM₂':[{ORTH:    'x-KAM₂'}],
   'UD-x-KAM':[{ORTH:    'UD-x-KAM'}],
   'issu mar':[{ORTH:    'issu mar'}],
}


]

TOKENIZER_EXCEPTIONS = update_exc(BASE_EXCEPTIONS, *exclusions)
