class Student:
    """def __init__(self, identification,gender,salary,job,name,age,zone,city):
        self.identification=identification
        self.gender=gender
        self.salary=salary
        self.job=job
        self.name=name
        self.age=age
        self.zone=zone
        self.city=city"""

    def __init__(self, my_dict):
        if self.validate_datas(my_dict)==True:
            for key in my_dict:
                setattr(self,key, my_dict[key])
        else:
            raise Exception("Debe de diligenciar todos los datos, para agregar el estudiante")

    def validate_datas(self, my_dict):
        atributes=["identification", "gender", "salary", "job", "name", "age", "zone", "city"]
        keys=list(my_dict.keys())
        return keys == atributes





