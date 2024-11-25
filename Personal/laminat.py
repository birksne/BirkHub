import math

class laminat:
    def __init__(self, board_width, corner_list : list, corner_type_list : list , cut_threshold : int):
        self.board_width = board_width 
        self.corner_list = corner_list
        self.corner_type_list = corner_type_list
        self.cut_threshold = cut_threshold
        self.cut = 0
        self.log = []


    def check_cut(self, cut ,threshold):
        for i, corner in enumerate(self.corner_list):
            type = self.corner_type_list[i]
            distance = sum(self.corner_list[0:i+1]) # Getting distance from wall to current corner / obsticle

            if type == 'Corner':
                test = math.ceil((distance - cut) / self.board_width )  
            elif type == 'Opposite wall':
                test = math.floor((distance - cut) / self.board_width )  

            calculated_cut = math.sqrt(((cut + test* self.board_width ) - distance) **2)
            print(corner, type, distance, calculated_cut )

            if calculated_cut > threshold or calculated_cut < 1: # Checking if corner is leaving with cut smaller than treshold
                self.log.append(f'{corner} : {type} : {distance} : {calculated_cut}')

            else:
                return 'FAIL'
        return 'OK'        

        


    def check_correction(self, threshold):
        x = 0 # Setting variable for loop

        for i in range(round(self.board_width)): # Creating relevant range of correction
            x =+ i # Adding correction for each loop 
            
            test_cut = self.check_cut(x, threshold) # Checking if cut pass            
            if test_cut == 'OK': # If no fails, return successfull cut
                self.cut = x
                return 'OK'
            else: 
                self.log = []
                pass
        
        return 'FAIL' # Return fail if none is found


    def check_threshold(self, threshold):
            new_treshold = threshold
            for i in range(threshold-1):
                new_treshold-= i
                test_threshold = self.check_correction( new_treshold)
                if test_threshold == 'FAIL':
                    pass
                else:
                    self.cut_threshold = new_treshold
                    return 'OK'
            return "It's impossible my guy..."


    def run(self, modify_threshold=False, return_log=True):
        '''
        Serving as orchestrator
        '''
        if modify_threshold:
            status = self.check_threshold(self.cut_threshold)
        else: 
            status = self.check_correction(self.cut_threshold) 
        
        if status == 'OK' and return_log:
            print(f'\nCut: {self.cut}\nMin cut: {self.cut_threshold}\n\nLog:')
            for i in self.log:
                print(i)
        elif status == 'OK' and not(return_log):
            print(f'\nCut: {self.cut}\nMin cut: {self.cut_threshold}')
        
        else:
            print('\nUnable to find any cuts with current attributes\n')




# Setting variables
laminat_width = 24.1
corner_list_oneway = [74, 33, -17, 119, -18, 4]
corner_type = ['Corner','Corner','Corner','Opposite wall','Corner','Corner']

corner_list_whole = [74, 33, -17, -92, 218,12,-20, 18, 4]
corner_type_whole = ['Corner','Corner','Corner','Corner','Opposite wall','Opposite wall','Opposite wall','Opposite wall','Corner']

session = laminat(laminat_width,corner_list_oneway, corner_type, 10)
session.run(True, True)

