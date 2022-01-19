from time import sleep
import os
import random


list_ing = []
ing = ""
q = ""
y = 0
ll = 0
jia = 10
jixian = 100
gongfa1 = 0
gongfa2 = 0
gongfa3 = 0
bc_list = []
names = []
passws = []
gongji = 10
wuji1 = 0
wuji2 = 0
wuji3 = 0
lingqi1 = "11"
lingqi2 = "11"
lingqi3 = "11"
jgongfa1 = 0
jgongfa2 = 0
jgongfa3 = 0
lingqi = 0
location = "house"
jgongfa1 = 0
maxgongfa1 = 0
lvgongfa1 = 0

def eval1():
  global jgongfa1
  global maxgongfa1
  global lvgongfa1
  global jia
  if jgongfa1 < 201:
    if jgongfa1 < 101:
      lvgongfa1 = 1
      maxgongfa1 = 100
    else:
      lvgongfa1 = 2
      maxgongfa1 = 200
  elif jgongfa1 < 301:
    lvgongfa1 = 3
    maxgongfa1 = 300
  elif jgongfa1 < 401: 
    lvgongfa1 = 4
    maxgongfa1 = 400
  elif jgongfa1 < 501:
    lvgongfa1 = 5
    maxgongfa1 = 500
  else:
    lvgongfa1 = 5
    maxgongfa1 = 500
    jgongfa1 = 500

  if jixian == 100:
    jia = 10+(lvgongfa1*10)
  elif jixian == 500:
    jia = 30+(lvgongfa1*10)
  elif jixian == 2500:
    jia = 130+(lvgongfa1*10)
  elif jixian == 12500:
    jia = 630+(lvgongfa1*10)


def clear():
  os.system("clear")
  print("______________________________________")

def baocun():
  f3 = open("data.txt", "r")
  mes = 0
  for x in f3:
    mes += 1
  f3.close()
  f4 = open("data.txt", "r")
  f5 = list(f4.read())
  dictio = []
  it = 0
  for x in range(0, mes):
    scode = ""
    while f5[it] != "#":
      scode = scode + f5[it]
      it += 1
    dictio.append(scode)
    it += 2
  f4.close()

  bc_list = []
  bc_list.append(name)
  bc_list.append("/"+passw)
  bc_list.append("/"+str(ll))
  bc_list.append("/"+str(jia))
  bc_list.append("/"+str(gongfa1))
  bc_list.append("/"+str(gongfa2))
  bc_list.append("/"+str(jixian))
  bc_list.append("/"+str(gongfa3))
  bc_list.append("/"+str(gongji))
  bc_list.append("/"+str(wuji1))
  bc_list.append("/"+str(wuji2))
  bc_list.append("/"+str(wuji3))
  bc_list.append("/"+str(lingqi1))
  bc_list.append("/"+str(lingqi2))
  bc_list.append("/"+str(lingqi3))
  bc_list.append("/"+str(lingqi))
  bc_list.append("/"+str(location))
  bc_list.append("/"+str(jgongfa1))
  bc_list.append("/"+str(jgongfa2))
  bc_list.append("/"+str(jgongfa3))
  bc_list.append("/")
  bc_str = "".join(bc_list)
  dictio.append(bc_str)
  for x in range(0, len(dictio)):
    dictio[x] = dictio[x]+"#"
  for x in range(1, len(dictio)):
    dictio[x] = "\n"+dictio[x]
  dictio_str = "".join(dictio)
  f8 = open("data.txt", "w")
  f8.write(dictio_str)
  f8.close()


def dazuo(t):
  global ll
  global q
  global jgongfa1
  eval1()
  clear()
  sleep(0.5)
  for y in range(1,t):
    for v in range(0, 4):
      clear()
      list_ing = []
      for x in range(0, v+1):
        list_ing.append("*")
      ing = "".join(list_ing)
      print("\n[xiulianzhong] :{}".format(ing))
      sleep(0.5)
  sleep(0.5)
  clear()
  eval1()
  if t == 4:
    if location == "house":
      print("\n[lingli]+{}".format(jia))
      ll += jia
      jgongfa1 += 20
    elif location == "forest":
      print("\n[lingli]+{}".format(jia*2))
      ll += jia*2
      jgongfa1 += 40
  elif t == 10:
    if location == "house":
      print("\n[lingli]+{}".format(jia*2))
      ll += jia*2
      jgongfa1 += 40
    elif location == "forest":
      print("\n[lingli]+{}".format(jia*4))
      ll += jia*4
      jgongfa1 += 60
  if jgongfa1 > 500:
    jgongfa1 = 500
    clear()
    print("\n[Gongfa1 already max level !]")
  else:
    if t == 4:
      if location == "house":
        print("[Gongfa1 Exp+20]")
      elif location == "forest":
        print("[Gongfa1 Exp+40]")
    elif t == 10:
      if location == "house":
        print("[[Gongfa1 Exp+40]")
      elif location == "forest":
        print("[Gongfa1 Exp+60]")

  sleep(3)

clear()
sleep(2)
print("\nWord_XiuXian")
sleep(3)
clear()
sleep(0.5)
print("\nby HY_Black_Hole")
sleep(3)
clear()
sleep(2)

print("\n\n\n\n[Jiazaizhong] :          |")
sleep(1)

for v in range(0, 10):
  clear()
  list_ing = []
  for x in range(0, v+1):
    list_ing.append("*")
    num = x
  for x in range(0, 9-num):
    list_ing.append(" ")
  list_ing.append("|")
  ing = "".join(list_ing)
  print("\n\n\n\n[Jiazaizhong] :{}".format(ing))
  n = random.randint(0, 1)
  if list_ing[9] != "*":
    sleep(n)
sleep(3)
clear()
sleep(1)


clear()
print("\nHello !\nWelcome to \"Word_XiuXian\" !")
sleep(4)
clear()
sleep(0.5)
a = 0
while a != "s" and a != "l":
  clear()
  print("\n[Sign up][s]\n[Log in][l]")
  a = input("\n>>> ")

if a == "s":
  f3 = open("data.txt", "r")
  mes = 0
  for x in f3:
    mes += 1
  f3.close()
  f4 = open("data.txt", "r")
  f5 = list(f4.read())
  dictio = []
  it = 0
  for x in range(0, mes):
    scode = ""
    while f5[it] != "#":
      scode = scode + f5[it]
      it += 1
    dictio.append(scode)
    it += 2

  for x in range(0, len(dictio)):
    decode1 = dictio[x]
    decode2 = ""
    it2 = 0
    while decode1[it2] != "/":
      decode2 = decode2+decode1[it2]
      it2 += 1
    names.append(decode2)
    it2 += 1
    decode2 = ""
    while decode1[it2] != "/":
      decode2 = decode2+decode1[it2]
      it2 += 1
    passws.append(decode2)
  f4.close()
  ok = 0
  while ok != 1:
    clear()
    q = input("\n1.What's your name ?\n\n>>> ")
    sleep(0.5)
    if q not in names:
      if ("/" in q) or ("#" in q):
        clear()
        print("\nName can't contain / or # !")
        sleep(2)
      else:
        if q == "" or q == " ":
          clear()
          print("Name can't be empty !")
          sleep(2)
        else:
          ok = 1
          name = q
    else:
      clear()
      print("\nName already existing !")
      sleep(2)
  while ok != 2:
    clear()
    q = input("\n2.Create a password : ")
    sleep(0.5)
    if ("/" in q) or ("#" in q):
      clear()
      print("\nPassword can't contain / or # !")
      sleep(2)
    else:
      if q == "" or q ==  "" :
        clear()
        print("Password can't be empty !")
        sleep(2)
      else:
        ok = 2
        passw = q
  sleep(0.5)
  clear()
  print("\nInitialising...")
  sleep(4)

elif a == "l":
  f3 = open("data.txt", "r")
  mes = 0
  for x in f3:
    mes += 1
  f3.close()
  f4 = open("data.txt", "r")
  f5 = list(f4.read())
  dictio = []
  it = 0
  for x in range(0, mes):
    scode = ""
    while f5[it] != "#":
      scode = scode + f5[it]
      it += 1
    dictio.append(scode)
    it += 2

  for x in range(0, len(dictio)):
    decode1 = dictio[x]
    decode2 = ""
    it2 = 0
    while decode1[it2] != "/":
      decode2 = decode2+decode1[it2]
      it2 += 1
    names.append(decode2)
    it2 += 1
    decode2 = ""
    while decode1[it2] != "/":
      decode2 = decode2+decode1[it2]
      it2 += 1
    passws.append(decode2)
  f4.close()
  ok = 0
  while ok != 2:
    ok = 0
    while ok != 1:
      clear()
      q = input("\n1.What's your name ?\n\n>>> ")
      sleep(0.5)
      if q in names:
        ok = 1
        p2 = names.index(q)
      else:
        clear()
        print("\nName Unexisting !")
        sleep(2)
    while ok != 2:
      clear()
      q = input("\n2.Enter your password : ")
      if q == passws[p2]:
        ok = 2
      else:
        clear()
        print("\nIncorrect Password !")
        sleep(2)
  clear()
  print("\nLoging...")
  sleep(2)
  data = []
  decode1 = dictio[p2]
  it2 = 0
  for x in range(0,20):
    decode2 = ""
    while decode1[it2] != "/":
      decode2 = decode2+decode1[it2]
      it2 += 1
    data.append(decode2)
    it2 += 1
  name = data[0]
  passw = data[1]
  ll = int(data[2])
  jia = int(data[3])
  gongfa1 = int(data[4])
  gongfa2 = int(data[5])
  jixian = int(data[6])
  gongfa3 = int(data[7])
  gongji = int(data[8])
  wuji1 = int(data[9])
  wuji2 = int(data[10])
  wuji3 = int(data[11])
  lingqi1 = int(data[12])
  lingqi2 = int(data[13])
  lingqi3 = int(data[14])
  lingqi = int(data[15])
  location = data[16]
  jgongfa1 = int(data[17])
  jgongfa2 = int(data[18])
  jgongfa3 = int(data[19])


  f3 = open("data.txt", "r")
  mes = 0
  for x in f3:
    mes += 1
  f3.close()
  f4 = open("data.txt", "r")
  f5 = list(f4.read())
  dictio = []
  it = 0
  for x in range(0, mes):
    scode = ""
    while f5[it] != "#":
      scode = scode + f5[it]
      it += 1
    dictio.append(scode)
    it += 2
  f4.close()
  f8 = open("data.txt", "w")
  print(dictio)
  dictio.pop(p2)
  for x in range(0, len(dictio)):
    dictio[x] = dictio[x]+"#"
  for x in range(1, len(dictio)):
    dictio[x] = "\n"+dictio[x]
  dictio_str = "".join(dictio)
  f8.write(dictio_str)
  f8.close()








q = ""
while True:
  if ll > jixian:
    clear()
    print("\nTupola !")
    sleep(3)
    if jixian == 100:
      print("\nJingjie : zhujiqi")
      jixian = 500
      gongji += 30
    elif jixian == 500:
      print("\nJingjie : jindanqi")
      jixian = 2500
      gongji += 50
    elif jixian == 2500:
      print("\nJingjie : yuanyingqi")
      jixian = 12500
      gongji += 100
    elif jixian == 12500:
      clear()
      print("\nJingjie : Xian")
      print("\nYou win the game !")
      print("See you next time !")
      break
  if q == "":
    clear()
    print("\nName: {}".format(name)+"\nLingli : {}/{}".format(ll, jixian)+"\nGongji: {}".format(gongji))
    if jixian == 100:
      if ll == 0:
        print("Jingjie : wu")
        print("Huizhang : wu")
      else:
        print("Jingjie: lianqiqi")
        print("Huizhang : |*|")
    elif jixian == 500:
      print("Jingjie : zhujiqi")
      print("Huizhang : [#]")
    elif jixian == 2500:
      print("Jingjie : jindanqi")
      print("Huizhang : {∆}")
    elif jixian == 12500:
      print("Jingjie : yuanyingqi")
      print("Huizhang : (◊)")


  if location == "house":
    if q == "":
      print("\n[xiulian][x]\n[shangdian][s]\n[gongfa][g]\n[wuji][w]\n[lingqi][l]\n[ditu][d]\n[baocun][b]\n")
      q = input(">>> ")
  elif location == "forest":
    if q == "":
      print("\n[xiulian][x]\n[maoxian][m]\n[gongfa][g]\n[wuji][w]\n[lingqi][l]\n[ditu][d]\n[baocun][b]\n")
      q = input(">>> ")

  if location == "house":
    if q == "s":
      clear()
      print("\n[gongfa][g]")
      print("[wuji][w]")
      print("[lingqi][l]")
      print("[tuichu][t]")
      q = input("\n>>> ")
      if q == "t":
        q = ""
        continue
      elif q == "g":
        clear()
        s = 0
        print("\n[gongfa1][jiage30lingli][g1]")
        print("[gongfa2][jiage100lingli][g2]")
        print("[gongfa3][jiage500lingli][g3]")
        print("[tuichu][t]")
        q = input("\n>>> ")
        if q == "g1":
          if ll > 29:
            if gongfa1 < 10:
              ll -= 30
              jgongfa1 += 30
              clear()
              print("\nYou buy it succesfully !")
              print("\n[gongfa1][+1][Exp+30]")
              sleep(2)
              q = "s"
              continue
            else:
              clear()
              print("\nLevel max !")
              sleep(2)
              q = "s"
              continue
          else:
            clear()
            print("\nNot enough lingli !")
            sleep(2)
          q = "s"
          continue
        elif q == "g2":
          if jixian < 101:
            clear()
            print("\nYou have to be at least at zhujiqi !")
            sleep(3)
            q = "s"
            continue
          else:
            if ll > 99:
              if gongfa2 < 10:
                jia += 20
                ll -= 100
                clear()
                gongfa2 += 1
                print("\nYou buy it succesfully !")
                print("\n[gongfa2][lvl:{}]".format(gongfa2))
                sleep(2)
                q = "s"
                continue
              else:
                clear()
                print("\nLevel max !")
                q = "s"
                continue
            else:
              clear()
              print("\nNot enough lingli !")
              sleep(2)
            q = "s"
            continue
        elif q == "g3":
          if jixian < 501:
            clear()
            print("\nYou have to be at least at jindanqi !")
            sleep(3)
            q = "s"
            continue
          else:
            if ll > 499:
              if gongfa3 < 10:
                jia += 100
                ll -= 500
                clear()
                gongfa3 += 1
                print("\nYou buy it succesfully !")
                print("\n[gongfa3][lvl:{}]".format(gongfa3))
                sleep(2)
                q = "s"
                continue
              else:
                clear()
                print("\nLevel max !")
                sleep(2)
                q = "s"
                continue
            else:
              clear()
              print("\nNot enough lingli !")
              sleep(2)
            q = "s"
            continue
        else:
          q = "s"
          continue
      elif q == "w":
        s = 0
        clear()
        print("\n[wuji1][gongji+10][jiage50lingli][w1]")
        print("[wuji2][gongji+30][jiage150lingli][w2]")
        print("[wuji3][gongji+50][jiage250lingli][w3]")
        print("[tuichu][t]")
        q = input("\n>>> ")
        if q == "w1":
          if ll > 49:
            if wuji1 < 4:
              jia += 10
              ll -= 50
              wuji1 += 1
              clear()
              print("\nYou buy it succesfully !")
              print("\n[wuji1][lvl:{}]".format(wuji1))
              sleep(2)
              q = "s"
              continue
            else:
              clear()
              print("\nLevel max !")
              sleep(2)
              q = "s"
              continue
          else:
            clear()
            print("\nNot enough lingli !")
            sleep(2)
          q = "s"
          continue
        elif q == "w2":
          if jixian < 101:
            clear()
            print("\nYou have to be at least at zhujiqi !")
            sleep(3)
            q = "s"
            continue
          else:
            if ll > 149:
              if wuji2 < 4:
                jia += 30
                ll -= 150
                wuji2 += 1
                clear()
                print("\nYou buy it succesfully !")
                print("\n[wuji2][lvl:{}]".format(wuji2))
                sleep(2)
                q = "s"
                continue
              else:
                clear()
                print("\nLevel max !")
                q = "s"
                continue
            else:
              clear()
              print("\nNot enough lingli !")
              sleep(2)
            q = "s"
            continue
        elif q == "w3":
          if jixian < 501:
            clear()
            print("\nYou have to be at least at jindanqi !")
            sleep(3)
            q = "s"
            continue
          else:
            if ll > 249:
              if wuji3 < 4:
                jia += 50
                ll -= 250
                wuji3 += 1
                clear()
                print("\nYou buy it succesfully !")
                print("\n[wuji3][lvl:{}]".format(wuji3))
                sleep(2)
                q = "s"
                continue
              else:
                clear()
                print("\nLevel max !")
                sleep(2)
                q = "s"
                continue
            else:
              clear()
              print("\nNot enough lingli !")
              sleep(2)
            q = "s"
            continue
        else:
          q = "s"
          continue

      elif q == "l":
        s = 0
        clear()
        print("\n[lingqi1][gongji+50][jiage500lingli][l1]")
        print("[lingqi2][gongji+50][jiage500lingli][l2]")
        print("[lingqi3][gongji+100][jiage1200lingli][l3]")
        print("[tuichu][t]")
        q = input("\n>>> ")
        if q == "l1":
          if jixian < 101:
            clear()
            print("\nYou have to be at least at zhujiqi !")
            sleep(3)
            q = "s"
            continue
          else:
            if ll > 49:
              if wuji1 != "":
                gongji += 50
                ll -= 500
                clear()
                print("\nYou buy it succesfully !")
                sleep(2)
                lingqi1 = 0
                q = "s"
                continue
              else:
                clear()
                print("\nAlready purchased !")
                sleep(2)
                q = "s"
                continue
            else:
              clear()
              print("\nNot enough lingli !")
              sleep(2)
            q = "s"
            continue
        elif q == "l2":
          if jixian < 501:
            clear()
            print("\nYou have to be at least at jindanqi !")
            sleep(3)
            q = "s"
            continue
          else:
            if ll > 149:
              if wuji2 != "":
                gongji += 50
                ll -= 500
                clear()
                print("\nYou buy it succesfully !")
                sleep(2)
                lingqi = 0
                q = "s"
                continue
              else:
                clear()
                print("\nAlready purchased !")
                q = "s"
                continue
            else:
              clear()
              print("\nNot enough lingli !")
              sleep(2)
            q = "s"
            continue
        elif q == "l3":
          if jixian < 2501:
            clear()
            print("\nYou have to be at least at yuanyingqi !")
            sleep(3)
            q = "s"
            continue
          else:
            if ll > 249:
              if wuji3 != "":
                gongji += 100
                ll -= 1200
                clear()
                print("\nYou buy it succesfully !")
                sleep(2)
                lingqi = 0
                q = "s"
                continue
              else:
                clear()
                print("\nAlready purchased !")
                sleep(2)
                q = "s"
                continue
            else:
              clear()
              print("\nNot enough lingli !")
              sleep(2)
            q = "s"
            continue
        else:
          q = "s"
          continue

  if location == "forest":
    if q == "m":
      clear()
      print("\n(in progress)\n[tuichu][t]")
      q = input("\n>>> ")
      if q == "t":
        q = ""
        continue
      else:
        q = "m"
        continue

  if q == "x":
    clear()
    print("\n[dazuo][10s][d]\n[biguan][20s][b]\n[tuichu][t]")
    q = input("\n>>> ")
    if q == "t":
      q = ""
      continue
    elif q == "d":
      dazuo(4)
      q = ""
      continue
    elif q == "b":
      dazuo(10)
      q = ""
      continue
    else:
      q = "x"
      continue


  elif q == "g":
    clear()
    print("\nJia : +{}".format(jia))
    eval1()
    print("\n[gongfa1][Exp:{}/{}][Lvl:{}]".format(jgongfa1, maxgongfa1, lvgongfa1))
    print("[gongfa2][lvl:{}]".format(gongfa2, gongfa2*20))
    print("[gongfa3][lvl:{}]".format(gongfa3, gongfa3*100))
    print("\n[tuichu][t]")
    q = input("\n>>> ")
    if q == "t":
      q = ""
      continue
    else:
      q = "g"
      continue
      

  elif q == "w":
    clear()
    print("\n[wuji1][lvl:{}][+{}]".format(wuji1, wuji1*10))
    print("[wuji2][lvl:{}][+{}]".format(wuji2, wuji2*30))
    print("[wuji3][lvl:{}][+{}]".format(wuji3, wuji3*50))
    print("\n[tuichu][t]")
    q = input("\n>>> ")
    if q == "t":
      q = ""
      continue
    else:
      q = "w"
      continue


  elif q == "l":
    clear()
    if lingqi == 0:
      print("\nLingqi selected : None")
    else:
      print("\nLingqi selected : lingqi{}".format(lingqi))
    if lingqi1 == 0:
      if lingqi == 1:
        print("\n[lingqi1][gongji+50][purchased]\n[selected]")
      else:
        print("\n[lingqi1][gongji+50][purchased]\n[not selected][l1]")
    else:
      print("\n[lingqi1][gongji+50][not purchased]")
    if lingqi2 == 0:
      if lingqi == 2:
        print("\n[lingqi2][gongji+50][purchased]\n[selected]")
      else:
        print("\n[lingqi2][gongji+50][purchased]\n[not selected][l2]")
    else:
      print("\n[lingqi2][gongji+50][not purchased]")
    if lingqi3 == 0:
      if lingqi == 3:
        print("\n[lingqi3][gongji+100][purchased]\n[selected]")
      else:
        print("\n[lingqi3][gongji+100][purchased]\n[not selected][l3]")
    else:
      print("\n[lingqi3][gongji+100][not purchased]")
    print("\n[tuichu][t]")
    q = input("\n>>> ")
    if q == "t":
      q = ""
      continue
    elif q == "l1":
      if lingqi1 == "11":
        clear()
        print("\nLingqi1 not purchased !")
        sleep(2)
        q = "l"
        continue
      else:
        if lingqi == 1:
          clear()
          print("\nLingqi1 already selected !")
          sleep(2)
          q = "l"
          continue
        else:
          clear()
          print("\nLingqi1 now selected !")
          lingqi = 1
          sleep(2)
          q = "l"
          continue
    elif q == "l2":
      if lingqi2 == "11":
        clear()
        print("\nLingqi2 not purchased !")
        sleep(2)
        q = "l"
        continue
      else:
        if lingqi == 2:
          clear()
          print("\nLingqi2 already selected !")
          sleep(2)
          q = "l"
          continue
        else:
          clear()
          print("\nLingqi2 now selected !")
          lingqi = 2
          sleep(2)
          q = "l"
          continue
    elif q == "l3":
      if lingqi3 == "11":
        clear()
        print("\nLingqi3 not purchased !")
        sleep(2)
        q = "l"
        continue
      else:
        if lingqi == 3:
          clear()
          print("\nLingqi3 already selected !")
          sleep(2)
          q = "l"
          continue
        else:
          clear()
          print("\nLingqi3 now selected !")
          lingqi = 3
          sleep(2)
          q = "l"
          continue
    else:
      q = "l"
      continue


  elif q == "d":
    clear()
    print("Location : {}".format(location))
    print("Go to :")
    print("[House][h]")
    print("[Forest][min zhujiqi][f]")
    print("[Mystery Mountain][not accessible]")
    print("[tuichu][t]")
    q = input("\n>>> ")
    if q == "t":
      q = ""
      continue
    elif q == "h":
      if location == "house":
        clear()
        print("\nAlready at house !")
        sleep(2)
        q = "d"
        continue
      else:
        clear()
        sleep(0.5)
        for y in range(1,4):
          for v in range(0, 4):
            clear()
            list_ing = []
            for x in range(0, v+1):
              list_ing.append("*")
            ing = "".join(list_ing)
            print("\n[Bashezhong] :{}".format(ing))
            sleep(0.5)
        sleep(0.5)
        clear()
        print("\nLocation : house")
        location = "house"
        sleep(2)
        q = ""
        continue
    elif q == "f":
      if jixian < 101:
        clear()
        print("\nYou have to be at least at zhujiqi !")
        sleep(3)
        q = "d"
        continue
      else:
        if jixian < 101:
          if location == "forest":
            clear()
            print("\nAlready at forest !")
            sleep(2)
            q = "d"
            continue
          else:
            clear()
            sleep(0.5)
            for y in range(1,4):
              for v in range(0, 4):
                clear()
                list_ing = []
                for x in range(0, v+1):
                  list_ing.append("*")
                ing = "".join(list_ing)
                print("\n[Bashezhong] :{}".format(ing))
                sleep(0.5)
            sleep(0.5)
            clear()
            print("\nLocation : forest")
            location = "forest"
            sleep(2)
            q = ""
            continue
        else:
          clear()
          print("")
    else:
      q = "d"
      continue

  elif q == "b":
    clear()
    baocun()
    clear()
    sleep(0.5)
    for y in range(1,4):
      for v in range(0, 4):
        clear()
        list_ing = []
        for x in range(0, v+1):
          list_ing.append("*")
        ing = "".join(list_ing)
        print("\n[baocunzhong] :{}".format(ing))
        sleep(0.5)
    sleep(0.5)
    clear()
    print("\nBaocun sucessfully !\n\nSee you next time !\n")
    break

  else:
    if location == "house" and q != "s":
      q = ""
      continue
    elif location == "forest" and q != "m":
      q = ""
      continue

