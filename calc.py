import PySimpleGUI as sg

equation = ""
display = ""

ob = {"size": (8,2), "button_color": "#c98c15", 'font':('Franklin Gothic Book', 13, "bold")}
lgb = {"size": (8,2), "button_color": "#a8a4b0", 'font':('Franklin Gothic Book', 13, "bold")}
gb = {"size": (8,2), "button_color": "#6e6878", 'font':('Franklin Gothic Book', 13, "bold")}
rb = {"size": (8,2), "button_color": "#b65549",'font':('Franklin Gothic Book', 13, "bold")}

def update_display():
  if equation.isdigit:
    window['DISPLAY'].update(value=display)
  elif len(equation) >= 37:
    window['DISPLAY'].update(value=display[-37:-1])
  else:
    window['DISPLAY'].update(value=display[:-1])

layout = [
  [sg.Text(size=(10, 1), justification="right", background_color="white", text_color="red", font=('Digital-7', 48), key="DISPLAY")],
  [sg.Button("C", **rb), sg.Button("CE", **rb), sg.Button("(", **ob), sg.Button(")", **ob)],
  [sg.Button("7", **gb), sg.Button("8", **gb), sg.Button("9", **gb), sg.Button("/", **lgb)],
  [sg.Button("4", **gb), sg.Button("5", **gb), sg.Button("6", **gb), sg.Button("*", **lgb)],
  [sg.Button("1", **gb), sg.Button("2", **gb), sg.Button("3", **gb), sg.Button("-", **lgb)],
  [sg.Button("0", **gb), sg.Button(".", **gb), sg.Button("=", **lgb), sg.Button("+", **lgb)],
  ]

window = sg.Window('Calculator', layout=layout, background_color="#001820")

while True:
  event, values = window.read()   

  if event == sg.WIN_CLOSED:
    break 

  if event in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", ")", "."]:
    display += event
    equation += event
    update_display()

  elif len(equation) == 0 and event == "(":
    display += "("
    equation += "1*("
    update_display()

  elif (len(equation) > 1 and event == "(" and equation[-1] != "("):
    display += "("
    equation += "*("
    update_display()

  elif event == "(" and equation[-1] == "(":
    display += "("
    equation += "("
    update_display()

  elif event == "C":
    display = ""
    equation = ""
    update_display()

  elif len(equation) >= 2 and event == "CE" and equation[-2:] == "*(":
    display = display[:-2]
    equation = equation[:-2]
    update_display()

  elif (len(equation) >= 2 and event == "CE" and equation[-2:] != "*(") or (len(equation) < 2 and event == "CE"):
    display = display[:-1]
    equation = equation[:-1]
    update_display()   

  elif event == "=":
      display = str(eval(equation))
      if len(display) > 3 and display[-2] == "." and display[-1] == "0":
        display = display[:-2]
      update_display()
      equation = display

window.close()