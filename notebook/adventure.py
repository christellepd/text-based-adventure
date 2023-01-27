####Quest Adventure Project####
###Task:
#the ‘world’ should consist of at least four “rooms” (clearing, tower, forest etc.)
#every room has a description
#you enter the room to which you want to go on the keyboard
#when you find “the medal”, the game ends with a final message

    
#other ideas:
    #change fonts or something to distinguish questions from answers from statements,add complexities, aesthetics-header design, success design

    
########## DICTIONARIES
node={
"validate":"Oops, you entered the wrong key. Try again.", 
      
"Friedrichshain_desc":"is young, punk, industrial, and full of history.", 
      
"Kreuzberg_desc":"seems to breed bars here, as well as restaurants offering more exotic fares than schnitzel.",
    
    
    "pause":{
        "pause_validate":"Select [B] or [L]",
        
        "pause_text":"While walking, you decide to take a pause and either have a [B]eer or [L]unch. What do you fancy?",
    
        "pause_Beer_K":"Beer is always a good idea! \n\t...You had a bit too much fun and now you're late for your appointment. Good thing the landlord allows you to reschedule. Try again tomorrow.",

        "pause_Lunch_K":"Perfect! Food gets us energized. \n\t...You are now ready to move forward.",
    
        "pause_Lunch_C":"Delicious! \n\t...Your order is delayed and now you're late for your appointment. Good thing the landlord allows you to reschedule. Try again tomorrow.",
    
        "pause_Beer_C":"Beer is always a good idea and you finished your last gulp just in time! \n\t...Ready to move forward."},
    
    
    "transportation":{
        "transportation_validate":"Select [T] or [B]",
        
        "transportation_text":"To get to Mitte, which mode of transportation do you want to take? [T]rain or [B]us",
        
        "transportation_Train_K":"Train is on time. \n\t...You made it to Mitte!",
        
        "transportation_Bus_K":"En route, the tires blow up! \n\t...You missed you appointment. Good thing the landlord allows you to reschedule. Try again tomorrow.",
    
        "transportation_Bus_C":"Bus is on time. \n\t...You made it to Mitte!",
    
        "transportation_Train_C":"There is a railroad maintenance. \n\t...You missed you appointment. Good thing the landlord allows you to reschedule. Try again tomorrow."},
      
    
"Charlottenburg_desc":"is ideal for upscale families and it also has some of the best restaurants in the city."
}




    
    
    
    



########## INTRO

print("\n\n\033[1m"+"\033[1;33m"+"THE CRAZY APARTMENT HUNT\n"+"\033[0m"+"\033[0m")

print("\033[1;33m"+"*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"+"\033[0m")

print("""
You are new in Berlin and are looking for a place to live. You found a listing in Mitte, applied to rent, and the landlord chooses you as a tenant! But there's one last thing

    ...you need to sign the Rental Contract.
    
        ... ... ...

You got your signing appointment with you landlord and you now need to figure out which route will lead you to your destination and arrive on time.

There are various ways to get to Mitte. Are you ready?
""")

print("\033[1;33m"+"*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"+"\033[0m")

input()


########## COUNTDOWN
import time

print("""
Your journey begins in...
""")
for i in range(5,0,-1):
    time.sleep(1)
    print(f'\n{i}')





########## ENTER USER DATA
#ask player name
name=input("\033[1;34m\nWhat is your name? \033[0m").capitalize()
intro=("welcome to Berlin! Your're gonna love it!\n")

print(f"\nHi {name}, {intro}")


#ask player current location
location=input("\033[1;34m\nEnter your location: \033[0m").capitalize()


#set up district list
district=['Friedrichshain','Kreuzberg','Charlottenburg']
district.insert(0,{location})

#select route
import random
location_desc=random.choice([' - beautiful place!',' - cool area!',' - nice location!'])

print(f"\n{location}{location_desc}")
print(f"\nFrom {location}, you leave your place and on your way, you end up at an intersection.")

 
    

    
    
    
    
########## LOOPS
#There are 2 out of 3 districts in which you can get to your sub-destination, where player chooses a district and in that district there are 2 puzzles.
route_found=False
import time

while not route_found:
    
    route=input(f"\n~*=*=*=*=*=*~\033[1;34m\nThrough which district would you like to go to?\n{', '.join(district[1:])}: \033[0m").capitalize()
    
    
    while route not in district:    
        print(f'\nIs "{route}" even a place? Try again.\n')
        break
        
    
        
    if route=='Friedrichshain':
        print(f'\n{route} {node["Friedrichshain_desc"]}\n')
        print('The streets are under construction. \n\t...You cannot enter. Turn around.\n')
    
    
    
    
    elif route=='Kreuzberg':
        print(f'\n{route} {node["Kreuzberg_desc"]}\n')
        pause=input(f'\n\033[1;34m{node["pause"]["pause_text"]} \033[0m').upper()
    
        
        while not pause=='B' and not pause=='L':
            print(node["validate"])
            pause=input(f'\n{node["pause"]["pause_validate"]}\n').upper()
                 
        if pause=='B':
            print(f'\n{node["pause"]["pause_Beer_K"]}\n')
        elif pause=='L':
            print(f'\n{node["pause"]["pause_Lunch_K"]}\n')
            transportation=input(f'\n\033[1;34m{node["transportation"]["transportation_text"]}? \033[0m').upper()
            
            while not transportation=='T' and not transportation=='B':
                print(node["validate"])
                transportation=input(f'{node["transportation"]["transportation_validate"]}\n').upper()

            if transportation=='T':
                print(f'{node["transportation"]["transportation_Train_K"]}\n')
                route_found=True
            elif transportation=='B':
                print(f'\n{node["transportation"]["transportation_Bus_K"]}\n!')
            
    
    
    
    
    elif route=='Charlottenburg':        
        print(f'\n{route} {node["Charlottenburg_desc"]}\n') 
        pause=input(f'\n\033[1;34m{node["pause"]["pause_text"]} \033[0m').upper()
        
        while not pause=='B' and not pause=='L':
            print(node["validate"])
            pause=input(f'{node["pause"]["pause_validate"]}\n').upper()
        
        if pause=='L':
            print(f'\n{node["pause"]["pause_Lunch_C"]}\n')
        elif pause=='B':
            print(f'\n{node["pause"]["pause_Beer_C"]}\n')
            transportation=input(f'\n\033[1;34m{node["transportation"]["transportation_text"]}? \033[0m').upper()
            
            while not transportation=='T' and not transportation=='B':
                print(node["validate"])
                transportation=input(f'{node["transportation"]["transportation_validate"]}\n').upper()
                
            if transportation=='B':
                print(f'\n{node["transportation"]["transportation_Bus_C"]}\n')
                route_found=True
            elif transportation=='T':
                print(f'\n{node["transportation"]["transportation_Train_C"]}.\n') 


                
         
            
########## FINAL ROOM & OUTRO

walk=['Bridge', 'Tunnel', 'Street']


tries = 2
wrong = 'Oh no, the path is blocked!\nYou only have 1 chance\n\t...quick!'
lose = "Sorry, you didn't get to your destination! Goodbye apartment. Better luck next time!"
win = 'You made it JUST IN TIME! You sign your contract and the landlord officially accepts you as a tenant.'



print('\n~*=*=*=*=*=*~\nNow, you end up at the final intersection\n\t...but there is only ONE way to get to your final destination.\n')

print(f"you only have {tries} chance(s)\n\t...or you won't get there in time.\n")

#while loop
# while tries:    
#     room=input(f'\nWhich path do you think you should take -- go over the "{walk[0]}", go through the "{walk[1]}", or just walk on the "{walk[2]}" ?' ).capitalize()

#     while room not in walk:
#         print(f'\n"{room}" is not one of the options. Try again.\n')
#         room=input(f"Choose: {', '.join(walk)}\n").capitalize()
        
    
#     if room == 'Tunnel':
#         print("\033[1;34m"+"*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"+"\033[0m")
#         print(f'\n{win}')
#         print("""        
#                        @@@@/                 
#             .@@@(  #@@@% @@@@               
#             .@@@@@@@@      /@@@@            
#              @@@@@@           @@@@(         
#             @@@@                 @@@@       
#          .@@@@@@&&&&&%%%%%%########&@@@@    
#        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@( 
#      @@@@ @@&  .....              . @@@  @@ 
#           @@& @    @         @    @ @@@     
#           @@& @@@@@@         @(***@ &@@     
#           @@&        @@@@@@@        %@@.    
#           @@&        %@   @@        #@@.    
#           @@&        *@.  @@        /@@*    
#           @@&        .@*  %@        ,@@/    
#           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
#                """)
#         print("Your apartment hunt has been successful.\n")
#         print("\033[1m"+"\033[1;32m"+"CONGRATULATIONS!!!"+"\033[0m"+"\033[0m")
#         print("\nNext step, Anmeldung...")
#         print("\033[1;34m"+"*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"+"\033[0m")
#         tries=False
#     else:
#         if tries == 2:
#             tries-=1
#             print(f'\n{wrong}')
#             walk.remove(room)
#         else:
#             print("\033[1;34m"+"*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"+"\033[0m")
#             print(f'\n{lose}')
#             print("""
#                           ((((((.     .((((/(                         
#                        ((((                 ((((                      
#                      (((                       (((                    
#                     ((      ((((       ((((      /(                   
#                    ((      ((((((     ((((((      ((                  
#                   (/                               ((                 
#                   ((           (((((((((           (/                 
#                   ((        (((.       ,(((        ((                 
#                    ((     ((               ((     ((                  
#                     ((   ((                 (/   ((                   
#                      (((                       (((                    
#                        ((((                 ((((                      
#                           /(((((*     /(((((*  
            
#             """)
#             print("\n\033[1m"+"\033[1;31m"+"GAME OVER! PLAY AGAIN."+"\033[0m"+"\033[0m")
#             print("\033[1;34m"+"*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"+"\033[0m")
#             break




#For loop

for i in range(tries):
    room=input(f"\033[1;34m\nWhich path should you take -- {', '.join(walk)}? \033[0m").capitalize()

    while room not in walk:
        print(f'\n"{room}" is not one of the options. Try again.\n')
        room=input(f"Choose: {', '.join(walk)}\n").capitalize()
        
    if room== 'Tunnel':
        for i in [0]:
            print("\033[1;32m"+"*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"+"\033[0m")
            print(f'\n{win}')
            time.sleep(5)
            print("""        
                       @@@@/                 
            .@@@(  #@@@% @@@@               
            .@@@@@@@@      /@@@@            
             @@@@@@           @@@@(         
            @@@@                 @@@@       
         .@@@@@@&&&&&%%%%%%########&@@@@    
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@( 
     @@@@ @@&  .....              . @@@  @@ 
          @@& @    @         @    @ @@@     
          @@& @@@@@@         @(***@ &@@     
          @@&        @@@@@@@        %@@.    
          @@&        %@   @@        #@@.    
          @@&        *@.  @@        /@@*    
          @@&        .@*  %@        ,@@/    
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
               """)
            print("Your apartment hunt has been successful.\n")
            time.sleep(2)
            print("\033[1m"+"\033[1;32m"+"CONGRATULATIONS!!!"+"\033[0m"+"\033[0m")
            print("\nNext step, Anmeldung...")
            print("\033[1;32m"+"*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"+"\033[0m")
        break
    else:
        if tries == 2:
            print(f'\n{wrong}\n')
            tries-=1
            walk.remove(room)
        else:
            for i in [0]:
                print("\033[1;31m"+"*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"+"\033[0m")
                print('Oh no, the path is also blocked!')
                print(f'\n{lose}')
                time.sleep(5)
                print("""
                              ((((((.     .((((/(                         
                           ((((                 ((((                      
                         (((                       (((                    
                        ((      ((((       ((((      /(                   
                       ((      ((((((     ((((((      ((                  
                      (/                               ((                 
                      ((           (((((((((           (/                 
                      ((        (((.       ,(((        ((                 
                       ((     ((               ((     ((                  
                        ((   ((                 (/   ((                   
                         (((                       (((                    
                           ((((                 ((((                      
                              /(((((*     /(((((*  

                """)
                time.sleep(3)
                print("\n\033[1m"+"\033[1;31m"+"GAME OVER! PLAY AGAIN."+"\033[0m"+"\033[0m")
                print("\033[1;31m"+"*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"+"\033[0m")
                break



