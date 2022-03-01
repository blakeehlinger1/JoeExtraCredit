taxrate = .08

class Service:
    def __init__(self, pcharge, lcharge):
        self.__parts = pcharge
        self.__labor = lcharge
    def set_parts_charges(self,pcharge):
        self.__parts = pcharge
    def set_labor_charges(self,lcharge):
        self.__labor = lcharge 
    def get_parts_charges(self):
        return self.__parts
    def get_labor_charges(self):
        return self.__labor
    def get_sales_tax(self):
       self.__salestax = taxrate * (self.__labor + self.__parts)
       return self.__salestax

    def get_total_charges(self):
        self.__total = self.__salestax + self.__labor + self.__parts
        return self.__total