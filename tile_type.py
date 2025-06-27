import time
import math

class Tile:
    """
    Base class for all tile types in the game.
    """
    def __init__(self, name: str, description: str, traversable: bool = True, symbol: str = "."):
        self.name = name
        self.description = description
        self.traversable = traversable
        self.symbol = symbol  # For map representation

    def __str__(self):
        return f"{self.name}: {self.description}"

    def to_dict(self):
        """Serializes the tile object to a dictionary for JSON storage."""
        return {
            "name": self.name,
            "description": self.description,
            "traversable": self.traversable,
            "symbol": self.symbol,
            "type": self.__class__.__name__  # Store the subclass type
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Deserializes a dictionary back into a Tile object or its subclass."""
        tile_type = data.get("type", "Tile")
        # This part will require specific subclass knowledge if we want to instantiate them directly.
        # For now, it can create a base Tile or we can expand it later.
        if tile_type == "Forest":
            return Forest.from_dict(data)
        elif tile_type == "Mountain":
            return Mountain.from_dict(data)
        elif tile_type == "City":
            return City.from_dict(data)
        elif tile_type == "Water":
            return Water.from_dict(data)
        # Add other tile types here
        return Tile(data["name"], data["description"], data.get("traversable", True), data.get("symbol", "."))


class Forest(Tile):
    """
    Represents a forest tile, potentially rich in wood or hiding creatures.
    """
    def __init__(self, name: str = "Forest", description: str = "A dense collection of trees.", traversable: bool = True, symbol: str = "F", resource_type: str = "wood"):
        super().__init__(name, description, traversable, symbol)
        self.resource_type = resource_type

    def to_dict(self):
        data = super().to_dict()
        data["resource_type"] = self.resource_type
        return data

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name", "Forest"),
            description=data.get("description", "A dense collection of trees."),
            traversable=data.get("traversable", True),
            symbol=data.get("symbol", "F"),
            resource_type=data.get("resource_type", "wood")
        )

class Mountain(Tile):
    """
    Represents a mountain tile, possibly difficult to traverse or rich in ore.
    """
    def __init__(self, name: str = "Mountain", description: str = "A towering peak, challenging to climb.", traversable: bool = False, symbol: str = "M", elevation: int = 1000):
        super().__init__(name, description, traversable, symbol)
        self.elevation = elevation # in meters

    def to_dict(self):
        data = super().to_dict()
        data["elevation"] = self.elevation
        return data

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name", "Mountain"),
            description=data.get("description", "A towering peak, challenging to climb."),
            traversable=data.get("traversable", False),
            symbol=data.get("symbol", "M"),
            elevation=data.get("elevation", 1000)
        )

class City(Tile):
    """
    Represents a city tile, a hub of civilization, trade, and quests.
    """
    def __init__(self, name: str = "City", description: str = "A bustling urban center.", traversable: bool = True, symbol: str = "C", population: int = 10000):
        super().__init__(name, description, traversable, symbol)
        self.population = population

    def to_dict(self):
        data = super().to_dict()
        data["population"] = self.population
        return data

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name", "City"),
            description=data.get("description", "A bustling urban center."),
            traversable=data.get("traversable", True),
            symbol=data.get("symbol", "C"),
            population=data.get("population", 10000)
        )

class Water(Tile):
    """
    Represents a water tile, like a lake or ocean, possibly requiring a boat to traverse.
    """
    def __init__(self, name: str = "Water", description: str = "A body of water.", traversable: bool = False, symbol: str = "W", water_type: str = "lake"):
        super().__init__(name, description, traversable, symbol)
        self.water_type = water_type # e.g., "lake", "river", "ocean"

    def to_dict(self):
        data = super().to_dict()
        data["water_type"] = self.water_type
        return data

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name", "Water"),
            description=data.get("description", "A body of water."),
            traversable=data.get("traversable", False),
            symbol=data.get("symbol", "W"),
            water_type=data.get("water_type", "lake")
        )

# Example usage:
if __name__ == '__main__':
    forest_tile = Forest()
    mountain_tile = Mountain(elevation=1500)
    city_tile = City(name="Capital City", population=50000)
    water_tile = Water(water_type="ocean")

    print(forest_tile)
    print(mountain_tile)
    print(city_tile)
    print(water_tile)

    # Serialization example
    city_dict = city_tile.to_dict()
    print("\nSerialized City:", city_dict)

    # Deserialization example
    # In a real scenario, you'd get tile_type from the dict to know which class to call from_dict on.
    # For simplicity, we know it's a City here.
    # A more robust from_dict in the base Tile class could handle routing to the correct subclass.
    loaded_city_tile = Tile.from_dict(city_dict) # Using the base class's factory method
    print("Loaded City Name:", loaded_city_tile.name)
    if isinstance(loaded_city_tile, City):
        print("Loaded City Population:", loaded_city_tile.population)

    # Test deserialization for other types
    forest_dict = forest_tile.to_dict()
    loaded_forest_tile = Tile.from_dict(forest_dict)
    print("\nLoaded Forest Resource Type:", loaded_forest_tile.resource_type if isinstance(loaded_forest_tile, Forest) else "N/A")

    mountain_dict = mountain_tile.to_dict()
    loaded_mountain_tile = Tile.from_dict(mountain_dict)
    print("Loaded Mountain Elevation:", loaded_mountain_tile.elevation if isinstance(loaded_mountain_tile, Mountain) else "N/A")

    water_dict = water_tile.to_dict()
    loaded_water_tile = Tile.from_dict(water_dict)
    print("Loaded Water Type:", loaded_water_tile.water_type if isinstance(loaded_water_tile, Water) else "N/A")