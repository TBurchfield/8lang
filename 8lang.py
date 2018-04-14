#!/usr/bin/env python3
import sys
import time
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
class Thread():
  def __init__(self, x, y, velocity, value):
    self.x = x
    self.y = y
    self.velocity = velocity
    self.value = value
  def advance(self):
    if self.velocity == UP:
      self.y -= 1
    if self.velocity == DOWN:
      self.y += 1
    if self.velocity == LEFT:
      self.x -= 1
    if self.velocity == RIGHT:
      self.x += 1

class Program():
  def __init__(self, program):
    self.state = State()
    self.program = program
  def process(self):
    step_threads(self.program, self.state)
    while not self.state.end:
      #show_state(self.program, self.state)
      step_threads(self.program, self.state)
    return self.state.acc

class State():
  def __init__(self):
    self.end = False
    self.acc = False
    self.threads = set([Thread(0,0,RIGHT, 0)])

def usage(rc):
  print("Usage:")
  print("{} <filename>".format(sys.argv[0]))
  print("where <filename> is an 8lang source file.")
  exit(rc)

def show_state(program, state):
  out = [line for line in program]
  for thread in state.threads:
    out[thread.y] = '{}{}{}'.format(out[thread.y][:thread.x],thread.value,out[thread.y][thread.x+1:])
  time.sleep(.1)
  print('X' * (len(program[0]) + 2))
  for line in out:
    pass
    print('X', end='')
    print(line, end='')
    print('X')
  print('X' * (len(program[0]) + 2))

def rotate_cw(velocity):
  if velocity == RIGHT:
    return DOWN
  if velocity == DOWN:
    return LEFT
  if velocity == LEFT:
    return UP
  if velocity == UP:
    return RIGHT

def rotate_ccw(velocity):
  if velocity == RIGHT:
    return UP
  if velocity == DOWN:
    return RIGHT
  if velocity == LEFT:
    return DOWN
  if velocity == UP:
    return LEFT

def step_threads(program, state):
  new_threads = set()
  for thread in state.threads:
    out_threads = step_thread(program, thread, state)
    for new_thread in out_threads:
      new_threads.add(new_thread)
  state.threads = new_threads

def step_thread(program, thread, state):
  thread.advance()
  if thread.y >= len(program) or thread.y < 0 or thread.x >= len(program[thread.y]) or thread.x < 0:
    state.end = True
    state.acc = thread.value
    return []
  c = program[thread.y][thread.x]
  if c == '#':
    if thread.value > 0:
      thread.velocity = rotate_ccw(thread.velocity)
    elif thread.value < 0:
      thread.velocity = rotate_cw(thread.velocity)
    return [thread]
  elif c == '/':
    if thread.velocity == RIGHT:
      thread.velocity = UP
    elif thread.velocity == LEFT:
      thread.velocity = DOWN
    elif thread.velocity == UP:
      thread.velocity = RIGHT
    elif thread.velocity == DOWN:
      thread.velocity = LEFT
    return [thread]
  elif c == '\\':
    if thread.velocity == RIGHT:
      thread.velocity = DOWN
    elif thread.velocity == LEFT:
      thread.velocity = UP
    elif thread.velocity == UP:
      thread.velocity = LEFT
    elif thread.velocity == DOWN:
      thread.velocity = RIGHT
    return [thread]
  elif c == '<' and thread.velocity == RIGHT:
    new = Thread(thread.x, thread.y, UP, thread.value)
    thread.velocity = DOWN
    return [new, thread]
  elif c == '>' and thread.velocity == LEFT:
    new = Thread(thread.x, thread.y, UP, thread.value)
    thread.velocity = DOWN
    return [new, thread]
  elif c == 'v' and thread.velocity == UP:
    new = Thread(thread.x, thread.y, RIGHT, thread.value)
    thread.velocity = LEFT
    return [new, thread]
  elif c == '^' and thread.velocity == DOWN:
    new = Thread(thread.x, thread.y, RIGHT, thread.value)
    thread.velocity = LEFT
    return [new, thread]
  elif c == ',':
    v = sys.stdin.read(1)
    if v == '':
      thread.value = 0
      return [thread]
    thread.value = ord(v)
    return [thread]
  elif c == '.':
    print(chr(thread.value), end='')
    return [thread]
  elif c == 'T':
    print("'T' is not yet implemented.  Sorry.")
    exit(1)
  elif c == '+':
    thread.value += 1
    return [thread]
  elif c == '-':
    thread.value -= 1
    return [thread]
  elif c == '_':
    if thread.velocity == UP:
      thread.velocity = DOWN
    elif thread.velocity == DOWN:
      thread.velocity = UP
    return [thread]
  elif c == '|':
    if thread.velocity == LEFT:
      thread.velocity = RIGHT
    elif thread.velocity == RIGHT:
      thread.velocity = LEFT
    return [thread]
  return [thread]

if __name__=='__main__':
  program_text = []
  if len(sys.argv) != 2:
    usage(1)
  filename = sys.argv[1]
  max_len = 0
  for line in open(filename, 'r'):
    program_text.append(line.rstrip())
    max_len = max(max_len, len(program_text[-1]))
  i = 0
  while i < len(program_text):
    program_text[i] = program_text[i].ljust(max_len, ' ')
    i += 1
  s = Program(program_text)
  print('Return: {}'.format(s.process()))
