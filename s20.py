import sys #needed to use arguments
import os, glob #needed for deleting

NAME = sys.argv[1]
ID = NAME.lower()
ID = ID.replace(' ', '_')

print('NAME: ' + NAME)
print('ID: ' + ID)

genFilePrefix       = 's20_'

templateFolder      = 'templates/'

autoFileTemplate    = templateFolder + 's20_automation_template.yaml'
autofolder          = 'automation/'
autoFile            = autofolder + genFilePrefix + 'automation_' + ID + '.yaml'

bsFileTemplate      = templateFolder + 's20_binary_sensors_template.yaml'
bsFolder            = 'binary_sensors/'
bsFile              = bsFolder + genFilePrefix + 'binary_sensors_' + ID + '.yaml'

groupFileTemplate   = templateFolder + 's20_group_template.yaml'
groupFolder         = 'group/'
groupFile           = groupFolder + genFilePrefix + 'group_' + ID + '.yaml'

sensFileTemplate    = templateFolder + 's20_sensors_template.yaml'
sensFolder          = 'sensors/'
sensFile            = sensFolder + genFilePrefix + 'sensors_' + ID + '.yaml'

switchFileTemplate  = templateFolder + 's20_switch_template.yaml'
switchFolder        = 'switch/'
switchFile          = switchFolder + genFilePrefix + 'switch_' + ID + '.yaml'

listOfTemplates     = [autoFileTemplate , bsFileTemplate, groupFileTemplate, sensFileTemplate , switchFileTemplate]
listOfNewFiles      = [autoFile         , bsFile        , groupFile        , sensFile         , switchFile]
listOfFolders       = [autofolder       , bsFolder      , groupFolder      , sensFolder       , switchFolder]

viewsFile           = 'group/views.yaml'

allS20AdminFile    = 'group/group_s20_admin_all.yaml'
newAdminGroupToken  = '#{{ADMINGROUP}}'
newAdminGroupString = '- group.' + ID + '_admin_group'

newTempToken        = '#{{TEMP}}'

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
            
    # re-init variable
    writeFile = False
    
    # add admin_group to all s20 admin group
    with open(allS20AdminFile, 'r') as myFile:
        data = myFile.read()
        if (data.find(newAdminGroupString)) == -1:
            writeFile = True
        else:
            writeFile = False
        myFile.close()
    
    if (writeFile == True):
        with open(allS20AdminFile, 'w') as myFile:
            data = data.replace(newAdminGroupToken, newAdminGroupString + '\n      ' + newAdminGroupToken)
            myFile.write(data)
            myFile.close()
    
    # re-init variable
    writeFile = False
    
else:
    for folder in listOfFolders:
        for filename in glob.glob(autofolder + genFilePrefix +"*"):
            os.remove(filename)
        for filename in glob.glob(bsFolder + genFilePrefix +"*"):
            os.remove(filename)
        for filename in glob.glob(groupFolder + genFilePrefix +"*"):
            os.remove(filename)
        for filename in glob.glob(inFolder + genFilePrefix +"*"):
            os.remove(filename) 
        for filename in glob.glob(sensFolder + genFilePrefix +"*"):
            os.remove(filename)
        for filename in glob.glob(switchFolder + genFilePrefix +"*"):
            os.remove(filename)