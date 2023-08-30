import curses

def window(stdscr):

  msg="hello mr bit aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  wrd_in_mssg= len(msg)
  hlf_of_wrd_in_mssg= wrd_in_mssg / 2
  sh, sw = stdscr.getmaxyx()
  stdscr.addstr(0, 0, str(sh))
  stdscr.addstr(1, 0, str(sw))
  
  y= sh / 2
  x= sw / 2 - hlf_of_wrd_in_mssg
  stdscr .addstr(int(y), int(x), msg)
  while True:
    #getch will get users
    user_key=stdscr.getch()
    if user_key in [27,113,81]:
      break
 
curses.wrapper(window)

 
