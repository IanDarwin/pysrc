''' Print the python shell history. Crunched onto one line since you'll commonly just copy-and-paste it. '''
import readline; print('\n'.join([str(readline.get_history_item(i + 1)) for i in range(readline.get_current_history_length())]))
