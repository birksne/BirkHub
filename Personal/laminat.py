import math

def check_cut(cut, corners, width ,threshold):
    for i, corner in enumerate(corners):
        distance = sum(corners[0:i+1]) # Getting distance from wall to current corner
        test = round((distance - cut) / width, 0)  # Taking distance - cut dividing my full width of boards
        calculated_cut = (cut + test* width) - distance # Calculating the calculated cut to fit corner

        if math.sqrt(calculated_cut**2) < threshold: # Checking if corner is leaving with cut smaller than treshold
            #print(f'Cut of {cut}cm will work on {corner} with {calculated_cut} surplus')
            return 'FAIL'

    return 'OK'


def check_correction(width, corners, threshold, correction):
    x = 0 # Setting variable for loop

    for i in range(round(width/correction)): # Creating relevant range of correction
        x =+ i*correction # Adding correction for each loop 
        test_cut = check_cut(x, corners, width, threshold) # Checking if cut pass
        
        if test_cut == 'OK': # If no fails, return successfull cut
            return f'With a {x}cm cut you should pass all corner with minimum {threshold} cm cuts!'
        else: 
            pass
    
    return 'No valid cuts found... \nTry Altering correction or threshold' # Return fail if none is found


def check_threshold(width, corners, threshold, correction, try_threshold_on_fail = False):
    
    if try_threshold_on_fail:
        new_treshold = threshold
        for i in range(threshold-1):
            new_treshold-= i
            test_threshold = check_correction(width, corners, new_treshold, correction)
            if test_threshold == 'No valid cuts found... \nTry Altering correction or threshold':
                pass
            else:
                return test_threshold
        return "It's impossible my guy..."

    else:
        return check_correction(width, corners, threshold, correction)



# Setting variables
laminat_width = 24 
corner_list = [70, 40, -17, 97, 4]

# Metadata variables: 
accepted_cut = 10
correction = 1

# Running the mf
print(check_threshold(laminat_width, corner_list, accepted_cut, correction,True))

