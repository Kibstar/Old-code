import csv, os

loc = r'C:\Users\jackk\Documents\Python\CSV_READER'

os.chdir(loc)

class Job:

    material_costs = {
        'RGD515':965,
        'RGD450':300,
        'RGD531':1004,
        'SUP706':300,
    }

    def __init__(self,mat1,mat2,mat3,sup,date,user,duration):
        self.mat1 = mat1
        self.mat2 = mat2
        self.mat3 = mat3
        self.sup = sup
        self.date = date
        self.user = user
        self.duration = duration
        self.project = 'Enter project here'
        self.get_costs()

    def get_costs(self):
        total = 0
        for i in self.material_costs.items():
            for j in self.mat1.items():
                if i[0].lower() == j[0].lower():
                    mat_cost = (int(i[1]) / 3600) * (float(j[1]))
                    total += mat_cost
                    mat_cost = 0
        
        for i in self.material_costs.items():
            for j in self.mat2.items():
                if i[0].lower() == j[0].lower():
                    mat_cost = (int(i[1]) / 3600) * (float(j[1]))
                    total += mat_cost
                    mat_cost = 0        

        for i in self.material_costs.items():
            for j in self.mat3.items():
                if i[0].lower() == j[0].lower():
                    mat_cost = (int(i[1]) / 3600) * (float(j[1]))
                    total += mat_cost
                    mat_cost = 0

        for i in self.material_costs.items():
            for j in self.sup.items():
                if i[0].lower() == j[0].lower():
                    mat_cost = (int(i[1]) / 3600) * (float(j[1]))
                    total += mat_cost
                    mat_cost = 0
        self.price = round(total,2)

    def __str__(self):
        return f'''User: {self.user}\nDate: {self.date}\nCost: £{self.price}\n'''



job_list =[]

with open('job_history.csv','r') as f:
    csv_reader = csv.reader(f, delimiter = ';')

    line_no = 0
    for line in csv_reader:
        if line_no == 0:
            line_no +=1
            continue
        else:
            job_inst = Job(
                user=line[3],
                mat1={line[11]:line[12]},
                mat2={line[13]:line[14]},
                mat3={line[15]:line[16]},
                sup={line[17]:line[18]},
                duration=line[7],
                date=line[4]
                )
            job_list.append(job_inst)
            line_no += 1

for i in job_list:
    print(i)