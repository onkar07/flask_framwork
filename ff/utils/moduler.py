import os

fixedDir = ['auth', 'utils', '__pycache__']

def getDir():
    # folder path
    dir_path = r'./'
    moduleArray = []
    # list to store files
    res = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        # if os.path.isfile(os.path.join(dir_path, path)):
        #     res.append(path)
        if os.path.isdir(os.path.join(dir_path, path)):
            res.append(path)
    projectNameDirectory = []
    for ele in res:
        if(ele not in fixedDir):
            projectNameDirectory.append(ele)
    
    insideDir = []
    for directory in projectNameDirectory:
        dir_path = os.path.join(directory)
        for path in os.listdir(directory):
        # check if current path is a file
            if os.path.isdir(os.path.join(dir_path, path)):
                insideDir.append(path)
                
    for itm in insideDir:
        path = './'+projectNameDirectory[0]+'/'+itm+'/module.py'
        try:
            file = open(path, 'r').read()
            exec(file)
        except Exception as e:
            print(e)