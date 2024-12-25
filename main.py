"""_Ce code est creer par Elisee ATIKPO """
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from time import *

#Debut la classe Cotisation
class Cotisation:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Cotisations")
        self.root.geometry("400x250")
        self.root.config(bg = "#000")
        
        #Bonjour ELISEE
        bjr = Label(self.root,text = "Salut Elisee !",font = ("Romance Breakin",14,"bold"),fg = "#fff",bg = "#000")
        bjr.pack()
        #Creation du frame_1
        self.frame_1 = Frame(self.root,width= 300,height= 150,bg = "#063dfa")
        self.frame_1.pack(expand=YES)
        
        # initialiser self.fen
        self.List_total = []
        
    
    def Buttons(self):
        But = ["Ajouter","Liste complete","Total"]
        self.Liste_But = []
        i,j = 0,0
        for x in But : 
            but = Button(self.frame_1,text = x,font= ("Romance Breakin",11,"bold"),bg = "#faf306")
            if x == "Total":
                but.grid(row = 1,column = 0,columnspan = 2)
            else:
                but.grid(row = i,column= j,padx = 20,pady= 20)
            but.bind("<Button-1>",lambda e,name = x : self.appui(name))
            self.Liste_But.append(but)
            j+=1
    
    def appui(self,txt):
        dic = {"Ajouter" : self.ajouter,"Liste complete" : self.Liste_complete , "Total" : self.toto}
        do = dic.get(txt)
        do()
    
    def toto(self):
        self.totols = Tk()
        self.totols.title("Total")
        
        for i in range(len(self.List_total)):
            if self.List_total[i] != None:
                    self.List_total[i].destroy()
            self.List_total.pop(i)
            
        self.List_total.append(self.totols)
        
        Label(self.totols,text = "Voici le total M.Elisee : ",font = ("Romance Breakin",12,"bold")).pack()
        Label(self.totols,text = f"   T = {self.total()}",font = ("Romance Breakin",12,"bold")).pack()
        self.totols.mainloop()
    def ajouter(self):
            self.aj = Tk()
            
            for i in range(len(self.List_total)):
                if self.List_total[i] != None:
                    self.List_total[i].destroy()
                self.List_total.pop(i)
            
            self.List_total.append(self.aj)
            
            self.Ents = []
            self.aj.title("Ajouter")
            
            Fair = ["Nom : ","Mottant : "]
            for x in Fair : 
                Label(self.aj,text = x,font = ("Romance Breakin",12,"bold")).pack()
                Ent = Entry(self.aj,fg = "#888",font = ("Romance Breakin",12,"bold"))
                Ent.insert(0,x)
                Ent.pack()
                Ent.bind("<FocusIn>",lambda e , fen = Ent,txt = x : self.cursor_in(fen,txt))
                Ent.bind("<FocusOut>",lambda e , fen = Ent,txt = x : self.cursor_out(fen,txt))
                lab = Label(self.aj)
                lab.pack()
                self.Ents.append((Ent,lab))
            
            self.frame_2 = Frame(self.aj)
            self.frame_2.pack()
            ii , jj = 0,0
            but = Button(self.frame_2,text = "Quiter",font= ("Romance Breakin",11,"bold"),bg = "#f00",command = self.aj.destroy)
            but.grid(row= ii,column= jj)
            jj += 1
            but = Button(self.frame_2,text = "Ajouter",font= ("Romance Breakin",11,"bold"),bg = "#063dfa",command = self.effectuer_ajout)
            but.grid(row= ii,column= jj)
            
            jj += 1
            
            self.aj.mainloop()
    
    def Liste_complete(self):
        self.Liste = Tk()
        self.Liste.title("Liste Complete")
        
        for i in range(len(self.List_total)):
            if self.List_total[i] != None:
                    self.List_total[i].destroy()
            self.List_total.pop(i)
            
        self.List_total.append(self.Liste)
        
        #------------------ Presentation ---------
        Lab = Label(self.Liste,text = "Voici la liste Complete M.Elisee : ",font = ("Romance Breakin",15,"bold"))
        Lab.pack()
        #----------------------------------------
        
        #------------------ Creation d'un tree ---------
        self.Tree = ttk.Treeview(self.Liste,columns=(1,2,3,4),show ='headings')
        self.Tree.pack()
        
        #------- Definition des entres ------------
        self.Tree.heading(1,text = "ID :")
        self.Tree.heading(2,text = "Date :")
        self.Tree.heading(3,text = "Name :")
        self.Tree.heading(4,text = "Mottant :")
        #-----------------------------------------
        #------------- Redimentionnement -------
        self.Tree.column(1,width = 50)
        self.Tree.column(2,width = 150)
        self.Tree.column(3,width = 150)
        self.Tree.column(4,width = 150)
        #----------------
        #----------- Copier le contenu dans "tous" -----
        with open("/home/elisee/Bureau/Gestion_des_cotisations/cotisation.txt","r") as fil : 
            tous = fil.read()
        #---------------------------------------
        #------------Inserer les valeurs ---------
        nbr = 1
        for elmt in tous.split("\n") :
            elmt = elmt.split("!!!")
            if len(elmt) > 1:
                self.Tree.insert("",END,values=(nbr,elmt[0],elmt[1],elmt[2]))
                nbr += 1
        #------------------------------------------
                
       
        self.Liste.mainloop()
    def effectuer_ajout(self):
        do = True
        name , mottant = self.Ents[0][0].get(),self.Ents[1][0].get()
        if name == "Nom : ":
            name = ""
        
        if mottant == "Mottant : ":
             mottant = ""
        
        ent = [name,mottant] 
        for x,y in zip(self.Ents,ent):
            if y == '':
                x[1].config(text = "Ce Champ est Vide !",fg = "#f00")
                do = False
        if do :
            dates = strftime("%D")
            with open("/home/elisee/Bureau/Gestion_des_cotisations/cotisation.txt","r") as fil:
                tous = fil.read()
            
            #Valeur a inserer
            add = dates +"!!!" +name + "!!!" + mottant
            #Transformer tous en liste
            tous = tous.split("\n")
            for i in range(len(tous)-1):
                if len(tous[i] ) < 6:
                    tous.pop(i)  #Supprimer les elements vides
            #Mottant qui se fait ajouter
            prix = int(mottant)
            aj = False #Verifier si l'ajoute a ete effectue
            for i in range(len(tous)):
                if tous[i] != "":
                    val = int(tous[i].split("!!!")[-1])
                    if prix > val and not aj:
                        tous.insert(i,add)
                        aj = True
            
            if not aj:
                tous.append(add)  
                    
            tous = "\n".join(tous)
            
            with open("/home/elisee/Bureau/Gestion_des_cotisations/cotisation.txt","w") as fil:
                val = fil.write(tous)
            if val != 0 :
                showinfo("Info","Operation Reussi !") 
    def total(self):
        with open("/home/elisee/Bureau/Gestion_des_cotisations/cotisation.txt","r") as fil:
                tous = fil.read()
        tous = tous.split("\n")
        self.total_prix = 0
        for x in tous:
            if x!= "":
                val = int(x.split("!!!")[-1])
                self.total_prix += val
        
        return self.total_prix
    def cursor_in(self,fen,txt):
        for x in self.Ents : 
            if x[0] == fen :
                x[1].config(text = "")
        if fen.get() == txt : 
            fen.delete(0,'end')
            fen.config(fg = "#000")
    
    def cursor_out(self,fen,txt):
        if fen.get() == '':
            fen.config(fg = "#888")
            fen.insert(0,txt)
    
    def finish_principal(self):
        self.root.mainloop()
        #self.conn.close()
        

fen = Tk()
cot = Cotisation(fen)
cot.Buttons()
cot.finish_principal()

#Fin du code