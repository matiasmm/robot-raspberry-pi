import l293d
import time
import serial

MOTOR_1_ENABLE = 22
MOTOR_1_PIN_1 = 16
MOTOR_1_PIN_2 = 18

MOTOR_2_ENABLE = 12
MOTOR_2_PIN_1 = 13
MOTOR_2_PIN_2 = 15

motor1 = l293d.DC(MOTOR_1_ENABLE, MOTOR_1_PIN_1, MOTOR_1_PIN_2)
motor2 = l293d.DC(MOTOR_2_ENABLE, MOTOR_2_PIN_1, MOTOR_2_PIN_2)

try:
  motor1.clockwise()
  motor2.anticlockwise()
  time.sleep(1)
  motor1.anticlockwise()
  motor2.clockwise()
  time.sleep(1)
  motor1.stop()
  motor2.stop()
finally:
  pass
