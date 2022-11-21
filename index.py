
#####################################################

#                Employee Total Salary             #

#####################################################



employeeData = {
    "Data" :[
        {
            "employeeId" : 1,
            "employeeName" : "Waqar",
            "employeeDesignation" : "Loader",
            "employeeType" :  "Daily",
            "employeeRatePerDay" : 1000,
            "totalAttendence" : 22,
            "totalDays" : 30
            
        },
         {
            "employeeId" : 2,
            "employeeName" : "Samee",
            "employeeDesignation" : "Loader",
            "employeeType" :  "Daily",
            "employeeRatePerDay" : 800,
            "totalAttendence" : 15,
            "totalDays" : 30
            
        },
         {
            "employeeId" : 3,
            "employeeName" : "Arbab",
            "employeeDesignation" : "Loader",
            "employeeType" :  "Daily",
            "employeeRatePerDay" : 1500,
            "totalAttendence" : 10,
            "totalDays" : 30
            
        }
    ]
}

my_value = input()
length = len(employeeData["Data"])
print(length)

for i in range(0 , length-1) :

    if employeeData["Data"][i]["employeeName"] == my_value:

        get_name = employeeData['Data'][i]["employeeName"]
        get_attendence = employeeData["Data"][i]["totalAttendence"]
        get_salary = employeeData["Data"][i]["employeeRatePerDay"]
        total_salary = get_attendence * get_salary
        result = f"{get_name} total salary is {total_salary}"
        print(result)
    else :
       print("Employee Name not Matched")  








#####################################################

#                Employee Daily Charges             #

#####################################################
employeeData2 = {
    "Data" :[
        {
            "employeeId" : 1,
            "employeeName" : "Waqar",
            "employeeDesignation" : "Loader",
            "employeeType" :  "Daily",
            "totalAttendence" : 22,
            "totalDays" : 30,
            "total_salary" : 20000
            
        },
         {
            "employeeId" : 2,
            "employeeName" : "Samee",
            "employeeDesignation" : "Loader",
            "employeeType" :  "Daily",
            "totalAttendence" : 10,
            "totalDays" : 30,
            "total_salary" : 12000
            
        },
         {
           "employeeId" : 2,
            "employeeName" : "Sameed",
            "employeeDesignation" : "Loader",
            "employeeType" :  "Daily",
            "totalAttendence" : 10,
            "totalDays" : 30,
            "total_salary" : 12000
            
        }
    ]
}


my_value2 = input()
length = len(employeeData2["Data"])
print(length)

for i in range(0 , length-1):
        if employeeData2["Data"][i]["employeeName"] == my_value2:
            get_name = employeeData2["Data"][i]["employeeName"]
            get_attendence = employeeData2["Data"][i]["totalAttendence"]
            get_total_salary = employeeData2["Data"][i]["total_salary"]
            result = get_total_salary / get_attendence
            daily_charges = result
            my_res = f"{get_name} daily charges is {daily_charges}"
            print(my_res)
        else :
            print("Employee Name not Matched")    






