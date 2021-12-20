irish_counties = ["Mayo", "Sligo", "Rosscommon", "Letirm", "Galway",
                  "Donegal", "Derry", "Tyrone", "Antrim", "Fermanagh", "Monaghan", "Cavan", "Armagh", "Down",
                  "Wicklow", "Dublin", "Louth", "Kildare" "Longford", "Kilkenny", "Meath", "West Meath", "Wexford", "Offaly", "Laois", "Carlow",
                   "Clare", "Cork", "Kerry", "Limerick", "Tipperary", "Waterford"
                  ]
connaght = ["Sligo", "Letrim", "Rosscommon", "Galway"]
print(connaght)

connaght.insert(0,"Mayo")
print(connaght)


munster = [ "Clare", "Cork", "Kerry", "Limerick"]
print(munster)

munster.extend(["Tipperary", "Waterford"])
print(munster)
