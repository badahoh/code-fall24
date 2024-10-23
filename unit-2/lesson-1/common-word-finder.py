word_counts = {}
file = "sola.txt"

openfile = open(file)
for line in openfile: 
    for word in line.split(" "): 
        print(word) 
        # if the word is already been seen, increment the count by 1
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else: # if we have not seen the word yet, set the count to 1
            word_counts[word] = 1




print("~~~~~~\n~~~~~\n~~~~~~\n~~~~~~~\n~~~~~~\n~~~~~\n~~~~~~")
for key in word_counts:
        print(key, "--->", word_counts[key])

word_counts["total"] = 0
#adding more into forloop 
#updating value in the dictionary 
for item in word_counts.items():
    # each pair of key and value is an item 
    #each key value is "each"
    print(item) 
    for each in item:
        if(type(each)is list):
            # seeing what type of data each key is in dictionary
            print("this is not a string, but there are",len(each),"items in this list!!")

            for i in each:
                word_counts["total"] = word_counts["total"] + 1
        if (type(each)is str):
            print("there are",len(each),"characters in this string:", each)


# terminal results

# ~~~~~~
# ~~~~~
# ~~~~~~
# ~~~~~~~
# ~~~~~~
# ~~~~~
# ~~~~~~
# Te ---> 1
# conviene ---> 3
# no ---> 11
# decirme ---> 1
# que ---> 3
# me ---> 6
# quieres
#  ---> 1
# Prefiero ---> 1
# te ---> 9
# alejes, ---> 1
# prefiero ---> 1
# dejes ---> 1
# sola
#  ---> 2
# Te ---> 1
# andar ---> 2
# firmando ---> 1
# papeles
#  ---> 1
# Ni ---> 1
# subir ---> 1
# los ---> 1
# decibeles, ---> 1
# cuando ---> 1
# estoy ---> 1
# cerca ---> 1
# de ---> 7
# ti
#  ---> 1
# Yo ---> 5
# soy ---> 6
# el ---> 2
# tipo ---> 6
# mujer ---> 3
# con ---> 2
# quien ---> 2
# tu ---> 3
# mamá ---> 2
# quiere ---> 2
# ver
#  ---> 2
# Me ---> 2
# hacen ---> 5
# falta ---> 1
# tantas ---> 4
# cosas ---> 2
# y ---> 2
# fallan ---> 2
# otras
#  ---> 2
# Nunca ---> 2
# podría ---> 5
# complacer
#  ---> 5
# Ellas ---> 6
# son ---> 9
# fieles. ---> 1
# ellas ---> 3
# santas
#  ---> 3
# buenas, ---> 3
# perdonan ---> 3
# calladas
#  ---> 3
# No ---> 9
# escenas, ---> 3
# piden ---> 3
# nada
#  ---> 3
# ese ---> 4
# mujer
#  ---> 3
# soñando ---> 1
# ilusionada
#  ---> 1
# Si ---> 1
# sirvo ---> 1
# estando ---> 1
# atada
#  ---> 1
# Soy ---> 1
# un ---> 1
# águila ---> 1
# volando ---> 1
# Necesito ---> 1
# desvestirme ---> 1
# perfume
#  ---> 1
# Este ---> 1
# aroma ---> 1
# consume
#  ---> 1
# quiero ---> 1
# confundir
#  ---> 1
# faltas ---> 1
# fieles, ---> 2
# ni ---> 1
# nada ---> 1
# de, ---> 1
# ('\ufeffTe', 1)
# there are 3 characters in this string: ﻿Te
# ('conviene', 3)
# there are 8 characters in this string: conviene
# ('no', 11)
# there are 2 characters in this string: no
# ('decirme', 1)
# there are 7 characters in this string: decirme
# ('que', 3)
# there are 3 characters in this string: que
# ('me', 6)
# there are 2 characters in this string: me
# ('quieres\n', 1)
# there are 8 characters in this string: quieres

# ('Prefiero', 1)
# there are 8 characters in this string: Prefiero
# ('te', 9)
# there are 2 characters in this string: te
# ('alejes,', 1)
# there are 7 characters in this string: alejes,
# ('prefiero', 1)
# there are 8 characters in this string: prefiero
# ('dejes', 1)
# there are 5 characters in this string: dejes
# ('sola\n', 2)
# there are 5 characters in this string: sola

# ('Te', 1)
# there are 2 characters in this string: Te
# ('andar', 2)
# there are 5 characters in this string: andar
# ('firmando', 1)
# there are 8 characters in this string: firmando
# ('papeles\n', 1)
# there are 8 characters in this string: papeles

# ('Ni', 1)
# there are 2 characters in this string: Ni
# ('subir', 1)
# there are 5 characters in this string: subir
# ('los', 1)
# there are 3 characters in this string: los
# ('decibeles,', 1)
# there are 10 characters in this string: decibeles,
# ('cuando', 1)
# there are 6 characters in this string: cuando
# ('estoy', 1)
# there are 5 characters in this string: estoy
# ('cerca', 1)
# there are 5 characters in this string: cerca
# ('de', 7)
# there are 2 characters in this string: de
# ('ti\n', 1)
# there are 3 characters in this string: ti

# ('Yo', 5)
# there are 2 characters in this string: Yo
# ('soy', 6)
# there are 3 characters in this string: soy
# ('el', 2)
# there are 2 characters in this string: el
# ('tipo', 6)
# there are 4 characters in this string: tipo
# ('mujer', 3)
# there are 5 characters in this string: mujer
# ('con', 2)
# there are 3 characters in this string: con
# ('quien', 2)
# there are 5 characters in this string: quien
# ('tu', 3)
# there are 2 characters in this string: tu
# ('mamá', 2)
# there are 4 characters in this string: mamá
# ('quiere', 2)
# there are 6 characters in this string: quiere
# ('ver\n', 2)
# there are 4 characters in this string: ver

# ('Me', 2)
# there are 2 characters in this string: Me
# ('hacen', 5)
# there are 5 characters in this string: hacen
# ('falta', 1)
# there are 5 characters in this string: falta
# ('tantas', 4)
# there are 6 characters in this string: tantas
# ('cosas', 2)
# there are 5 characters in this string: cosas
# ('y', 2)
# there are 1 characters in this string: y
# ('fallan', 2)
# there are 6 characters in this string: fallan
# ('otras\n', 2)
# there are 6 characters in this string: otras

# ('Nunca', 2)
# there are 5 characters in this string: Nunca
# ('podría', 5)
# there are 6 characters in this string: podría
# ('complacer\n', 5)
# there are 10 characters in this string: complacer

# ('Ellas', 6)
# there are 5 characters in this string: Ellas
# ('son', 9)
# there are 3 characters in this string: son
# ('fieles.', 1)
# there are 7 characters in this string: fieles.
# ('ellas', 3)
# there are 5 characters in this string: ellas
# ('santas\n', 3)
# there are 7 characters in this string: santas

# ('buenas,', 3)
# there are 7 characters in this string: buenas,
# ('perdonan', 3)
# there are 8 characters in this string: perdonan
# ('calladas\n', 3)
# there are 9 characters in this string: calladas

# ('No', 9)
# there are 2 characters in this string: No
# ('escenas,', 3)
# there are 8 characters in this string: escenas,
# ('piden', 3)
# there are 5 characters in this string: piden
# ('nada\n', 3)
# there are 5 characters in this string: nada

# ('ese', 4)
# there are 3 characters in this string: ese
# ('mujer\n', 3)
# there are 6 characters in this string: mujer

# ('soñando', 1)
# there are 7 characters in this string: soñando
# ('ilusionada\n', 1)
# there are 11 characters in this string: ilusionada

# ('Si', 1)
# there are 2 characters in this string: Si
# ('sirvo', 1)
# there are 5 characters in this string: sirvo
# ('estando', 1)
# there are 7 characters in this string: estando
# ('atada\n', 1)
# there are 6 characters in this string: atada

# ('Soy', 1)
# there are 3 characters in this string: Soy
# ('un', 1)
# there are 2 characters in this string: un
# ('águila', 1)
# there are 6 characters in this string: águila
# ('volando', 1)
# there are 7 characters in this string: volando
# ('Necesito', 1)
# there are 8 characters in this string: Necesito
# ('desvestirme', 1)
# there are 11 characters in this string: desvestirme
# ('perfume\n', 1)
# there are 8 characters in this string: perfume

# ('Este', 1)
# there are 4 characters in this string: Este
# ('aroma', 1)
# there are 5 characters in this string: aroma
# ('consume\n', 1)
# there are 8 characters in this string: consume

# ('quiero', 1)
# there are 6 characters in this string: quiero
# ('confundir\n', 1)
# there are 10 characters in this string: confundir

# ('faltas', 1)
# there are 6 characters in this string: faltas
# ('fieles,', 2)
# there are 7 characters in this string: fieles,
# ('ni', 1)
# there are 2 characters in this string: ni
# ('nada', 1)
# there are 4 characters in this string: nada
# ('de,', 1)
# there are 3 characters in this string: de,
# ('total', 0)
# there are 5 characters in this string: total
# badaoh@Badas-MBP unit-2 % 