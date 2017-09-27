import time

from interface import combine1 as c


def mainb():
    def quit():
        c.mainc()
###A choice based game where every choice make a difference###
    print("Crypt Walker v1.0\nMade by Fiqhy and Fariz\n########################")
    print("Game is loading...")
    time.sleep(3)
#variables
    ins=("Select a choice:")
    divider="----------------------------------------------"
#####PERSPECTIVE AND INTRODUCTION#####
    def begin():
        print("The year is 1257 AD set in the northern part of Europe,\nwhen knights fight each other for the greed of their king\n",divider),time.sleep(6)
    def char():
        view=input("1.First Person\n2.Third Person\nChoose the perspective:")
###1ST PERSON###
        if view=="1":
            begin(),time.sleep(3)
            self = "yourself"
            pron = "you"
            pos = "yours"
#####CHOICES IN GAME(1ST PERSON)#####
            print(pron, "hear rumors from the local townsfolk of an ancient crypt"
                        "\nburning with treasures worth of a king ransom,"
                        "\nand decide to take a look for", self, ".", "\n", divider), time.sleep(4)
            def fChoice1():
                print("While", pron, "are traveling near the crypt,", "\n" + pron,
                      "come upon several soldiers attacking each other."), time.sleep(4)
                c1a = ("wait for the fight to end and approach the victor")
                c1b = ("pick a side and join the fight")
                print(pron, "decide to...\n1.", c1a, "\n2.", c1b)
                choice1 = input(ins)
                if choice1 == "1":
                    print(pron, "wait then approaches two remaining soldiers.\n", divider), time.sleep(4)
                    Choice2a()
                elif choice1 == "2":
                    print(pron, "survive and there are four soldiers remaining.\n", divider), time.sleep(4)
                    Choice2b()
            def Choice2a():
                print("The two soldiers asked for", pron + "r help to join them.","\n", divider, time.sleep(2),
                      "\nUpon entering the crypt,", pron, "see several weapon wielding"
                      "\nundeads in the distance and a hole underneath the wall near", self + ".")
                c2_aa = ("fight the undeads")
                c2_ab = ("crawl through the hole")
                print(pron, "decide to...\n1.", c2_aa, "\n2.", c2_ab)
                choice2a = input(ins)
                if choice2a == "1":
                    print(pron, "and the two soldiers are unable to managed the undeads\n", divider,
                          "\nFAIL"), time.sleep(5)
                    quit()
                elif choice2a == "2":
                    print(pron, "and the soldiers crawl through the hole\n", divider), time.sleep(5)
                    Choice3a()
            def Choice2b():
                print("The soldiers appreciate", pron + "r help and allow","you to join them.\n", divider,
                    "\nUpon entering the crypt,", pron, "see several weapon wielding"
                    "\nundeads in the distance and a hole near", self + ".")
                c2_ba = ("fight the undeads")
                c2_bb = ("crawl through the hole")
                print(pron, "decide to...\n1.", c2_ba, "\n2.", c2_bb)
                choice2b = input(ins)
                if choice2b == "1":
                    print(pron, "and the soldiers have managed the undeads"), time.sleep(5)
                    Choice4()
                elif choice2b == "2":
                    print(pron, "and the soldiers crawl through the hole\n", divider), time.sleep(5)
                    Choice3b()
            def Choice3a():
                print("After going through the tunnel,", pron, "find", self, "in an antechamber."
                      "\nUp front is a small hallway with two different floor tiling,"
                      "\nand the left tile seems darker than the right one."), "\n",divider, time.sleep(2)
                c3_aa = ("walk through the left tile")
                c3_ab = ("walk through the right tile")
                print(pron, "decide to...\n1.", c3_aa, "\n2.", c3_ab)
                choice3a = input(ins)
                if choice3a == "1":
                    print(pron, "finds out that the floor tile is a pressure plate,"
                                "\nand suddenly the hallway is burning with fire."
                                "\n" + pron, "and the two soldiers are burned alive.","\n", divider), time.sleep(5)
                    quit()
                elif choice3a == "2":
                    print(pron, "finds out that the floor tile is a pressure plate,"
                                "\nand suddenly the antechamber is burning with fire."
                                "\n" + pron, "and the two soldiers pass through the hallway.","\n", divider), time.sleep(5)
                    Choice4()
            def Choice3b():
                print("After going through the tunnel,", pron, "find", self, "in an antechamber."
                "\nUp front is a small hallway with two different floor tiling,"
                "\nand the left tile seems darker than the right one."
                "\nThe hallway is too narrow for all soldiers to go through,"
                "\nso two of them wait in the antechamber"),"\n", divider, time.sleep(2)
                c3_ba = ("walk through the right tile")
                c3_bb = ("walk through the left tile")
                print(pron, "decide to...\n1.", c3_ba, "\n2.", c3_bb)
                choice3b = input(ins)
                if choice3b == "1":
                    print(pron, "find out that the floor tile is a pressure plate,"
                                "\nand suddenly the antechamber is burning with fire."
                                "\nThe two soldiers in the antechamber are burned alive, while"
                                "\n" + pron, "and the other two soldiers pass through the hallway.","\n",divider), time.sleep(5)
                    Choice4()
                elif choice3b == "2":
                    print(pron, "finds out that the floor tile is a pressure plate,"
                                "\nand suddenly the hallway is burning with fire."
                                "\n" + pron, "and two soldiers is burned alive.","\n", divider), time.sleep(5)
                    quit()
            def Choice4():
                print(pron, "enter a large round hall flooded with gold coins around it"
                            "\nand a throne in the center. An ancient corpse sit on the throne,"
                            "\nwith a crown over it's head."), time.sleep(5), \
                            ("\nThe soldiers approach the throne while suddenly, a ghost wielding a sword"
                            "\ncomes out of the corpse and attacked them"),"\n", divider, time.sleep(5)
                c4_a = ("take off the crown from the corpse and break it")
                c4_b = ("put a sword on the corpse's chest while aiming for it's heart")
                print(pron, "quickly decide to...\n1.", c4_a, "\n2.", c4_b)
                choice4 = input(ins)
                if choice4 == "1":
                    print(pron, "finally break the crown,", time.sleep(2),
                          "\nbut it seems nothing is happening.", time.sleep(1),
                          "\nUnfortunately, all the soldiers have been killed"
                          "\nand the ghost is charging at", pron + ".", time.sleep(3),
                          pron, "lie dead on the ground.","\n", divider, "FAIL"), time.sleep(5)
                    quit()
                elif choice4 == "2":
                    print(pron, "finally stab the corpse's heart,", time.sleep(2),
                          "\nin a sudden the ghost charges at", pron + ".", time.sleep(3),
                          "\nThe ghost disappears and all the soldiers have been killed.","\n",
                          divider, "\n","Finally the treasure belongs to", pron, "now.", time.sleep(2),
                          "\n--Congratulation you have won the game--"
                          "\nthank you for playing"), time.sleep(5)
                    quit()
            fChoice1()
###3RD PERSON###
        elif view=="2":
            name=input("Enter the person's name:").title()
            while not name.isalpha():
                print("Name can only contain letters without any spaces")
                name=input("Enter the person's name:").title()
            gender=input("Male=m\nFemale=f\nEnter the person's gender:")
            if gender=="m":
                sel="him"
                self="himself"
                pron="he"
                pos="his"
            elif gender=="f":
                sel="her"
                self="herself"
                pron="she"
                pos="her"
            print("Creating character..."),time.sleep(4)
            begin(),time.sleep(3)
#####CHOICES IN GAME(3RD PERSON)#####
        print(name, "hears rumors from the local townsfolk of an ancient crypt"
                    "\nburning with treasures worth of a king ransom,"
                    "\nand decides to take a look for", self, ".", "\n", divider), time.sleep(6)
        def Choice1():
            print("While",name,"is traveling near the crypt,","\n"+pron,"comes upon several soldiers attacking each other."),time.sleep(4)
            c1a=("wait for the fight to end and approach the victor")
            c1b=("pick a side and join the fight")
            print(name, "decides to...\n1.", c1a, "\n2.", c1b)
            choice1=input(ins)
            if choice1=="1":
                print(name,"waits then approaches two remaining soldiers.\n",divider),time.sleep(4)
                Choice2a()
            elif choice1=="2":
                print(name,"survives and there are four soldiers remaining.\n",divider),time.sleep(4)
                Choice2b()
        def Choice2a():
            print("The two soldiers asked for",name+"'s help to joins them.","\n",divider,time.sleep(2),
                  "\nUpon entering the crypt,",name,"sees several weapon wielding"
                  "\nundeads in the distance and a hole near",self+".")
            c2_aa=("fight the undeads")
            c2_ab=("crawl through the hole")
            print(name, "decides to...\n1.", c2_aa, "\n2.", c2_ab)
            choice2a=input(ins)
            if choice2a=="1":
                print(name,"and the two soldiers are unable to managed the undeads\n",divider,"\nFAIL"),time.sleep(5)
                quit()
            elif choice2a=="2":
                print(name,"and the soldiers crawl through the hole\n",divider),time.sleep(5)
                Choice3a()
        def Choice2b():
            print("The soldiers appreciate",name+"'s help and allow",pos,"to joins them.","\n",divider,time.sleep(2),
                  "\nUpon entering the crypt,",name,"sees several weapon wielding"
                  "\nundeads in the distance and a hole underneath the wall near",self+".")
            c2_ba=("fight the undeads")
            c2_bb=("crawl through the hole")
            print(name, "decides to...\n1.", c2_ba, "\n2.", c2_bb)
            choice2b=input(ins)
            if choice2b=="1":
                print(name,"and the soldiers have managed the undeads"),time.sleep(5)
                Choice4()
            elif choice2b=="2":
                print(name,"and the soldiers crawl through the hole\n",divider),time.sleep(5)
                Choice3b()
        def Choice3a():
            print("After going through the tunnel,",name,"finds",self,"in an antechamber."
                  "\nUp front is a small hallway with two different floor tiling,"
                  "\nand the left tile seems darker than the right one."),"\n",divider,time.sleep(2)
            c3_aa=("walk through the left tile")
            c3_ab=("walk through the right tile")
            print(name, "decides to...\n1.", c3_aa, "\n2.", c3_ab)
            choice3a=input(ins)
            if choice3a=="1":
                print(name,"finds out that the floor tile is a pressure plate,"
                      "\nand suddenly the hallway is burning with fire."
                      "\n"+name,"and the two soldiers are burned alive.","\n",divider),time.sleep(5)
                quit()
            elif choice3a=="2":
                print(name,"finds out that the floor tile is a pressure plate,"
                      "\nand suddenly the antechamber is burning with fire."
                      "\n"+name,"and the two soldiers pass through the hallway.","\n",divider),time.sleep(5)
                Choice4()
        def Choice3b():
            print("After going through the tunnel,",name,"finds",self,"in an antechamber."
                  "\nUp front is a small hallway with two different floor tiling,"
                  "\nand the left tile seems darker than the right one."
                  "\nThe hallway is too narrow for all soldiers to go through,"
                  "\nso two of them wait in the antechamber"),"\n",divider,time.sleep(2)
            c3_ba=("walk through the right tile")
            c3_bb=("walk through the left tile")
            print(name, "decides to...\n1.", c3_ba, "\n2.", c3_bb)
            choice3b=input(ins)
            if choice3b=="1":
                print(name,"finds out that the floor tile is a pressure plate,"
                      "\nand suddenly the antechamber is burning with fire."
                      "\nThe two soldiers in the antechamber are burned alive, while"
                      "\n"+name,"and the other two soldiers pass through the hallway.","\n",divider),time.sleep(5)
                Choice4()
            elif choice3b=="2":
                print(name,"finds out that the floor tile is a pressure plate,"
                      "\nand suddenly the hallway is burning with fire."
                      "\n"+name,"and two soldiers are burned alive.","\n",divider),time.sleep(5)
                quit()
        def Choice4():
            print(name, "enters a large round hall flooded with gold coins around it"
                  "\nand a throne in the center. An ancient corpse sit on the throne,"
                  "\nwith a crown over it's head.",
                  "\nThe soldiers approach the throne while suddenly, a ghost wielding a sword",
                  "\ncomes out of the corpse and attacked them", "\n"),divider, time.sleep(5)
            c4_a = ("take off the crown from the corpse and break it")
            c4_b = ("put a sword on the corpse's chest while aiming for it's heart")
            print(name, "quickly decides to...\n1.", c4_a, "\n2.", c4_b)
            choice4 = input(ins)
            if choice4 == "1":
                print(name, "finally breaks the crown,",time.sleep(2),
                            "\nbut it seems nothing is happening.",time.sleep(1),
                            "\nUnfortunately, the all the soldiers have been killed"
                            "\nand the ghost is charging at",name+".",time.sleep(3),
                            name,"lies dead on the ground.", "\n",divider,"\n","FAIL"), time.sleep(5)
                quit()
            elif choice4 == "2":
                print(name, "finally stabs the corpse's heart,"
                            "\nin a sudden the ghost charges at",name+".","\n",
                            "\nThe ghost disappears and all the soldiers have been killed."
                            ,"\n",divider,"\n","Finally the treasure belongs to",name,"now.","\n",time.sleep(2),
                            "\n--Congratulation you have won the game--"
                            "\nthank you for playing"), time.sleep(5)
                quit()
        Choice1()
    char()
