from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum


app = FastAPI()


# Basic FastAPI endpoint:
@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}


# Endpoint that requires an int as a path parameter:
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # If the item_id param can't be parsed as an int, this route
    # will respond with 422 and { detail: [ {errorObject} ] }
    return {"item_id": item_id}

# Can define an Enum class if there's a use case for a path parameter
# needing to be validated against limited/predefined values/datatypes:
class GrandTour(str, Enum):
    giro = "giro"
    tour = "tour"
    vuelta = "vuelta"

# Endpoint that requires one of three specific strings as a path parameter:
    # If the tour_name param is not a member of the GrandTour enum,
	# this route will respond with 422 and { detail: [ {errorObject} ] }
@app.get("/grand_tours/{tour_name}")
async def read_grand_tour(tour_name: GrandTour):
    # Value of tour_name parameter will be an enum member, so
    # can compare against the GrandTour.giro enum member:
    if tour_name is GrandTour.giro: # Python reminder: "is" checks for reference equality
		# The tour_name enum member gets converted to its actual value:
        return {"tour_name": tour_name, "2023_winner": "Primož Roglič! 🇸🇮"}
    
    # Can also use the enum member's value for comparison:
    if tour_name.value == "tour":
        return {"tour_name": tour_name, "2023_winner": "Jonas Vingegaard! 🇩🇰"}
    
    return {"tour_name": tour_name, "2023_winner": "Sepp Kuss! 🇺🇸"}


# ----- BIKES STUFF! Playing around with query params and request body
#                    validation in POST route.

# Enum for valid bike types
class BikeType(str, Enum):
    road = "road"
    track = "track"

# Bike class:
class Bike(BaseModel):
    type: BikeType
    name: str
    matt_owns_this: bool = False

# List of Bike instances:
bikes: list[Bike] = [
    Bike(type = BikeType.road, name = "Gitane TdF", matt_owns_this = True),
    Bike(type = BikeType.road, name = "Cervelo R5"),
    Bike(type = BikeType.track, name = "Surly Steamroller", matt_owns_this = True),
    Bike(type = BikeType.track, name = "All-City Thunderdome"),
    Bike(type = BikeType.road, name = "Gitane Team Pro"),
]

# Endpoint that accepts whitelisted query parameters:
    # just_my_bikes is an optional query parameter with a default value of False
    # type is an optional parameter with a default value of None
# IF YOU DON'T SPECIFY A DEFAULT (some value or None), the query param is required
@app.get("/bikes")
async def read_bikes(just_my_bikes: bool = False, type: BikeType | None = None):
    bikes_to_send = bikes

    # Potentially filter available bikes by type:
    if type is BikeType.road:
        bikes_to_send = [bike for bike in bikes if bike.type == "road"]
            # Python reminder! This 👆 list comprehension stuff is the Pythonic way
            # to do filter/map/reduce stuff. Rather than: 
            # bikes_to_send = list(filter(lambda x: x.type == "road", bikes))
                # https://www.artima.com/weblogs/viewpost.jsp?thread=98196
    elif type is BikeType.track:
        bikes_to_send = [bike for bike in bikes if bike.type == "track"]

    if just_my_bikes == False:
        return bikes_to_send
    else:
        return [bike for bike in bikes_to_send if bike.matt_owns_this == True]

# Ensures that the request body is a valid Bike instance, sends 201:
@app.post("/bikes", status_code=201)
async def create_bike(bike: Bike):
    bikes.append(bike)
    return bike
