import RPi.GPIO as GPIO
import math
import xbox
 
GPIO_LED_GREEN  = 23
GPIO_LED_RED    = 22
GPIO_LED_YELLOW = 27
GPIO_LED_BLUE   = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
GPIO.setup(GPIO_LED_GREEN, GPIO.OUT)
GPIO.setup(GPIO_LED_RED, GPIO.OUT)
GPIO.setup(GPIO_LED_YELLOW, GPIO.OUT)
GPIO.setup(GPIO_LED_BLUE, GPIO.OUT)
 
if __name__ == '__main__':
    joy = xbox.Joystick()
    
    while not joy.Back():
        
        # LEDs
        led_state_green  = GPIO.HIGH if joy.A() else GPIO.LOW
        led_state_red    = GPIO.HIGH if joy.B() else GPIO.LOW
        led_state_yellow = GPIO.HIGH if joy.Y() else GPIO.LOW
        led_state_blue   = GPIO.HIGH if joy.X() else GPIO.LOW
            
        GPIO.output(GPIO_LED_GREEN, led_state_green)
        GPIO.output(GPIO_LED_RED, led_state_red)
        GPIO.output(GPIO_LED_YELLOW, led_state_yellow)
        GPIO.output(GPIO_LED_BLUE, led_state_blue)
        
    joy.close()
