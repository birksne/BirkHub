import math
from tabulate import tabulate 

class laminat:
    '''
    Function for finding all available combinations of cuts that can be.
    '''
    def __init__(self, board_width, corner_list: list, corner_type_list: list, cut_threshold: int):
        self.board_width = board_width
        self.corner_list = corner_list
        self.corner_type_list = corner_type_list
        self.cut_threshold = cut_threshold
        self.cut = 0
        self.log = []

    def check_cut(self, cut, threshold):
        '''
        Tests all corners with the given cut.
        '''
        self.log_test = []  # Reset log_test for each check
        for i, corner in enumerate(self.corner_list):
            type_ = self.corner_type_list[i]
            distance = sum(self.corner_list[0:i+1])  # Getting distance from wall to current corner/obstacle

            if type_ == 'Corner':
                test = math.ceil((distance - cut) / self.board_width)  
            elif type_ == 'Opposite wall':
                test = math.floor((distance - cut) / self.board_width)  

            calculated_cut = round(math.sqrt(((cut + test * self.board_width) - distance) ** 2), 2)

            # Only add to log if the calculated cut is within the threshold (greater than 1 and less than or equal to threshold)
            if calculated_cut >= 1 and calculated_cut <= threshold:
                self.log_test.append(f'{cut} : {corner} : {type_} : {distance} : {calculated_cut}')
        
        return 'OK' if self.log_test else 'FAIL'  # Return OK if there are successful cuts, otherwise FAIL

    def check_correction(self, threshold):
        x = 0  # Setting variable for loop

        for i in range(round(self.board_width)):  # Creating relevant range of correction
            x += i  # Adding correction for each loop 

            testing_cut = self.check_cut(x, threshold)  # Checking if cut passes            
            
            if testing_cut == 'OK':  # If no fails, return successful cut
                self.log.extend(self.log_test)  # Add only successful cuts to the main log
            else:
                pass  # Do nothing for failed cuts
        
        return f'All cuts tested with limit of {threshold} cm from obstacle'

    def check_threshold(self, threshold):
        new_threshold = threshold
        for i in range(threshold - 1):
            new_threshold -= i  # Reduce the threshold
            self.check_correction(new_threshold)
            print(f'Testing with {new_threshold}')
        return f'All cuts tested with limit of {threshold} cm from obstacle'

    def run(self, modify_threshold=False):
        '''
        Serving as orchestrator
        '''
        if modify_threshold:
            self.check_threshold(self.cut_threshold)
        else: 
            self.check_correction(self.cut_threshold) 

        # Prepare data for tabulate and display
        headers = ["Cut", "Corner", "Type", "Distance", "Calculated Obstacle Cut"]
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

