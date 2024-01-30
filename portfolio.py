import matplotlib.pyplot as plt

class StockData:
    def __init__(self, symbol, price, quantity):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity
        
    def data(self):
        try:
            self.symbol = input("Podaj symbol: ")
            self.price = float(input("Podaj cenę: "))
            self.quantity = int(input("Podaj ilość: "))
        except Exception:
            raise Exception("Błąd wprowadzonych danych")
            
            
class StockDataModification:
    def __init__(self, stock_data):
        self.stock_data = stock_data
        
    def portfolio(self):
        return self.stock_data.price * self.stock_data.quantity
    
    def introduce(self):
        print("Symbol akcji: " + self.stock_data.symbol)
        print("Cena akcji: " + str(self.stock_data.price))
        print("Ilość akcji: " + str(self.stock_data.quantity))
        print("Wartość portfela: " + str(self.portfolio()))
        
        
class Graph:
    def __init__(self, stock_modification):
        self.stock_modification = stock_modification
        
    def make_graph(self):
        symbol = self.stock_modification.stock_data.symbol
        portfolio_value = self.stock_modification.portfolio()

        plt.bar([symbol], [portfolio_value])
        plt.title('Wartość portfela dla różnych akcji')
        plt.xlabel('Symbol Akcji')
        plt.ylabel('Wartość Portfela')
        plt.show()
    

stock_data = StockData("", 0.0, 0)
stock_data.data()
stock_data_mod = StockDataModification(stock_data)
stock_data_mod.introduce()

graph_stock = Graph(stock_data_mod)
graph_stock.make_graph()




