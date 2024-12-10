'''
For more structured layouts, you can use
sg.Column to create column instances.Here is an
example:
'''

import PySimpleGUI as sg


'''
First solution
# Prepare the widgets for the left column
left_column_content = [[sg.Text('Left 1  ')],
                       [sg.Input('Left 1')],
                       [sg.Text('Left 2  ')],
                       [sg.Input('Left 2 ')]]

# Prepare the widgets for the right column
right_column_content = [[sg.Text('Right 1')],
                        [sg.Input('Right 1')],
                        [sg.Text('Right 2')],
                        [sg.Input('Right 2')],]


Note:
sg.Text = used for labels. Cannot be changed by users
sg.Input = modern way to get users input
sg.InputText = Older version of sg.Input
'''

# Second Solution
# Construct the Column widgets
#left_column = sg.Column(left_column_content)
#right_column = sg.Column(right_column_content)
left_column = sg.Column([[sg.Text('Left 1  ')],
                       [sg.InputText('Left 1')],
                       [sg.Text('Left 2  ')],
                       [sg.Input('Left 2 ')]])
right_column = sg.Column([[sg.Text('Right 1')],
                        [sg.Input('Right 1')],
                        [sg.Text('Right 2')],
                        [sg.Input('Right 2')],])

# Construct the layout
layout = [[left_column, right_column]]

# Construct and display the window
window = sg.Window('Columns Sample Window Layout', layout)
window.read()
window.close()