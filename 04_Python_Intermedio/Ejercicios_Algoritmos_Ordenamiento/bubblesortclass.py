from listclass import list_sort

class BublleSort(list_sort):

    def bubble_sort_list(self):
        # i=0
        for inicialindex in range(len(self.number_list) - 1):
            # print(f'\nIteacion # {i}')
            # i+=1
            check = False
            for index in range(len(self.number_list) - 1 - inicialindex):
                actualnumber = self.number_list[index]
                nextnumber = self.number_list[index+1]
                if(actualnumber>nextnumber):
                    self.number_list[index] = nextnumber
                    self.number_list[index+1] = actualnumber 
                    check = True
                # print(f'Numero Actual {actualnumber}')
                # print(f'Numero siguiente {nextnumber}')
            if(check == False):
                break                
        return self.number_list

    def reverse_bubble_sort_list(self):
            # i=0
            for inicialindex in range(len(self.number_list) - 1,0,-1):
                # print(f'\nIteacion # {i}')
                # print(f'Inicial index {inicialindex}') #--8
                # i+=1
                check = False
                for index in range(len(self.number_list) - 1,0,-1): #--8
                    actualnumber = self.number_list[index] #--2
                    nextnumber = self.number_list[index-1] #--1
                    if(actualnumber<nextnumber):
                        self.number_list[index] = nextnumber
                        self.number_list[index-1] = actualnumber 
                        check = True
                    # print(f'Index {index}') #--0
                    # print(f'Numero Actual {actualnumber}')
                    # print(f'Numero siguiente {nextnumber}')
                if(check == False):
                    break                
            return self.number_list

    