from PyQt5 import QtWidgets, uic,QtCore
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
import sys
from pathlib import Path
import data as dataReader
import numpy as np
from algorithme_genetique import genetic
from algo_genetique_recherche_locale import genetic_rt
from neh import neh
from cds import CDS,plotGantt
from Simulated_annealing import simulated_annealing
from makespan import makespan
from time import time
from random import shuffle, randrange, sample, random

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('PROJET OPTIM')
        self.show()
        self.cds.clicked.connect(self._cds)
        self.genetic.clicked.connect(self._genetic)
        self.neh.clicked.connect(self._neh)
        self.recuit.clicked.connect(self._recuit)
        self.hybrid.clicked.connect(self._hybrid)
    def openDiag(self,method):
        self.diag=SelectFile(method)
        self.close()
        self.diag.show()
    def _branch_and_bound(self):
        self.openDiag('B&B')
    
    def _cds(self):
        self.openDiag('CDS')
    def _neh(self):
        self.openDiag('NEH')
    def _genetic(self):
        self.openDiag('GENETIC')
    def _recuit(self):
        self.openDiag('RECUIT')
    def _hybrid(self):
        self.openDiag('HYBRID')
class SelectFile(QtWidgets.QDialog):
    def __init__(self,method):
        QtWidgets.QDialog.__init__(self)
        uic.loadUi('fileSelect.ui', self)
        self.method=method
        self.setWindowTitle(method)
        self.file.clicked.connect(self.showDiag)
        self.exec.clicked.connect(self.run)
        self.back.clicked.connect(self.backHome)
        self.exec.setEnabled(False)

    def closeEvent(self, event):
        self.ui=Ui()
        self.ui.show()
    def showDiag(self):
        home_dir = str(Path.cwd())+'/data'
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir,'Text Files ( *.txt)')
        if fname[0]:
            self.input.setText(fname[0])
            print(fname[0])
            if '/data/ta20_5_1.txt' in fname[0]:
                nbLignes = 5
            elif  '/data/ta20_20_1.txt' in fname[0]:
                nbLignes = 20
            elif '/data/ta100_10_1.txt' in fname[0]:
                nbLignes = 10
            #Load the file and check if valid
            matrice = dataReader.read(fname[0], nbLignes)
            matrice = np.array(matrice)
            machine_count, job_count = matrice.shape
            #Display infos about job count ...
            self.label.setText('{} machines et {} jobs'.format(machine_count, job_count))
            #Set the data as class var
            self.data=matrice
            #enable the execution button
            self.exec.setEnabled(True)

    def run(self):
        machine_count, job_count = self.data.shape
        if self.method=="B&B":
            #do somethign
            print('BB')
            print(self.data)
        elif self.method=="CDS":
            start = time()
            result = CDS(self.data)
            end = time()
            self.label.setText(bend(50,'{}\nOrdre : {}\nMakespan : {}\nTemps d\'execution : {:.6}s'.format(self.label.text(),result[0],result[1],end - start)))
            plotGantt(self.data,result[0],"CDS",job_count)
        elif self.method=="NEH":
            start = time()
            result = neh(self.data)
            end = time()
            self.label.setText(bend(50,'{}\nOrdre : {}\nMakespan : {}\nTemps d\'execution : {:.6}s'.format(self.label.text(),result[0],result[1],end - start)))
            plotGantt(self.data,result[0],"NEH",job_count)
        elif self.method=="GENETIC":
            population_size = 50
            # Generer une les individus de la population aleatoirement
            initPop = [sample(list(range(0, job_count)), job_count) for _ in range(0, population_size)] # same repeated individual
            start = time()
            result = genetic(self.data, initPop, population_size, 0.1, 200)
            end = time()
            self.label.setText(bend(50,'{}\nOrdre : {}\nMakespan : {}\nTemps d\'execution : {:.6}s'.format(self.label.text(),result[0],result[1],end - start)))
            plotGantt(self.data,result[0],"Genetic",job_count)
        elif self.method=="RECUIT":
            start = time()
            result = simulated_annealing(self.daa, Ti = 790,Tf = 3 ,alpha = 0.93)
            end = time()
            self.label.setText(bend(50,'{}\nOrdre : {}\nMakespan : {}\nTemps d\'execution : {:.6}s'.format(self.label.text(),result[0],result[1],end - start)))
            plotGantt(self.data,result[0],"Genetic",job_count)
        elif self.method=="HYBRID":
            population_size = 50
            # Generer une les individus de la population aleatoirement
            initPop = [sample(list(range(0, job_count)), job_count) for _ in range(0, population_size)] # same repeated individual
            start = time()
            result = genetic_rt(self.data, initPop, population_size, 0.1, 200)
            end = time()
            self.label.setText(bend(50,'{}\nOrdre : {}\n Makespan : {}\nTemps d\'execution : {:.6}s'.format(self.label.text(),result[0],result[1],end - start)))
            plotGantt(self.data,result[0],"Hybrid",job_count)

    def backHome(self):
        self.ui=Ui()
        self.ui.show()


            
def bend(w, s):
    s = s.split(" ") #creates list of all the words (any sequence between characters)
    lst = filter(None, s) # removes the repeated spaces from list
    new_lst = [""]
    i = 0
    for word in lst:
        line = new_lst[i] + " " + word #possible line
        if(new_lst[i] == ""): #first time is different
            line = word
        if(len(word)  > w): #splits words that are too large
            while(len(word)  > w):
                new_lst.append(word[:w])
                i += 1
                word = word[w:]
            i += 1
            new_lst.append(word)
        elif(len(line) > w):
           new_lst.append(word) #line length reached, start new line
           i += 1        
        else:
            new_lst[i] = line
    return "\n".join(new_lst)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()