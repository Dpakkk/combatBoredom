class Mercedez:
    totalProduction = 50000
    damageNumbers = 32
    consumedCountry = 'USA'

    def __init__(self, modelName, modelYear, manufactureCountry, colors, mileageCapacity, salesTarget, salesQuantity):
        self.modelName = modelName
        self.modelYear = modelYear
        self.manufactureCountry = manufactureCountry
        self.colors = colors
        self.mileageCapacity = mileageCapacity
        self.salesTarget = salesTarget
        self.salesQuantity = salesQuantity

    @classmethod 
    def defectRate(cls):
        return cls.damageNumbers/cls.totalProduction

    def targetGuage(self):
        return self.salesQuantity/self.salesTarget


m1 = Mercedez("A-CLASS",2020,"USA",['Black', 'Blue','Navy','White'], 450000, 8000, 3000)
m2 = Mercedez("B-CLASS*",2020,"USA",['Black', 'Blue','Navy','White'], 550000, 6000, 2000)
m3 = Mercedez("CLA",2020,"USA",['Black', 'Blue','Navy','White'], 350000, 4000, 3000)
m4 = Mercedez("C-CLASS",2020,"GERMANY",['Black', 'Blue','Navy','White'], 450000, 14000, 9000)
m5 = Mercedez("E-CLASS/CLS",2020,"USA",['Black', 'Blue','Navy','White'], 250000, 17000, 16999)
m6 = Mercedez("S-CLASS/CLS",2020,"USA",['Black', 'Blue','Navy','White'], 450000, 19990, 15349)
m7 = Mercedez("GLA",2020,"USA",['BLUE', 'YELLOW','MATT BLACK','White'], 430000, 600, 100)
m8 = Mercedez("GLB",2020,"USA",['SHINY BLACK', 'Blue','Navy','White'], 450000, 500, 250)
m7 = Mercedez("GLC",2020,"USA",['BLUE', 'YELLOW','MATT BLACK','White'], 420000, 800, 800)
m8 = Mercedez("GLE",2021,"GERMANY",['G-WAGON MIX COLOR', 'Blue','Navy DARK','White'], 60000, 200, 180)
