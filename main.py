from util import Display, eprint
from time import sleep
from board import Board


def main():
    # Create the display object. This is found in util.py
    x=3
    y=3
    display = Display()
    board = Board()
    message = 'Hello'
    key_template = "The last key pressed was: \n {} {}"


    while True:
        # See util.py for where these methods are defined
        display.print_board(board.get_stone_at)
        display.display_message(message)
        display.refresh()


        #######################################################
        # Task 1:
        # Move the cursor when they arrow keys are pressed.
        # You can find the libcurses documentation here
        # https://docs.python.org/3/library/curses.html#constants

        input_char = display.get_input()
        display.set_cursor((x,y))

        if input_char == 67:
            x=x+1
        elif input_char == 66:
            y=y+1
        elif input_char == 65:
            y=y-1
        elif input_char == 68:
            x=x-1

        display.set_cursor((x,y))

        # These may help you figure out what is going on
        eprint("This appears in the error log.", input_char)
        message = key_template.format(input_char, chr(input_char))

        #
        ######################################################
    
if __name__ == "__main__":
    main()
    
