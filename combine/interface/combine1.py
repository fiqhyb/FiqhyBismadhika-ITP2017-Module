def mainc():
    while True:
        input_menu = input("Menu:\na for barcode\nb for story\nc to exit\ninput:")
        from programs import Barcode as a
        from programs import Story as b

        if input_menu=="a":
            a.maina()
        elif input_menu=="b":
            b.mainb()
        elif input_menu=="c":
            quit()
        elif input_menu == "back":
            input_menu
