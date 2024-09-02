meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL" : "bir şakaya karşılık cevap",
            "SHEESH" : "onaylamamak",
            "CREEPY" : "korkunç",
            "AGGRO" : "agresifleşmek/sinirlenmek",
            }
            
word = input("Anlamadığınız bir kelime yazın: ").upper()

if word in meme_dict.keys():
    print(meme_dict[word])
elif word=="X":
    print(meme_dict.keys(),"kelimelerini biliyorum" )
else:
    print("kelime bulunmamaktadır")
