import l293d
import time
import serial



MOTOR_1_ENABLE = 22
MOTOR_1_PIN_1 = 16
MOTOR_1_PIN_2 = 18

MOTOR_2_ENABLE = 11
MOTOR_2_PIN_1 = 13
MOTOR_2_PIN_2 = 15



blue = serial.Serial('/dev/ttyAMA0', 9600, timeout=2)


motor1 = l293d.DC(MOTOR_1_ENABLE, MOTOR_1_PIN_1, MOTOR_1_PIN_2)
motor2 = l293d.DC(MOTOR_2_ENABLE, MOTOR_2_PIN_1, MOTOR_2_PIN_2)
last_direction = None

def stop_motion():
    motor1.stop()
    motor2.stop()

def move(direction):
    global last_direction
    if direction != last_direction:
        last_direction = direction
        if direction == "STOP":
          stop_motion()
        elif direction == "FORWARD":
          motor1.clockwise()
          motor2.clockwise()
        elif direction == "BACKWARDS":
          motor1.anticlockwise()
          motor2.anticlockwise()
        elif direction == "RIGHT":
          motor1.clockwise()
          motor2.anticlockwise()
        elif direction == "LEFT":
          motor2.clockwise()
          motor1.anticlockwise()

try:
    while True:
        if blue.in_waiting:
          result = blue.read(1)  
          if len(result) >= 0:
            char = result.decode('utf-8')
            if char == 'f':
                move("FORWARD")
            elif char == 'b':
                move("BACKWARDS")
            elif char == 'l':
                move("LEFT")
            elif char == 'r':
                move("RIGHT")
            elif char == 's':
                move("STOP")
            elif char == 'q':
                break
finally:
    print("Algun error hubo")

