init -2 python:
    import sys
    sys.path.append(renpy.loader.transfn("scripts"))
    
init -1 python:
    sys.path.append(renpy.loader.transfn("scripts/person"))
    from random import *
    from output import Outputable
    from obj_character import Person, gen_random_person, get_avatars
init python:
    pass

# The game starts here.

label splashscreen:
    call screen sc_choose_language
    
    return

label start:
    show expression "interface/bg_base.jpg" as bg
    call lbl_choose_type
    return
    
label lbl_choose_type:
    call texts_dictionary
    menu:
        'Дженерик':
            $ to_say = generic
        'Принцесса':
            $ to_say = princess
        'Крестьянка':
            $ to_say = pesant  
            
    call lbl_output
    return

label lbl_output:
    $ say = to_say['hello']
    '[say]'   

    $ say = to_say['happy']
    '[say]'   
    
    $ say = to_say['bye']    

    menu:
        "[say]":
            $ renpy.full_restart()

    return

screen sc_choose_language:
    add "interface/bg_base.jpg"
    modal True
    imagebutton:
        idle im.Grayscale('images/rus.jpg') 
        hover 'images/rus.jpg'
        xalign 0.1 yalign 0.5
        focus_mask True 
        action [Language('rus'), Return()]
    imagebutton:
        idle im.Grayscale('images/eng.jpg') 
        hover 'images/eng.jpg'
        xalign 0.9 yalign 0.5
        focus_mask True 
        action [Language('eng'), Return()]
