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

bsFileTemplate      = templateFolder + 'thermo_binary_sensors_template.yaml'
bsFolder            = 'binary_sensors/'
bsFile              = bsFolder + genFilePrefix + 'binary_sensors_' + ID + '.yaml'

groupFileTemplate   = templateFolder + 'thermo_group_template.yaml'
groupFolder         = 'group/'
groupFile           = groupFolder + genFilePrefix + 'group_' + ID + '.yaml'

climateFileTemplate      = templateFolder + 'thermo_climate_template.yaml'
climateFolder            = 'climate/'
climateFile              = climateFolder + genFilePrefix + 'climate_' + ID + '.yaml'

sensFileTemplate    = templateFolder + 'thermo_sensors_template.yaml'
sensFolder          = 'sensors/'
sensFile            = sensFolder + genFilePrefix + 'sensors_' + ID + '.yaml'

switchFileTemplate  = templateFolder + 'thermo_switch_template.yaml'
switchFolder        = 'switch/'
switchFile          = switchFolder + genFilePrefix + 'switch_' + ID + '.yaml'

listOfTemplates     = [autoFileTemplate, bsFileTemplate, groupFileTemplate, climateFileTemplate, sensFileTemplate, switchFileTemplate]
listOfNewFiles      = [autoFile        , bsFile        , groupFile        , climateFile        , sensFile        , switchFile]
listOfFolders       = [autofolder      , bsFolder      , groupFolder      , climateFolder      , sensFolder      , switchFolder]

viewsFile           = 'group/views.yaml'
newGroupToken       = '#{{GROUP}}'
newGroupString      = '- group.' + ID + '_group'

allThermoAdminFile = 'group/group_thermo_admin_all.yaml'
newAdminGroupToken  = '#{{ADMINGROUP}}'
newAdminGroupString = '- group.' + ID + '_admin_group'

tempsGroupfile      = 'group/group_current_temps.yaml'
newTempToken        = '#{{TEMP}}'
newTempString       = '- sensor.temperatur_' + ID

climateGroupfile      = 'group/group_climate.yaml'
newClimateToken        = '#{{CLIMATE}}'
newClimateString       = '- climate.thermostat_' + ID

historyfolder       = 'history/'
historyFile         = historyfolder + genFilePrefix + 'history_' + ID + '.yaml'


if (ID != 'remove'):
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
            
    # add group to heating view
    with open(viewsFile, 'r') as myFile:
        data = myFile.read()
        if (data.find(newGroupString)) == -1:
            writeFile = True
        else:
            writeFile = False
        myFile.close()
    
    if (writeFile == True):
        with open(viewsFile, 'w') as myFile:
            data = data.replace(newGroupToken, newGroupString + '\n      ' + newGroupToken)
            myFile.write(data)
            myFile.close()
    
    # re-init variable
    writeFile = False
    
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
            data = data.replace(newAdminGroupToken, newAdminGroupString + '\n      ' + newAdminGroupToken)
            myFile.write(data)
            myFile.close()

    # re-init variable
    writeFile = False
    
    # add current thermostat to climate group
    with open(climateGroupfile, 'r') as myFile:
        data = myFile.read()
        if (data.find(newClimateString)) == -1:
            writeFile = True
        else:
            writeFile = False
        myFile.close()
        
    if (writeFile == True):
        with open(climateGroupfile, 'w') as myFile:
            data = data.replace(newClimateToken, newClimateString + '\n      ' + newClimateToken)
            myFile.write(data)
            myFile.close()

    # re-init variable
    writeFile = False
    
    # add current temp to current temps group
    with open(tempsGroupfile, 'r') as myFile:
        data = myFile.read()
        if (data.find(newTempString)) == -1:
            writeFile = True
        else:
            writeFile = False
        myFile.close()
        
    if (writeFile == True):
        with open(tempsGroupfile, 'w') as myFile:
            data = data.replace(newTempToken, newTempString + '\n      ' + newTempToken)
            myFile.write(data)
            myFile.close()

    # add current temp to history
    with open(historyFile, 'w') as myFile:
        myFile.write('      - sensor.temperatur_' + ID + '\n      - binary_sensor.heizung_aktiv_' + ID)
        myFile.close()
else:
    for filename in glob.glob(historyfolder + genFilePrefix +"*"):
        os.remove(filename)
    for folder in listOfFolders:
        for filename in glob.glob(autofolder + genFilePrefix +"*"):
            os.remove(filename)
        for filename in glob.glob(bsFolder + genFilePrefix +"*"):
            os.remove(filename)
        for filename in glob.glob(groupFolder + genFilePrefix +"*"):
            os.remove(filename)
        for filename in glob.glob(climateFolder + genFilePrefix +"*"):
            os.remove(filename) 
        for filename in glob.glob(sensFolder + genFilePrefix +"*"):
            os.remove(filename)
        for filename in glob.glob(switchFolder + genFilePrefix +"*"):
            os.remove(filename)