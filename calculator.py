import numpy as np

def mean(total, num_values):
    return total / num_values

def variance(arange):
    num_values = len(arange)
    sum_values = sum(arange)
    mean = sum_values / len(arange)

    var = sum([((i-mean)**2) for i in arange]) / num_values
    
    std = np.sqrt(var)

    return f'''
    number of values = {num_values}
    sum of values = {sum_values}
    median = {mean} 
    variance = {var}
    '''

def stdd(arange):
    num_values = len(arange)
    sum_values = sum(arange)
    mean = sum_values / len(arange)

    var = sum([((i-mean)**2) for i in arange]) / num_values
    
    std = np.sqrt(var)

    return f'''
    number of values = {num_values}
    sum of values = {sum_values}
    median = {mean} 
    variance = {var} 
    Standard deviation = {std}
    '''

def outliers(arange):
    arange.sort()
    num_values = len(arange)
    sum_values = sum(arange)

    if num_values % 2:
        median = arange[int(len(arange)/2)]
        
        lower_half = arange[:int(len(arange)/2)]
        Q1 = lower_half[int(len(lower_half)/2)]
        
        upper_half = arange[int(len(arange)/2)+1:]
        Q3 = upper_half[int(len(upper_half)/2)]

        IQR = Q3 - Q1


        lower_outlier = (Q1)-(1.5*IQR)
        upper_outlier = (Q3)+(1.5*IQR)

        outlier_nums = [ i for i in arange if i < (Q1)-(1.5*IQR) or i > (Q3)+(1.5*IQR)]

        return f'The median is {median}, the Q1 is {Q1}, the Q3 is {Q3} and the IQR is {IQR}, and the outliers are {outlier_nums}'
        
    else:
        median = (arange[int(len(arange)/2)-1] + arange[int(len(arange)/2)]) / 2

        lower_half = arange[:int(len(arange)/2)-1]
        Q1 = (lower_half[int(len(lower_half)/2)] + lower_half[int(len(lower_half)/2)-1]) / 2

        upper_half = arange[int(len(arange)/2)+1:]
        Q3 = (upper_half[int(len(upper_half)/2)] + upper_half[int(len(upper_half)/2)-1]) / 2

        IQR = Q3 - Q1

        lower_outlier = (Q1)-(1.5*IQR)
        upper_outlier = (Q3)+(1.5*IQR)

        outlier_nums = [ i for i in arange if i < (Q1)-(1.5*IQR) or i > (Q3)+(1.5*IQR)]

        return f'The median is {median}, the Q1 is {Q1}, the Q3 is {Q3} and the IQR is {IQR}, and the outliers are {outlier_nums}'


if __name__ == '__main__':
    answer = input("""
    Welcome to the Statistics Caldulator
    please select an option:

        A. Mean
            NOTE: by giving the sum of the total values and the number of values.
        
        B.Variance
            NOTE: by giving the arange of values
        
        C. Standar Deviation
            NOTE: by giving the arange of values

        D. Determin the outliers from an arange
            NOTE: by giving the arange of values

    """)

    if answer == 'A'.lower():

        total = float(input('Please type the sum of the values:  '))
        num_values = int(input('Please type the number of values:  '))

        print(mean(total, num_values))

    elif answer == 'B'.lower():
        arange = input("Please enter the arange of numers separated by ',':  ").split(',')
        
        new_arange = [float(i) for i in arange]

        print(variance(new_arange))

        
    elif answer == 'C'.lower():

        arange = input("Please enter the arange of numers separated by ',':  ").split(',')
        
        new_arange = [float(i) for i in arange]

        print(stdd(new_arange))

    elif answer == 'D'.lower():

        arange = input("Please enter the arange of numers separated by ',':  ").split(',')
        
        new_arange = [float(i) for i in arange]

        print(outliers(new_arange))