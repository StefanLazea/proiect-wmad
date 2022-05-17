import pandas as pd


def main():
    realData = pd.DataFrame.from_records([
        {'mileage': 87000, 'make': 'Volkswagen', 'model': 'Gold',
            'fuel': 'Gasoline', 'gear': 'Manual', 'offerType': 'Used',
            'price': 12990, 'hp': 125, 'year': 2015},
        {'mileage': 230000, 'make': 'Opel', 'model': 'Zafira Tourer',
            'fuel': 'CNG', 'gear': 'Manual', 'offerType': 'Used',
            'price': 5200, 'hp': 150, 'year': 2012},
        {'mileage': 5, 'make': 'Mazda', 'model': '3', 'hp': 122,
            'gear': 'Manual', 'offerType': 'Employee\'s car',
            'fuel': 'Gasoline', 'price': 20900, 'year': 2020}
    ])


if __name__ == '__main__':
   main()