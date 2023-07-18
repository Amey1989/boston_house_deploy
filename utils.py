import numpy as np
import pickle


class hpp():
    def __init__(self,data):
        self.data = data

    def load_model(self):
        with open('model.pickle','rb') as file:
            self.model = pickle.load(file)

    def predict(self):

        self.load_model()   # above fuction call kele aahe

        CRIM= float(self.data['CRIM'])
        ZN= float(self.data['ZN'])
        INDUS= float(self.data['INDUS'])
        CHAS= float(self.data['CHAS'])
        NOX= float(self.data['NOX'])
        RM= float(self.data['RM'])
        AGE= float(self.data['AGE'])
        DIS= float(self.data['DIS'])
        RAD= float(self.data['RAD'])
        TAX= float(self.data['TAX'])
        PTRATIO= float(self.data['PTRATIO'])
        B= float(self.data['B'])
        LSTAT= float(self.data['LSTAT'])

        array = np.array([CRIM ,ZN ,INDUS ,CHAS ,NOX ,RM ,AGE ,DIS ,RAD ,TAX ,PTRATIO ,B ,LSTAT ,],ndmin = 2)
        print(array)
        print("*"*50)

        res = np.round(self.model.predict(array),2)[0]    # yethe ans he array([33.5]) ase yete so aatil list [33.5] yachi index 0 aahe so we give [0]
        print(res)
        return res