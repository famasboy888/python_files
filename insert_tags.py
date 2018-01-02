import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from itertools import zip_longest

DIR = os.path.dirname(__file__)
cred = credentials.Certificate(os.path.join(DIR, 'service.json'))
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://zywie-2b7c2.firebaseio.com'
})
rootDB = db.reference()
value = []
d = {}
for i, val in enumerate(value):
    d[i] = val.lower()
rootDB.child('food_exchange_list_tag').set({
  "Fat" : [ "bacon", "butter", "grated coconut", "coconut grated", "coconut cream", "coconut oil", "cream cheese", "margarine", "mayonaise", "whipping cream", "avocado", "peanut buter", "pili nut", "peanut oil", "olive oil" ],
  "Fruit" : [ "apple", "atis fruit", "sugar apple", "custard apple", "balimbing", "averrhoa carambola", "star fruit", "banana", "cashew", "chico", "dalanghita", "citrus reticulata", "tangerine orange", "datil", "duhat", "syzygium cumini", "black plum", "java plum", "durian", "grapes", "guava", "guyabano", "annona muricata", "soursop", "custard apple", "jackfruit", "kamatsile", "kamachile", "pithecellobium dulce", "lansones", "lanzones", "lychee", "mabolo", "velvet apple", "peach bloom", "macopasyzygium samarangense", "mango", "mangosteen", "terap", "marang", "johey oak", "green pedalai", "madang", "tarap", "timadang", "melon", "papaya", "pear", "pineapple", "rambutan", "santol", "lolly", "sayai", "visayan", "wild mangosteen", "siniguelas", "spanish plum", "star apple", "strawberry", "suha", "tamarind", "tiesa", "watermelon", "prunes", "champoy", "raisins", "buko", "coconut water" ],
  "Meat_Low_fat" : [ "beef shank", "lean meat", "tenderloin", "porterhouse steak", "sirloin steak", "centerloin", "carabeef", "carabeef shank", "carabeef meat", "lean pork", "chicken leg", "chicken meat", "chicken breast", "chicken", "blood", "gizzard", "heart", "liver", "lungs", "omassum", "small intestine", "spleen", "tripe", "uterus", "fish", "hasa-hasa", "dalangang bukid", "galunggong", "hito", "sapsap", "tilapya", "dilis", "crabs", "lobster", "octopus", "squid", "shells", "kuhol", "susong pilipit", "paros", "milk fish", "salmon", "tuna", "shrimp" ],
  "Meat_Med_fat" : [ "beef flank", "beef brisket", "beef plate", "beef chuck", "pork", "brain", "karpa", "egg", "chicken wing", "chicken head", "sardines canned", "canned sardines", "tuna sardines", "tuna spread", "corned beef", "ham sausage" ],
  "Milk" : [ "milk", "evaporated milk", "low fat milk", "skimmed milk", "yoghurt" ],
  "Rice" : [ "rice", "lugaw", "porridge", "bibingka", "biko", "casava cake", "espasol", "kalamay", "ube", "kutsinta", "palitaw", "puto", "sapin-sapin", "sapin sapin", "suman", "tikoy", "pan amerikano", "pan de limon", "pan de sal", "whole wheat bread", "sponge cake", "pasensiya", "lady fingers", "mamon tostado", "hopia", "ensaymada", "corn", "bihon", "macaroni", "sotanghon", "spaghetti", "cornstarch", "sago" ],
  "Sugar" : [ "banana chip", "caramel", "bukayo", "champoy", "condesed milk", "honey", "jam", "marshmallow", "maraschino cherr", "pastillas", "tofee candy", "taho", "yema", "halo-halo", "halo halo", "ice candy", "pulvoron", "chocolate", "banana split", "milo", "cocoa", "chocolate" ],
  "Vegetable_A" : [ "acelgas", "chinese cabbage", "alagaw", "premna odorata", "alugbati", "malabar nightshade", "ampalaya", "momordica charantia", "ampalya fruit", "baguio beans", "abitsuelas", "balbalulang", "seaweed", "sea weed", "bamboo shoot", "labong", "banana heart", "puso na saging", "puso ng saging", "banana blossom", "bataw", "lablab purpureus", "hyacinth bean", "cabbage", "repolyo", "camote", "sweet potato leave", "sweet potato", "cauliflower", "celery", "chayote fruit", "chayote", "sayote", "cucumber", "eggplant", "gabi", "taro", "garlic", "kangkong", "water spinach", "river spinach", "water morning glory", "water convolvulus", "chinese spinach", "katuray flower", "corkwood tree flower", "sesbania grandiflora", "katuray", "katurai", "lettuce", "letsugas", "malunggay", "moringa oleifera", "moringa", "mushroom", "mustard leave", "okra", "ladies' finger", "ladies finger", "onion", "sibuyas", "papaya green", "green papaya", "patola", "luffa acutangula", "luffa gourd", "sponge gourd", "bell pepper", "peppper", "green peppper", "petsay", "chinese cabbage", "petchay", "sea weed", "seaweed", "radish", "saluyot", "jute", "sigarilyas", "winged bean", "wing'd bean", "spinanch", "squash", "pumpkin", "cucurbita", "string beans", "sitaw", "pea", "snow pea", "pea pod", "sitsaro", "tsitsaro", "tomato", "upo", "bottle gourd", "white-flowered gourd", "white flowered gourd" ],
  "Vegetable_B" : [ "carrot", "coconut shoot", "ubod", "cowpea", "paayap", "asparagus bean", "black-eyed pea", "kamansi", "seeded breadfruit", "artocarpus camansi", "lima bean", "butter bean", "sieva bean", "madagascar bean", "mungbean", "moong bean", "golden gram", "green gram", "pigeon pea", "kadyos", "singkamas", "mexican turnip" ]
}
)
