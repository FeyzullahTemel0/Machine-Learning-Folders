file= open("employee_revenue.txt","r")
data = file.read()
# print(data)

lines = data.splitlines()
# print(lines)

string = lines[0]
# print(string)

string = string.strip(" ")
# print(string)

string = string.lower()
# print(string)

string = string.capitalize()
# print(string)

# Split ile ilk veriyi parçalara yani indexlerine bölüyoruz.

# Bu durum istediğimiz indexteki veriye erişimimizi sağlıyor.
split_string = string.split(" ")
# print(split_string)

name = split_string[0]
# print(name)

call_number = split_string[2]
# print(call_number)

for i in split_string:
    if "$" in i :
        avarage_deal_size = i.split("$")[0]

# print(avarage_deal_size)


dollars_index = split_string.index("dollars")
# print(dollars_index)

revenue_index = dollars_index - 1
# print(revenue_index)

revenue = split_string[revenue_index]
# print(revenue)

# print("Name: ",name)
# print("Number of calls: ",call_number)
# print("Average deal size: ",avarage_deal_size)
# print("Revenue: ",revenue)


# Yukarıdaki verilerin tiplerini görmek için başlarına type ekleyerek hepsinin string tipinde olduğunu öğrenmiş olduk.
# print("Name: ",type(name))
# print("Number of calls: ",type(call_number))
# print("Average deal size: ",type(avarage_deal_size))
# print("Revenue: ",type(revenue))



# bu kısımda ise tip dönüşümleri yaptık string veri tipinde olan değişkenlerimizi int veri tipine dönüştürdük ardından dönüşümün başarılı olup olmadığını yazdırark kontrol ettik
'''avarage_deal_size = int(avarage_deal_size)
call_number = int(call_number)
revenue = int(revenue)
'''
# print("Number of calls: ",type(call_number))
# print("Average deal size: ",type(avarage_deal_size))
# print("Revenue: ",type(revenue))

names = []
call_numbers =[]
avarage_deal_sizes =[]
revenues = []

for employee in lines :
    employee = employee.strip(" ")
    employee = employee.lower()
    employee = employee.capitalize()

    split_employee= employee.split(" ")

    name = split_employee[0]
    call_number = split_employee[2]

    for i in split_employee:
        if "$" in i:
            avarage_deal_size =i
    avarage_deal_size = avarage_deal_size.split("$")[0]

    
    dollars_index = split_employee.index("dollars")
    revenue_index = dollars_index - 1
    revenue = split_employee[revenue_index]

    # avarage_deal_size = int(avarage_deal_size)
    # call_number= int(call_number)
    # revenue = int(revenue)

    # names.append(name)
    # call_numbers.append(call_number)
    # avarage_deal_sizes.append(avarage_deal_size)
    # revenues.append(revenue)

    # print("Names:",names)
    # print("Number of calls: ",call_numbers)
    # print("Average ideal sizes",avarage_deal_sizes)
    # print("Revenues: ", revenues)



names = []
call_numbers =[]
avarage_deal_sizes = []
revenues = []


def clean_extract(lines):
    for employee in lines:
        employee = employee.strip(" ")
        employee = employee.lower()
        employee = employee.capitalize()

        split_employee = employee.split(" ")

        name = split_employee[0]
        call_number = split_employee[2]

        for i in split_employee:
            if "$" in i:
                avarage_deal_size = i
                avarage_deal_size = avarage_deal_size.split("$")[0]
        dollars_index = split_employee.index("dollars")
        revenue_index = dollars_index - 1
        revenue = split_employee[revenue_index]

        avarage_deal_size = int(avarage_deal_size)
        call_number = int(call_number)
        revenue = int(revenue)

        names.append(name)
        call_numbers.append(call_number)
        avarage_deal_sizes.append(avarage_deal_size)
        revenues.append(revenue)

    return names, call_numbers, avarage_deal_sizes,revenues

names,call_numbers,avarage_deal_sizes,revenues = clean_extract(lines)
# print("Names: ",names)
# print("Number of calls: ",call_numbers)
# print("Avarage deal sizes: ",avarage_deal_sizes)
# print("Revenues: ",revenues)


# print(len(names))

IDs = list(range(0,11))
# print(IDs)
# len(IDs)



dictionary1 = dict(zip(IDs,names))
# print(dictionary1)

dictionary2 = dict(zip(revenues,names))
# print(dictionary2)


sorted_dictionary = sorted(dictionary2)[0:3]

for i in sorted_dictionary:
    print(dictionary2[i])


sorted_dictionary = sorted(dictionary2,reverse=True)[0:3]

for i in sorted_dictionary:
    print(dictionary2[i])

list1 = 'Ben,Omer,Karen'.split(" ")
print(list1.strip(" "))
list2 = [300,10,500,950,253]
dictionary1 = dict(zip(list1,list2))
print(dictionary1)