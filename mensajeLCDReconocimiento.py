import drivers
from time import sleep

display = drivers.Lcd()

try:
    
    while True:
        print("Writing to display")
        display.lcd_display_string("Hola Mundo! :)", 1) 
        display.lcd_display_string("Mi nombre es:", 2)  
        sleep(3)                                        
        display.lcd_clear()
        display.lcd_display_string("Mi nombre es:", 1)  
        display.lcd_display_string("Carina Escudero", 2)
        sleep(3)
        display.lcd_clear()
        display.lcd_display_string("Carina Escudero", 1)
        display.lcd_display_string("Perez :)", 2)
        sleep(3)                                        
        display.lcd_clear()                             
        sleep(2)                                        
except KeyboardInterrupt:
    
    print("Cleaning up!")
    display.lcd_clear()