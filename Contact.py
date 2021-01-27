import random
import math
import os
from tkinter import Tk, Text, Button, Label, messagebox


class Hash:
    __data=[] #hash table<Contact>

    def __init__(self):#Cunstructor
        self.a = random.randint(0, 200) / random.randint(200, 1000)#a<random double>
        for i in range(0,10000):#filling hash table with None
            self.__data.append(None)

    def hashCode(self,id):#hashCode
        index=math.floor((id*self.a)*10000)
        return index
    #insert into hash table
    #It get a key for id by using hashcode(),then it had filled it will put it in one of next buckets
    def insert(self,name,number,sex,address,codee,email,id):
        index=self.hashCode(id)#key
        while(self.__data[index]!=None or self.__data[index]==Contact("deleted","","","","","","")):
            index+=index
        self.__data[index]=Contact(name,number,sex,address,codee,email,id)#put in hash table

    #it takes the key and return the contact
    #if key isn't same with that bucket,it will search in next buckets untill the bucket isn't None
    def getContact(self,id):
        index=self.hashCode(id)
        c=self.__data[index]
        while c.id!=id:
            index+=1
            if self.__data[index]==None:
                return None
        return self.__data[index]
    #delet from hash table
    def delete(self,id):
        i=self.getContact(id)
        i=Contact("deleted","","","","","","")

class Tyre:
    def __init__(self,type):#Contructor
        self.arr={}#arr
        self.type=type#26 or 9
        if type==26:
            self.words=[chr(i) for i in range(97,123)]
        else:
            self.words=[str(i) for i in range(0,10)]
        self.data=None
    #insert
    #recresive
    def insert(self,st,id):

        if len(st)==0:
            if self.data==None:
                return self
            else:
                return False
        else:
            s=st[0]
            index=self.words.index(s.lower())
            if self.arr.get(index)==None:
                self.arr[index]=Tyre(self.type)
            return self.arr.get(index).insert(st[1:],id)
    #delete
    def delete(self,name,hash,tree,r):
        if len(name) == 0:
            if self.data!= None:
                tree.arr.pop(self.words.index(r.lower()))
                return hash.getContact(self.data)
            else:
                return False
        else:

            s = name[0]
            index = self.words.index(s.lower())
            if self.arr.get(index) == None:
                return False
            if self.data!=None:
                b=s.lower()
                tr=self
            else:
                b=r.lower()
                tr=tree
            return self.arr.get(index).delete(name[1:],hash,tr,b.lower())
    #search
    def search(self,name,hash,flag):

        if len(name) == 0:
            if flag:
                self.printer(hash)
            else:

                if self.data!= None:
                    return hash.getContact(self.data)
                else:
                    return "not found"
        else:

            s = name[0]
            index = self.words.index(s.lower())
            if self.arr.get(index) == None:
                return "not found"
            return self.arr.get(index).search(name[1:],hash,flag)
   #print under tree
    def printer(self,hash):
        if self.data!=None:
            if self.type==26:
                print(hash.getContact(self.data).getName())
            else:
                print(hash.getContact(self.data).getNumber())
        for i in self.arr:
            self.arr[i].printer(hash)

class Contact:

    id=""  #id
    __name=""  #name
    __number="" #number
    __sex=""  #sex
    __address="" # sex\
    __email=""
    __codee="" #code

    #Constructor
    def __init__(self,name,number,sex,address,codee,email,id):
        self.__name=name
        self.__number=number
        self.__sex=sex
        self.id=id
        self.__email=email
        self.__address=address
        self.__codee=codee
    #name getter
    def getName(self):
        return self.__name
    #number getter
    def getNumber(self):
        return self.__number
    #sex getter
    def getSex(self):
        return self.__sex
    #name setter
    def getEamil(self):
        return self.__email
    def setEmail(self,email):
        self.__email=email
    def setName(self,name):
        self.__name=name
        #number setter
    def setNumber(self,number):
        self.__number=number
        #sex stter
    def setSex(self,sex):
        self.__sex=sex
        #address setter
    def setAddress(self,address):
        self.__address=address
        #code stter
    def setCodee(self,codee):
        self.__codee=codee
    #toString
    def __str__(self):
        return " ".join([self.__name,self.__number,self.__sex,self.__address,self.__codee,self.__email])
#main class tharimcludes tow Tyre tress and hash
class PhoneBook:
    #Cunstroctor
    def __init__(self):
        self.id=0
    __sexes=("man","woman")
    __names=Tyre(26)#names
    __numbers=Tyre(9)#number
    __hash=Hash()#hash
    #add contact
    def espN(self,name):
        return self.__names.search(name,self.__hash,False)

    def espNu(self, number):
        return self.__numbers.search(number, self.__hash, False)
    def newContact(self,name,number,sex,address,codee,email):
        if sex in self.__sexes:
            f7=self.__names.search(name,self.__hash,False)#check that name isn't same
            f8=self.__numbers.search(number,self.__hash,False)#check that number isn't same
            if f7=="not found"  and f8=="not found":#ok
                f1 = self.__names.insert(name, self.id)#insert name into tyre of name
                f2 = self.__numbers.insert(number, self.id)#insert number into tyre of numbers
                f1.data=self.id
                f2.data=self.id
                self.__hash.insert(name,number,sex,address,codee,email,self.id)#insert into hash table
                self.id+=1
                return name+" added succsessfully!!!"
            else:
                answer=""
                if f7!="not found":
                  answer+="name already exist!\n"
                if f8!="not found":
                   answer+= "number already exist!"
                return  answer

        else:
            print("invalid sex")#sex should be man or woman

    #take the name and delete
    def delteByName(self,name):
         f1=self.__names.delete(name, self.__hash, self.__names, name[0])
         if f1!=False:
            self.__numbers.delete(f1.getNumber(), self.__hash, self.__numbers, f1.getNumber()[0])
            self.__hash.delete(f1.id)
            return True
         else:
             return False


    #takes the number and delete
    def delteByNumber(self, number):
        f1 = self.__numbers.delete(number, self.__hash, self.__numbers, number[0])
        if f1 != False:
            self.__names.delete(f1.getName(), self.__hash, self.__names, f1.getName()[0])
            self.__hash.delete(f1.id)
            return True
        else:
            return False
    #show detal of contact by searching by name
    def showContactByName(self,name):
        return self.__names.search(name, self.__hash,True)

    # show detal of contact by searching by number
    def showContactByNumber(self,number):
        return self.__numbers.search(number, self.__hash,True)
    #edits name
    def editName(self,c):

            name=c.getName()
            newN=input("please enter new name")
            c.setName(newN)
            self.__names.delete(name,self.__hash,self.__names,name[0])
            self.__names.insert(newN,c.id).data=c.id
    #edits number
    def editNumber(self,c):

        newN=input("please enter new number")
        number=c.getNumber()
        c.setNumber(newN)
        self.__numbers.delete(number,self.__hash,self.__numbers,number[0])
        self.__numbers.insert(number,c.id).data=c.id
    #edits sex
    def editSex(self,c):
        newS = input("please enter new sex")
        c.setSex(newS)
    #edits code
    def editCodee(self,c):
        newC = input("please enter new sex")
        c.setCodee(newC)
    #edits address
    def editAddress(self, c):
        newC = input("please enter new address")
        c.setAddress(newC)
    def editEmail(self,c):
        newC = input("please enter new email")
        c.setEmail(newC)
    #searches the contact by name.if it be found and suggestsome choices to change
    def editByName(self,name):
        c = self.__names.search(name, self.__hash,False)
        if c != "not found":
            l=input("1)Edit name  2)Edit number  3)Edit sex  4)Edit address  5)Edit code 6)Edit Email\n")
            if l=="1":
               self.editName(c)
            if l=="2":
                self.editNumber(c)
            if l=="3":
                self.editSex(c)
            if l=="4":
                self.editAddress(c)
            if l=="5":
                self.editCodee(c)
            if l=="6":
                self.editEmail(c)
            return "Edited successfully!!!"
        else:
            return  "not found"

    # searches the contact by number.if it be found and suggestsome choices to change
    def editByNumber(self,number):
        c = self.__numbers.search(number, self.__hash,False)
        if c != "not found":
            l = input("1)Edit name  2)Edit number  3)Edit sex  4)Edit address  5)Edit code 6)Edir Email\n")
            if l == "1":
                self.editName(c)
            if l == "2":
                self.editNumber(c)
            if l == "3":
                self.editSex(c)
            if l == "4":
                self.editAddress(c)
            if l == "5":
                self.editCodee(c)
            if l=="6":
                self.editEmail(c)
            return "Edited successfully!!!"
        else:
            return "nor found"
#man function

def main():
    clear=lambda: os.system("cls")
    ph=PhoneBook()
    sc=" "
    while sc!="5":
        sc=input("Please choose:\n1)Add contact\n2)Delete Contact\n3)Edit contact\n4)Search contact\n5)end\n")
        clear()
        if sc=="1":#add contact
            l=input("Please enter details as:name number sex address code email\n").split(" ")
            print(ph.newContact(l[0], l[1], l[2],l[3],l[4],l[5]))

        if sc=="2":#delete contact
            l=input("1)delete by name   2)delete by number\n")
            if(l=="1"):#by name
                t=ph.delteByName(input("please enter the name:\n"))
                if t:
                    print("user deleted!!")
                else:
                    print("user not found to delete!!")
            else:#by number
                t=ph.delteByNumber(input("please enter the number:\n"))
                if t:
                    print("user deleted!!")
                else:
                    print("user not found to delete!!")

        if sc=="3":#edit contact
            if(input("1)Find by name and eidt\n2)Find by number and edit\n")=="1"):#by name
                print(ph.editByName(input("please enter the name\n")))
            else:#by number
                print(ph.editByNumber(input("please enter the number\n")))
        if sc=="4":#search
                    if input("1)search by name   2)search by number") == "1":  # by name
                        root = Tk()
                        txt = Text(root, width="5", height="5")
                        txt.pack()

                        def tmp(event):
                            if repr(event.char) == '\'\\r\'':#enter key
                                ms = ph.espN(txt.get("1.0", "end-1c"))
                                if ms != None:
                                    print(ms)
                                    if ms!="not found":#if it found the user suggest to edit
                                        if input("Do you want to edit ?yes/no")=="yes":
                                            l = input(
                                                "1)Edit name  2)Edit number  3)Edit sex  4)Edit address  5)Edit code 6)Edit Email\n")
                                            if l == "1":
                                                ph.editName(ms)
                                            if l == "2":
                                                ph.editNumber(ms)
                                            if l == "3":
                                                ph.editSex(ms)
                                            if l == "4":
                                                ph.editAddress(ms)
                                            if l == "5":
                                                ph.editCodee(ms)
                                            if l == "6":
                                                ph.editEmail(ms)
                                            print( "Edited successfully!!!")
                            else:
                                if repr(event.char) != '\'0\\x86\'':#backspace
                                    ph.showContactByName(txt.get("1.0", "end-1c") + event.char)
                                else:
                                    ph.showContactByName(txt.get("1.0", "end-2c"))

                        txt.bind('<Key>', tmp)

                        root.mainloop()
                    else:#search by number
                        root = Tk()
                        txt = Text(root, width="5", height="5")
                        txt.pack()

                        def tmp(event):
                            if repr(event.char) == '\'\\r\'':#enter preesed
                                ms = ph.espNu(txt.get("1.0", "end-1c"))
                                if ms != None:
                                    print(ms)
                                    if ms!="not found":#if it found the user suggest to edit
                                        if input("Do you want to edit ?yes/no") == "yes":
                                            l = input(
                                                "1)Edit name  2)Edit number  3)Edit sex  4)Edit address  5)Edit code 6)Edit Email\n")
                                            if l == "1":
                                                ph.editName(ms)
                                            if l == "2":
                                                ph.editNumber(ms)
                                            if l == "3":
                                                ph.editSex(ms)
                                            if l == "4":
                                                ph.editAddress(ms)
                                            if l == "5":
                                                ph.editCodee(ms)
                                            if l == "6":
                                                ph.editEmail(ms)
                                            print("Edited successfully!!!")
                            else:
                                if repr(event.char) != '\'0\\x86\'':
                                    ph.showContactByNumber(txt.get("1.0", "end-1c") + event.char)
                                else:
                                    ph.showContactByNumber(txt.get("1.0", "end-2c"))

                        txt.bind('<Key>', tmp)
                        root.mainloop()
main()#start my programm!!

