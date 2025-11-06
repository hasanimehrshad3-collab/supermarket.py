# var1 ="iliya abdollahi"
# print(len(var1))
# print(type(var1))
# var2 = [1,2,3,4,5,"hello"]
# var2.insert(1, "alireza") 
# print(var2)

# var1 = []
# varinput = input("please inter your name;")
# var1.append(varinput)

# varinput2 = input("please inter your name;")
# var1.append(varinput2)

# varinput3 = input("please inter your name;")
# var1.append(varinput3)

# print(var1)

# varesm = []
# varinput = input("please enter your age")
# varesm.append(varinput)

# varinput2 = input("please enter your age")
# varesm.append(varinput2)

# varinput3 = input("please enter your age")
# varesm.append(varinput3)

# print(varesm)
# var = [1,3,6,[1,2,[25,36,["hoi",98,[25,[58,25,28,[3698,58]]]]]]]
# print(var[3][2][2][2][1][3][1])

# vartest = [1,2,3]
# print (vartest.remove(2))
# print(vartest)

# var_tuple = (10,20)
# print(var_tuple.index(20))
# print(type(var_tuple))
# var_convert_to_list = list(var_tuple)
# print(type(var_convert_to_list))
# var_convert_to_list.append("hi")
# print(var_convert_to_list)
# var_str = "    salaaam  bacheha    "
# print(var_str.strip())

# liste1 = []
# var1 = int(input("enter number"))
# liste1.append(var1)
# var1 = int(input("enter number"))
# liste1.append(var1)
# var1 = int(input("enter number"))
# liste1.append(var1)
# print(liste1)
# max_var = max(liste1)
# print ("adadmax hast {}" .format(max_var))
# min_var = min(liste1)
# print ("adadmin hast {}" .format(min_var))
# sum_var = sum(liste1)
# print ("adadsum hast {}" .format(sum_var))

# inp = input("enter your number")

# if inp in liste1:

#     print("adad dar list hast ")

# else :
#     print("adad ni")



# # project one
# from colorama import Fore ,Style 

# var1 = int( input("enter your number"))
# print(var1)
# if var1>0 :
#     print(Fore.GREEN + "adad mosbat ast")
# elif var1 < 0 :
#     print(Fore.RED +"adad manfi ast")
# else : 
#     print(Fore.YELLOW +"adad sefr ast")

# # project two

# from colorama import Fore ,Style 

# var1 = int (input("enter number"))
# print(var1)

# if var1 % 2 == 0 :
#     print(Fore.GREEN +("adad zoj ast"))
# else:
#         print(Fore.YELLOW +("adad fard ast"))


# project three
# from colorama import Fore ,Style 

# username_asli = "reza.98"
# password_asli = "reza25263565"
# print(username_asli)
# print(password_asli)
# username = input("enter your username")
# password = input("enter your password")

# if username == username_asli and password == password_asli :
#     print( Fore.BLUE +"acces to system")
# else :
#     print( Fore.GREEN +"username or password has wrong")



#  project four 

# from colorama import Fore ,Style 
# list1 = []

# var1 = int(input("enter number"))
# list1.append(var1)

# var2 = int(input("enter number"))
# list1.append(var2)

# var3 = int(input("enter number"))
# list1.append(var3)

# var4 = int(input("enter number"))
# list1.append(var4)

# print(list1)

# if 10<= var1 <=99 :
#    10<= var2 <=99
#    10<= var3 <=99
#    10<= var4 <=99
#    print("adad doroste")
# else : 
#    print("adad tak raghami")


# def_max = max(list1)
# print(  Fore.RED+"adad max hast {}".format(def_max))

# def_min = min(list1)
# print(  Fore.YELLOW+"adad min hast {}".format(def_min))

# def_sum = sum(list1)
# print(  Fore.BLACK+"adad sum hast {}".format(def_sum))

# miangin = def_sum / len(list1)
# print(Fore.CYAN + "miangin adad hast {}" .format(miangin))



# tamrin

# for i in range(1,10) :
#     for j in range(1,10) :
#         print(i*j, end="\t")
# print()


# list_asli = []

# for i in range(5) :
#     var_input = int(input("enter number"))
#     list_asli.append(var_input)
#     print(list_asli)

#     zoj_list = []
#     FARD_list = []

#     for n in list_asli :
#      if n % 2 == 0 :
#         zoj_list.append(n)
#      else :
#         FARD_list.append(n)
         

# print("asli",list_asli)
# print("zoje" , zoj_list)
# print("fard" , FARD_list)
      
# list_asli= []
# for i in range(5) :
#  inp = int(input("enter your number"))
#  list_asli.append(inp)

#  print(list_asli) 
        
# list_zoj = []
# list_fard = []

# for j in list_asli :
#  if j  % 2 == 0 :
#   list_zoj.append(j)
# else :
#  list_fard.append(j)


#  print("asli" , list_asli)
#  print("zoj",list_zoj)
#  print("fard", list_fard)
  
            
# # project2 num1 
# from colorama import Fore ,Style 

# counter = 0
# for i in range(1,101):
#     counter += i
#     print(Fore.GREEN+(counter))

# # # project2 num2
# from colorama import Fore ,Style 
# from datetime import datetime
# timing = datetime.now()
# print(   timing)
# real_pass = "mehrshad0023"

# for i in range(1,4):
#     var_input = input(Fore.RED+("try {}" .format(i)))
#     if real_pass == var_input :
#         print("pass is currect")
#         break
#     else:
#         print(Fore.YELLOW+("wrong pass"))
# else:
#     print(Fore.CYAN+("denied accses"))

# endtiming = datetime.now()
# print(endtiming)

# project2 num3
# from colorama import Fore ,Style

# zoj_list = []
# fard_list = []
# for i in range (1,21):
#     if i % 2 == 0 :
#         zoj_list.append(i)
#     else:
#         fard_list.append(i)
#         print(zoj_list)
#         print(fard_list)

# zoj_sum = sum(zoj_list)
# fard_sum = sum(fard_list)
# print(Fore.GREEN + "adad zoj {}".format(zoj_list))
# print(Fore.GREEN + "sum zoj {}".format(zoj_sum))

# print(Fore.RED + "adad fard{}".format(fard_list))
# print(Fore.RED + "sum fard {}".format(fard_sum))

# project2 num4
# from colorama import Fore ,Style

# currect_pass =input( "please enter code")
# min_len = len(currect_pass) >=8

# _digit = False
# for i in currect_pass :
#     if i.isdigit():
#         _digit = True
#         break
#     _upper = False
#     for i in currect_pass :
#         if i.isupper():
#          _upper= True
#          break


#     if min_len and _digit and _upper :
#           print("password is true")
#     else:
#            print("someting has wrong")
#            break


            
# # project3 number1 
# from random import randint 
# from datetime import datetime
# from colorama import Style, Fore
# print(datetime.now())
# random_num = randint(1,10)
# print(random_num)
# while True:
#     inp_karbar = int(input("enter number"))    
#     if random_num > inp_karbar :
#         print(Fore.RED+"adadet hast {} adad kochektare".format(inp_karbar))
         
#     elif random_num < inp_karbar :
#         print(Fore.GREEN+"adadet hast {} adad bozorgtar".format(inp_karbar))
        
#     else:
#         print(Fore.CYAN+"you win")
#         break


# # project3 number2
# from random import randint 
# from colorama import Fore , init
# init(autoreset=True)
# print(Fore.GREEN+"hi")
# print(Fore.GREEN+"hi")
# print(Fore.RED+"hi")


# list1 = []
# i = 0
# while i < 10 :
#     list1.append(randint(1,50))
#     i+=1
#     print(list1)


#     adad_kochak =list1[0]
#     adad_bzrg =list1[0]
#     j = 0
# while j <len(list1) :
#     if list1[j] < adad_kochak :
#         adad_kochak = list1[j]
#     elif list1[j] > adad_bzrg :
#         adad_bzrg = list1[j]
#         j+=1
# print(Fore.LIGHTGREEN_EX+"adad bozorg"+str(adad_bzrg))
# print(Fore.RED+"adad kochak"+str(adad_kochak))



# project3 num3
# from random import randint 
# from colorama import Fore , init
# tedadtos = 0
# while True :
#     tedadtos+=1
#     adadtos = randint(1,6)
#     print("partabtos{}: adad tos{}".format(tedadtos,adadtos))
#     if adadtos==6:
#         break



# project3 num4
# from random import randint 
# from colorama import Fore , init

# list1=[]
# for i in range(20):
#     list1.append(randint(1,10))

# tekrar = {}
# for j in list1 :
#     if list1.count(j) > 1 :
#         tekrar[j]=list1.count(j)

# print(list1)
# print(tekrar)

# project4 number1
# import random
# from datetime import datetime

# def create_users():
#     return["ali","reza","mmd","javad","hossein"]


# def draw_user(users , history):
#     if not users :
#         print("everyone selected")
#         return None  
#     chosen = random.choice(users)
#     users.remove(chosen)
#     draw_time =datetime.now()

#     history.append((chosen,draw_time))
#     print(f"karbar entekhab shode:{chosen} dar zaman {draw_time}")

# users= create_users()
# histori = []
    

# for i in range(7):
#     draw_user(users,histori)


# print("\n tarikhche ghore keshi :")
# for user, time in histori:
#     print(f"{user} dar zaman {time}")





# import random
# from datetime import datetime

# def list_karbar ():
#     return ["ali" , "mmd","reza","jafar", "zahra"]




# def entekhab_karbar (user , tarikhche):
#     if not user :
#         print("barname tamome")
#         return None
#     chosen = random.choice(user)
#     user.remove(chosen)
#     draw_time = datetime.now()
#     tarikhche.append((chosen,draw_time))
#     print(f"karbaran{chosen},zaman{draw_time}")
#     return chosen


# users = list_karbar()
# history = []

# for i in range(6):
#     entekhab_karbar(users , history)
#     print("\n tarikhche ghore keshi")
# for userr , time in history :
#     print(f"{userr} dar zaman {time}")



from random import randint 
var_test = [randint(1,5)]
print(var_test)
for i in range(3):
        var_shans = int(input("plz enter int"))
        if var_shans==var_test:
            print("you win")
            break
        else:
            print("try again")
            break
        
        