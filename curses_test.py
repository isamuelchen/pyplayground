import curses

def window(stdscr):

  sh, sw = stdscr.getmaxyx()
  stdscr.addstr(0, 0, str(sh))
  stdscr.addstr(1, 0, str(sw))
  
  y= sh / 2
  x= sw / 2 - 2.5
  stdscr .addstr(int(y), int(x), "hello")
  while True:
    #getch will get users
    user_key=stdscr.getch()
    if user_key in [27,113,81]:
      break
 
curses.wrapper(window)

 