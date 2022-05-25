from datetime import date

from numpy import double, void


class User:
    #Atributos
    UserId : int
    Password : str
    RegisterDate : date
    #Metodos
    def Login(self):
        void
#===================================================

class Administrator(User):
    #Atributos
    User : User
    Name : str
    Email : str
    #Metodos
    def UpdateProductos(self):
        void
#===================================================

class Customer(User):
    #Atributos
    User : User
    Name : str
    Address : str
    CustomerId: int
    AccountBalance: double
    #Metodos
    def Register(self):
        void
    def Purchase(self):
        void
#===================================================

class Order:
    #Atributos
    OrderId : int
    Date : date
    CustomerName : str
    CustomerId : int
    #Metodos
    def UpdateProductos(self):
        void
#===================================================

class OrderDetails:
    #Atributos
    OrderId : int
    ProductId : int
    ProductName : str
    Quantity : int
    UnitCost : double
    Total : double
    def __init__(self, order: Order):
        self.Order = order
    #Metodos
    def CalculateTotal(self):
        int




