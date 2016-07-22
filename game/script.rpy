init -2 python:
    import sys
    sys.path.append(renpy.loader.transfn("scripts"))
    
init -1 python:
    from random import *
    from output import Outputable
init python:
    pass

# The game starts here.

label splashscreen:
    $ renpy.change_language(None)
    call screen sc_choose_language
    
    return

label lang_rus:
    $ renpy.change_language('rus')
    return

label start:
    $ Outputable.set_lang(_preferences.language)
    $ antosha = Outputable('Antosha Sichev', 'antosha')
    $ to_say = antosha.description()
    show expression "interface/bg_base.jpg" as bg
    
    call lbl_choose_type
    return
    
label lbl_choose_type:
    menu:
        'Дженерик':
            $ chartype = 'generic'
        'Принцесса':
            $ chartype = 'princess'
        'Крестьянка':
            $ chartype = 'pesant'  
            
    call lbl_output
    return

label lbl_output:

    '[to_say]'   
    
    menu:
        "That's all folks!":
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
        action Jump('lang_rus')
    imagebutton:
        idle im.Grayscale('images/eng.jpg') 
        hover 'images/eng.jpg'
        xalign 0.9 yalign 0.5
        focus_mask True 
        action Return()
