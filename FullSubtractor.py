# **************************************************************************************************************************************************************************************************** #
# ****************************************************************************** 2.	To simulate Full-Subtractor Circuit  ***************************************************************************** #
# **************************************************************************************************************************************************************************************************** #
# -@ AmiLab


'''
Note-
    - **DATA VALIDATION EXCLUDED FOR BEING CHECKED AT THE TIME OF DATA INPUT**
    - All Testings have been logged into the terminal for future debuggings.
'''


# ********************************************************************** Argument / Variable Declaration (for Testing purposes) ********************************************************************** #



MSB = 0                                                         # For storing the MSB(Most Significant Bit) of the Input Signal
LSB = 1                                                         # For storing the LSB(Least Significant Bit) of the Input Signal
borrow_in = 1
bits = [MSB, LSB, borrow_in]                                               # For storing the complete(both MSB and LSB bits) Input Signal



# **************************************************************************************** Section ends here ***************************************************************************************** #


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #



# **************************************************************************** Calculation of Full-Binary Difference  ******************************************************************************** #



def fullSubtractor(bits):                                                         # For performing the Full-Binary Subtraction
    if str(bits[0]) + str(bits[1]) in ('00', '01', '10', '11'):
        return {'Borrow Out': (~ bits[0] & bits[1]) | (bits[1] & bits[2]) | ( ~ bits[0] & bits[2]), 'Difference': bits[0] ^ bits[1] ^ bits[2]}
    else:
        print('Not a Valid Binary Number')

# Testing-
bin_add = fullSubtractor(bits)
print(f'Binary_Full_Subtraction({bits[0]}, {bits[1]}, (Borrow In = {bits[2]})) =', bin_add)



# ********************************************************************************* Section ends here ************************************************************************************************ #


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #




