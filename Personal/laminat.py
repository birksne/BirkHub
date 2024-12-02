import math
from tabulate import tabulate 

class laminat:
    '''
    Function for finding all available combinations of cuts that can be.
    '''
    def __init__(self, board_width, corner_list : list, corner_type_list : list , cut_threshold : int):
        self.board_width = board_width 
        self.corner_list = corner_list
        self.corner_type_list = corner_type_list
        self.cut_threshold = cut_threshold
        self.cut = 0
        self.log = []


    def check_cut(self, cut ,threshold):
        '''
        Tests all corner with given cut
        '''
        self.log_test = []  # Reset log_test for each check
        for i, corner in enumerate(self.corner_list):
            type = self.corner_type_list[i]
            distance = sum(self.corner_list[0:i+1]) # Getting distance from wall to current corner / obsticle

            if type == 'Corner':
                test = math.ceil((distance - cut) / self.board_width )  
            elif type == 'Opposite wall':
                test = math.floor((distance - cut) / self.board_width )  

            calculated_cut = round(math.sqrt(((cut + test* self.board_width ) - distance) **2),2)
            #print(corner, type, distance, calculated_cut )

            if calculated_cut > threshold or calculated_cut < 1:  # Checking if corner is leaving with cut smaller than threshold
                self.log_test.append(f'{cut} : {corner} : {type} : {distance} : {calculated_cut}')
            else:
                # Skip failing cuts
                
        
        return 'OK' if len(self.log_test)== len(self.corner_list) else 'FAIL'  # Return OK if there are successful cuts, otherwise FAIL
            

    def check_correction(self, threshold):
        x = 0 # Setting variable for loop

        for i in range(round(self.board_width)): # Creating relevant range of correction
            x =+ i # Adding correction for each loop 

            testing_cut = self.check_cut(x, threshold) # Checking if cut pass            
            
            if testing_cut == 'OK': # If no fails, return successfull cut
                for entry in self.log_test:
                    self.log.append(entry)
            else: 
                pass
        
        return f'All cuts tested with limit of {threshold} cm from obsticle'


    def check_threshold(self, threshold):
            new_treshold = threshold
            for i in range(threshold-1):
                new_treshold = threshold - i
                print(new_treshold)
                self.check_correction(new_treshold)
                print(f'Testing with  {threshold}')
            return 


    def run(self, modify_threshold=False):
        '''
        Serving as orchestrator
        '''
        if modify_threshold:
            self.check_threshold(self.cut_threshold)
        else: 
            self.check_correction(self.cut_threshold) 
        


        headers = ["cut", "Corner", "Type", "Distance", "Calculated Obstacle Cut"]
        rows = [entry.split(" : ") for entry in self.log]
            
        print(tabulate(rows, headers=headers, tablefmt="grid"))



# Setting variables
laminat_width = 24.1
corner_list_oneway = [74, 33, -17, 119, -18, 4]
corner_type = ['Corner','Corner','Corner','Opposite wall','Corner','Corner']

corner_list_whole = [74, 33, -17, -92, 218,12,-20, 18, 4]
corner_type_whole = ['Corner','Corner','Corner','Corner','Opposite wall','Opposite wall','Opposite wall','Opposite wall','Corner']


delailed_list = [74.5, 33.1, -16.8, -92, 217.3,12.5, -20.7, 18.5, 1.5, 119.7, 53]
delailed_type = ['Corner','Corner','Corner','Corner','Opposite wall','Opposite wall','Opposite wall','Opposite wall','Corner', 'Opposite wall', 'Opposite wall']

session = laminat(laminat_width,delailed_list, delailed_type, 10)
session.run(True)

