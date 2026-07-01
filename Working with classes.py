class Planet:
    def __init__(self,name,planet_type,star):
        self.name=name
        self.planet_type=planet_type
        self.star=star


        
        if type(name) is not str or type(planet_type) is not str or type(star) is not str:
            raise TypeError("name, planet type, and star must be strings")

        if name  =="" or planet_type =="" or star =="":
            raise ValueError ("name, planet_type, and star must be non-empty strings")

    def orbit (self):
        return f"{self.name} is orbiting around {self.star}..."
        
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"

planet_1=Planet("real","mars","sun")
print(planet_1)
print(planet_1.orbit())

planet_2=Planet ("real","mars","sun")
print(planet_2)
print(planet_2.orbit())

planet_3=Planet ("real","mars","sun")
print(planet_3)
print(planet_3.orbit())

