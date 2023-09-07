import PySimpleGUI as sg
import subprocess

# Define the layout of the GUI
layout = [
    [sg.Text('Enter the username for resetting configurations:')],
    [sg.Input(key='-USERNAME-')],
    [sg.Button('Reset Configurations')]
]

# Create the window
window = sg.Window('Reset User Configurations', layout)

# Event loop
while True:
    event, values = window.read()
    
    # Close the window if the user closes it or clicks the "Reset Configurations" button
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Reset Configurations':
        # Get the username entered by the user
        target_user = values['-USERNAME-']
        
        # Copy contents of /etc/skel to user's home directory
        subprocess.run(['cp', '-R', '/etc/skel/.', f'/home/{target_user}'])
        
        # Delete existing configuration files
        subprocess.run(['rm', '-rf', f'/home/{target_user}/.config'])

        subprocess.run(['rm', '-rf', f'/home/{target_user}/.local'])

        subprocess.run(['rm', '-rf', f'/home/{target_user}/.cache'])
        
        # Show a message box indicating the reset is complete
        sg.popup('Reset complete!', title='Reset User Configurations')
        break

# Close the window
window.close()
