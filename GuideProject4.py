names = ['Ben','Omer','Karen','Celine','Sue','Bora','Rose','Ellen','Bob','Taylor','Jude']
call_number = [300,10,500,70,100,100,600,800,200,450,80]
average_deal_size =[8,6,24,32,5,25,25,40,15,10,12]
revenues = [2400,60,12000,2775,500,770,4000,6000,800,1200,500]

import numpy as np 

data = np.array([],dtype=int)

def append_names(names_list):
    global data
    for i in names_list:
        data = np.append(data,names.index(i))


def append_performance_measures(feature_list):
    global data 
    data = np.append(data,feature_list)


append_names(names)
append_performance_measures(call_number)
append_performance_measures(average_deal_size)
append_performance_measures(revenues)

print(data)
print(data.shape)

data = data.reshape(4,11)

print(data)
print(data.shape)

print(data[0])

print(data[1])

print(data[2])

print(data[3])

#ellen
print(data[3,7])



def calculate_performance(employee_name):
    idx = names.index(employee_name)
    number_of_calls = data[1,idx]
    avg_deal_size = data[2,idx]
    revenue= data[3,idx]

    score=(avg_deal_size*revenue)/number_of_calls

    return score


print(calculate_performance("Ellen"))

performance_scores = []
for name in names:
    score = int(calculate_performance(name))
    performance_scores.append(score)

data = np.concatenate((data,[performance_scores]),axis = 0)

print(data)


idx_best_employee = np.argmax(data[4])
idx_worst_employee =np.argmin(data[4])

print(f'Best Performing Employee: {names[idx_best_employee]}')
print(f'Worst Performing Employee: {names[idx_worst_employee]}')


a1 = np.array([1,4,8,6,2])
a2 = np.array([[11,44,88,66,22,],[22,10,47,60,5]])
array= np.array([a1.sum(),a2.ndim,a2.size,a1.argmax(),a2.argmin()])
print(array)
