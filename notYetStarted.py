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


m1 = Mercedez("A-CLASS",2020,"USA",['Black', 'Blue','Navy','White'], 450000, 44000, 32000)
m2 = Mercedez("B-CLASS*",2020,"GERMANY",['Black', 'Blue','Navy','White'], 450000, 44000, 32000)
m3 = Mercedez("CLA",2020,"USA",['Black', 'Blue','Navy','White'], 450000, 44000, 32000)
m4 = Mercedez("C-CLASS",2020,"GERMANY",['Black', 'Blue','Navy','White'], 450000, 44000, 32000)
m5 = Mercedez("E-CLASS/CLS",2020,"USA",['Black', 'Blue','Navy','White'], 450000, 44000, 32000)
m6 = Mercedez("S-CLASS/CLS",2020,"GERMANY",['Black', 'Blue','Navy','White'], 450000, 44000, 32000)
m7 = Mercedez("GLA",2020,"USA",['Black', 'Blue','Navy','White'], 450000, 44000, 32000)
m8 = Mercedez("GLB",2020,"GERMANY",['Black', 'Blue','Navy','White'], 450000, 44000, 32000)
m7 = Mercedez("GLC",2020,"USA",['Black', 'Blue','Navy','White'], 450000, 44000, 32000)
m8 = Mercedez("GLE",2020,"GERMANY",['Black', 'Blue','Navy','White'], 450000, 44000, 32000)

