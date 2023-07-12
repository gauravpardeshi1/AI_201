employees=[

    {"name":"john","salary":3000,"designation":"developer"},
     {"name":"Emma","salary":4000,"designation":"manager"},
      {"name":"kelly","salary":3500,"designation":"tester"}

]





def max_salary_employee(employees): 
    max_salary_e=None
    max_salary=None
    
    for el in employees:
    if el['salary'] >  max_salary :
        max_salary=el['salary']
        max_salary_e=el
    
    return max_salary_e   

ans=max_salary_employee(employees)  

print(ans)