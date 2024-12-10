import PySimpleGUI as sg

layout = [
    [sg.Text("Enter Feet:    "), sg.InputText(key="feet", tooltip="Enter a whole number")],
    [sg.Text("Enter Inches: "), sg.InputText(key="inches", tooltip="Enter a whole number")],
    [sg.Button("Convert", key="convert")],[sg.Text(" ", key="output")]
]

window = sg.Window("Convert", layout=layout, font=("Helvetica", 10))

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == sg.WIN_CLOSED:
        break
    if event == "Convert":
        try:
            num1 = float(values["feet"]) * 12
            num2 = float(values["inches"])
            tot_inches = num1 + num2
            output = tot_inches * 0.0254

            window["output"].update(f"{tot_inches} Inches is {output} meters long...")
        except ValueError:
            window["output"].update("Please enter valid numbers! ")


print("Bye!")
window.close()

