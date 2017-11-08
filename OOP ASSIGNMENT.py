
class Bank(object):
    def __init__(self,Bankid, Name, Location):
        assert type(Bankid) == int and type(Location) == str
        self.Bankid = Bankid
        self.Name = Name
        self.Location = Location
class Teller1(Bank):
    def __init__(self, Id, Name):
        assert type(Id) == int
        self.Id = Id
        self.Name = Name
    def CollectMoney(self, amount):
        self.balance += amount
        print("%d dear customer that is your balance"%(self.balance))
    def OpenAccount(self):
        print("%d, %s dear customer your account number is %d"%(self.Id, self.Name, self.AccNo))
        print(" branch is %s"%Bank1.Location)
    def CloseAccount(self):
        print("%s, account has been successfully closed %s" %(self.Name,Bank1.Location))
    def Loanrequest(self):
        if self.balance>4000:
            print("dear customer you can get  a loan from %s" %(Bank1.Location))
        else:
            print("request failed")
    def ProvideInfo(self):
        print("Id:%d\nName:%s\nAddress:%s\nPhoneNo:%d\nAccNo:%d\nBranch:%s"%(self.Id, self.Name, self.Address, self.PhoneNo, self.AccNo, Bank1.Location))
    def IssueCard(self):
        print("%s, dear customer get card from %s"%(self.Name,Bank1.Location))
class Teller2(Bank):
    def __init__(self, Id, Name):
        assert type(Id) == int
        self.Id = Id
        self.Name = Name
        self.balance = 0
    def CollectMoney(self, amount):
        self.balance += amount
        print("%d here is your balance"%(self.balance))
    def OpenAccount(self):
        print("%d %s dear customer your account number is %d"%(self.Id, self.Name, self.AccNo))
        print("your branch is %s" % Bank2.Location)
    def CloseAccount(self):
        print("%s, your account is closed from %s" % (self.Name, Bank2.Location))
    def Loanrequest(self):
        if self.balance > 4000:
            print("you are legible to getting a loan from %s" % (Bank2.Location))
        else:
            print("request failed")
    def ProvideInfo(self):
        print("Id:%d\nName:%s\nAddress:%s\nPhoneNo:%d\nAccNo:%d\nBranch:%s"%(self.Id, self.Name, self.Address, self.PhoneNo, self.AccNo, Bank2.Location))
    def IssueCard(self):
        print("%s, your ATM is ready,Come and pick it from %s" % (self.Name, Bank2.Location))
class CustomerB(Teller2, Bank):
    def __init__(self, Id, Name, Address, PhoneNo, AccNo, balance):
       self.Id = Id
       self.Name = Name
       self.Address = Address
       self.PhoneNo = PhoneNo
       self.AccNo = AccNo
       self.balance = balance
    def GeneralInquiry(self):
        print("Id:%d\nName:%s\nAddress:%s\nPhoneNo:%d\nAccNo:%d\nBalance:%d" % (self.Id, self.Name, self.Address, self.PhoneNo, self.AccNo,self.balance))
    def DepositMoney(self, amount):
        assert type(amount) == int
        self.balance += amount
        print('%d is your balance' % self.balance)
        print("you were assisted by %s" % Teller2A.Name)
    def WithdrawMoney(self, amount):
        self.balance -= amount
        if self.balance < 2000:
            print("sorry you have minimum balance")
            print("you were assisted by %s" % Teller2A.Name)
        else:
            print("%d is your balance" % self.balance)
            print("you were assisted by %s"%Teller2A.Name)
    def openAccount(self):
        print("open an account")
    def closeAccount(self):
        print("account closed")
    def applyLoan(self):
        print("Name:%s,AccNo:%d I would like to get a loan from %s" % (self.Name, self.AccNo, Bank2.Location))
    def requestCard(self):
        print("request for  card")
class CustomerA(Teller1, Bank):
    def __init__(self, Id, Name, Address, PhoneNo, AccNo, balance):
       self.Id = Id
       self.Name = Name
       self.Address = Address
       self.PhoneNo = PhoneNo
       self.AccNo = AccNo
       self.balance = balance
    def GeneralInquiry(self):
        print("Id:%d\nName:%s\nAddress:%s\nPhoneNo:%d\nAccNo:%d\nBalance:%d" % (self.Id, self.Name, self.Address, self.PhoneNo, self.AccNo,self.balance))
    def DepositMoney(self, amount):
        assert type(amount) == int
        self.balance += amount
        print('%d is your balance' % self.balance)
        print("you were assisted by %s"%Teller1A.Name)
    def WithdrawMoney(self,amount):
        self.balance-=amount
        if self.balance<2000:
            print("you have minimum balance")
            print(" served by  %s"%Teller1A.Name)
        else:
            print("%d is your balance"%(self.balance))
            print("you were served by %s"%Teller1A.Name)
    def openAccount(self):
        print("Do you wish to open an account")
    def closeAccount(self):
        print(" account closed ")
    def applyLoan(self):
        print("Name:%s,AccNo:%d I would like to get a loan from %s"%(self.Name,self.AccNo,Bank1.Location))
    def requestCard(self):
        print("where is my card")
class Account(CustomerB,CustomerA):
    def __init__(self,Id,CustomerId):
        self.Id=Id
        self.CustomerId
        print("your account balance is %d"%self.balance)
class Checking(Account):
    def __init__(self,Id,CustomerId):
        self.Id=Id
        self.CustomerId=CustomerId
        print("your account balance is %d"%self.balance)
class Loan(CustomerB,CustomerA):
    def __init__(self,Id,Type,AccountId,CustomerId):
     pass
class Account():
    def __init__(self,Id,CustomerId):
        pass
class Checking():
    def __init__(self,Id,CustomerId):
        pass
class Savings():
    def __init__(self,Id,CustomerId):
        pass
Bank1 = Bank(1, 'KCB', 'KAMPALA')
Bank2 = Bank(2, 'GTB', 'MAKERERE')
Teller1A = Teller1(4, "CLARISSE")
Teller1B = Teller1(5, "CLAUDETTE")
Teller1C = Teller1(6, "RHADIAH")
Teller2A = Teller2(7, "CLAIR")
Teller2B = Teller2(8, "AMORE")
Teller2C = Teller2(9, "ELICA")
A = CustomerA(12, "LILY", "KAMPALA", 800, 290, 870)
B = CustomerA(12, "ODONG", "KAMPALA", 789, 487, 534)
C = CustomerA(14, "DOREEN", "Kotido", 657, 598,556)
D = CustomerA(15, "ALINE", "BWAISE", 546, 665, 778)
E = CustomerA(16, "ANDREW", "WANDEGEYA", 564, 42,745)
F = CustomerA(17, "GRACE", "KOLOLO", 525, 556, 523)
G = CustomerA(34, "AIME", "MASAKA", 574, 812, 748)
H = CustomerA(14, "FAHADI", "PAKWACH", 564, 942, 635)
I = CustomerA(21, "ALICE", "KAMPALA", 554, 242, 867)
J = CustomerA(24, "SANDRINE", "KASESE", 5441, 425, 423)
K = CustomerB(45, "BENNY", "KAMPALA", 524, 425, 152)
R = CustomerB(17, "SABINE", "BUKEDIA", 700, 642, 578)
M = CustomerB(17, "DOLICE", "MOROTO", 400, 842, 765)
N = CustomerB(17, "DIANA", "GULU", 200, 52, 956)
O = CustomerB(17, "JOSI", "BUSHENYI", 212, 999, 597)
P = CustomerB(17, "CLAUDE", "IBANDA", 678, 232, 423)
L = CustomerB(17, "KAMI", "MARACHA", 435, 575, 645)
S = CustomerB(17, "ESTHER", "MAYUGE", 900, 657, 590)
T = CustomerB(17, "ZUHURAH", "KAMPALA", 456, 111, 278)
U = CustomerB(17, "NICE", "MUKONO", 456, 129, 246)
A.WithdrawMoney(2000)
