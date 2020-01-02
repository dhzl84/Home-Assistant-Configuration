import sys  # needed to use arguments

NAME = sys.argv[1]
ID = NAME.lower()
ID = ID.replace(' ', '_')

print('NAME: ' + NAME)
print('ID: ' + ID)

genFilePrefix = 'th_'

templateFolder = 'templates/'

autoFileTemplate = templateFolder + 'thermo_automation_template.yaml'
autofolder = 'automation/'
autoFile = autofolder + genFilePrefix + 'automation_' + ID + '.yaml'

listOfTemplates = [autoFileTemplate]
listOfNewFiles = [autoFile]
listOfFolders = [autofolder]
writeFile = False

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
