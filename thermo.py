import sys #needed to use arguments
import os, glob #needed for deleting

NAME = sys.argv[1]
ID = NAME.lower()
ID = ID.replace(' ', '_')

print('NAME: ' + NAME)
print('ID: ' + ID)

genFilePrefix       = 'th_'

templateFolder      = 'templates/'

autoFileTemplate    = templateFolder + 'thermo_automation_template.yaml'
autofolder          = 'automation/'
autoFile            = autofolder + genFilePrefix + 'automation_' + ID + '.yaml'

listOfTemplates     = [autoFileTemplate]
listOfNewFiles      = [autoFile        ]
listOfFolders       = [autofolder      ]

newAdminGroupString = \
'      #card\n' \
'      - type: entities\n'\
'        title: ' + NAME + '\n' \
'        show_header_toggle: false\n' \
'        entities:\n' \
'          - entity: climate.' + ID + '\n' \
'            name: ' + NAME + '\n' \
'          - sensor.temperatur_' + ID + '\n' \
'          - sensor.luftfeuchtigkeit_' + ID + '\n' \
'          - binary_sensor.state_' + ID + '\n' \
'          - binary_sensor.sensorfehler_' + ID + '\n' \
'          - sensor.firmware_' + ID + '\n' \
'          - switch.firmwareupdate_' + ID + '\n' \
'          - switch.neustart_' + ID + '\n' \
'          - sensor.ip_' + ID + '\n' \
'          - sensor.skalierung_' + ID + '\n' \
'          - sensor.offset_' + ID + '\n' \
'          - sensor_hysteresis_' + ID

writeFile           = False

    # generate new files
    for templateFile in listOfTemplates:
        idx = listOfTemplates.index(templateFile)
        with open(listOfNewFiles[idx], 'w+') as output, open(templateFile, 'r') as input:
            data = input.read()
            data = data.replace('{{ID}}', ID)
            data = data.replace('{{NAME}}', NAME)
            output.write(data)
            input.close()
            output.close()

# add admin_group to all thermostat admin group
with open(allThermoAdminFile, 'r') as myFile:
    data = myFile.read()
    if (data.find(newAdminGroupString)) == -1:
        writeFile = True
    else:
        writeFile = False
    myFile.close()

if (writeFile == True):
    with open(allThermoAdminFile, 'w') as myFile:
        data = data.replace(newAdminGroupToken, newAdminGroupString + '\n' + newAdminGroupToken)
        myFile.write(data)
        myFile.close()