import curses
import serial
import time
import pygame

from config import CLIENT_BLUETOOTH_DEVICE

pygame.init()
screen = pygame.display.set_mode((400, 300))

port  = serial.Serial(CLIENT_BLUETOOTH_DEVICE, 9600, bytesize=serial.EIGHTBITS)

done = False
send = None
while not done:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_DOWN:
              send = 'b'
              print('DOWN')
          if event.key == pygame.K_UP:
              send = 'f'
              print('UP')
          if event.key == pygame.K_LEFT:
              send = 'l'
              print('LEFT')
          if event.key == pygame.K_RIGHT:
              send = 'r'
              print('RIGHT')
          if event.key == pygame.K_q:
              done = True

      elif event.type == pygame.KEYUP:
        send = 's'
        print('stop')  
      if send:
        port.write(send.encode('utf-8'))
        send = False



while True:
  char = screen.getch()
  if char == curses.KEY_UP:
    send = 'f'
  elif char == curses.KEY_DOWN:
    send = 'b'
  elif char == curses.KEY_LEFT:
    send = 'l'
  elif char == curses.KEY_RIGHT:
    send = 'r'
  elif char == ord('q'):
      break
  else:
      send = 's'

  if prev != send:
      prev = send



port.close()
