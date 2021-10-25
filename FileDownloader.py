import requests
from requests.auth import HTTPBasicAuth
import tkinter.simpledialog
import os


baseStudIP_URL = "https://studip.uni-oldenburg.de"
name = "***"
password = "*******"
#LogIn_DiaLog_____________________________________________________________________________________________

#create Input diaolog for getting name and password
main = tkinter.Tk()
main.withdraw()

# getting name and password
name = tkinter.simpledialog.askstring("Kennung", "Gib deine StudIP Kennung ein:")
password = tkinter.simpledialog.askstring("Passwort", "Gib dein StudIp Passwort ein:")

#Methods__________________________________________________________________________________________________

def req(url):
    r = requests.get(url , auth=HTTPBasicAuth(name, password))
    print("Respeonse Code: " + str(r.status_code) + " for " + url)
    return r

#downloads every type of file
def downloadFile(fileID, to):
    filename = req(baseStudIP_URL + "/api.php/file/"+fileID).json()["name"]
    data = req(baseStudIP_URL + "/api.php/file/"+fileID+"/download").content
    f = open(to+"/"+filename, "wb")
    f.write(data)
    f.close()

def getFolder(folderID):
    return req(baseStudIP_URL + "/api.php/folder/"+folderID).json()


def getFileIDsNames(folder):
    ids_names = {}
    for file in folder["file_refs"]:
        name = file["name"]
        if ".pdf" in name:
            ids_names[file["id"]] = name
    return ids_names
  
def download(path, folderID):
    #download all lectures 
    if not os.path.exists(path): 
        os.mkdir(path)
    
    fileIDsNames = getFileIDsNames(
        getFolder(folderID))

    for id in fileIDsNames:
        if not os.path.exists(path+"/"+fileIDsNames[id]):
            downloadFile(id, path)

#downloading__________________________________________________________________________________________________

#G.Tech.I. ---------------------------------------------------------------------
exerciseFolderID = "8706196d8b142c6786cb5824786a433a"
#corrected_ex_fID = "683fcaae38f195009efaacacba004e19"
exercisePath = os.getcwd() + "/Informatik/GrundlagenDerTechnischenInformatik"
lecturesFolderID = "e164af0d66b1cd8e59a76005a6a76c1b"
lecturesPath = exercisePath + "/Vorlesung"

download(exercisePath+"/Uebungen", exerciseFolderID)
download(lecturesPath, lecturesFolderID)
#download(exercisePath+"/Uebungen", corrected_ex_fID)

#LinA -------------------------------------------------------------------------
exerciseFolderID = "2c796f4ed58002e38bb70277a0ff158d"
#corrected_ex_fID = ""
exercisePath = os.getcwd() + "/Mathe/LineareAlgebra"
"""
lecturesFolderID = "69c37d2bbea12e50b8703a0ff750ce0f"
lecturesPath = exercisePath + "/Vorlesung"
"""
download(exercisePath+"/Uebungen", exerciseFolderID)

#G.Teo.I. ---------------------------------------------------------------------
exerciseFolderID = "69406ddc7b229a749594121dddf0b863"
exercisePath = os.getcwd() + "/Informatik/GrundlagenDerTheoretischenInformatik"

lecturesFolderID = "188ceec1841ac9688e21e26ada464c8c"
lecturesPath = exercisePath + "/Vorlesung"

download(exercisePath+"/Uebungen", exerciseFolderID)
download(lecturesPath, lecturesFolderID)

#Informationsysteme1-------------------------------------------------------------
exerciseFolderID = "ea6ecbfb7c1cebcc42e7a70d57f4f1a1"
exercisePath = os.getcwd() + "/Informatik/Informationssysteme1/Uebungen"

folderIDs = []
for folder in getFolder(exerciseFolderID)["subfolders"]:
    folderIDs.append(folder["id"])

for fID in folderIDs:
    download(exercisePath,fID)

#Softwaretechnik1 ----------------------------------------------------------------
exerciseFolderID = "e6a900fa629924807a4fdbfd0d4e21a6"
exercisePath = os.getcwd() + "/Informatik/Softwaretechnik1/Uebungen"

folderIDs = []
for folder in getFolder(exerciseFolderID)["subfolders"]:
    folderIDs.append(folder["id"])

for fID in folderIDs:
    download(exercisePath,fID)

#Softwareprojekt ------------------------------------------------------------------
exerciseFolderID = "fb6cf91e114b4e88103f243d72df7042"
exercisePath = os.getcwd() + "/Informatik/Softwareprojekt/Uebungen"
download(exercisePath, exerciseFolderID)