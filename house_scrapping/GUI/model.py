class PropertyModel:
    def __init__(self):
        """
        Initialize the PropertyModel with default values.

        The model stores information about property attributes such as
        number of bathrooms, number of rooms, min and max values, and property types.
        """
        self._num_bathrooms = 0  # Default value for number of bathrooms
        self._num_rooms = 0  # Default value for number of rooms
        self._min_value = 0  # Default value for minimum value
        self._max_value = 0  # Default value for maximum value
        self._property_types = {
            "Apartmento": False,
            "Estúdio": False,
            "Moradia": False,
            "Prédio": False,
            "Terreno": False,
            "Duplex": False,
            "Garagem": False,
            "Outros\n(Habitacional)": False,
            "Quinta": False
        }

    def set_num_bathrooms(self, value):
        """
        Set the number of bathrooms.

        Args:
            value (int): The value to set for number of bathrooms.
        """
        self._num_bathrooms = value
    
    def set_num_rooms(self, value):
        """
        Set the number of rooms.

        Args:
            value (int): The value to set for number of rooms.
        """
        self._num_rooms = value
    
    def set_min_value(self, value):
        """
        Set the minimum value.

        Args:
            value (int): The value to set for the minimum value.
        """
        self._min_value = value
    
    def set_max_value(self, value):
        """
        Set the maximum value.

        Args:
            value (int): The value to set for the maximum value.
        """
        self._max_value = value
        
    def set_property_type(self, property_type, selected):
        """
        Set the selection status for a property type.

        Args:
            property_type (str): The property type to set.
            selected (bool): The selection status for the property type.
        """
        if property_type in self._property_types:
            self._property_types[property_type] = selected
        else:
            print(f"Invalid property type: {property_type}")

    def get_property_types(self):
        """
        Get the dictionary of property types and their selection status.

        Returns:
            dict: Dictionary of property types and selection status.
        """
        return self._property_types
    
    def add_property_type(self, property_type):
        """
        Add a property type to the dictionary.

        Args:
            property_type (str): The property type to add.
        """
        if property_type not in self._property_types:
            self._property_types[property_type] = False
        else:
            print(f"Property type '{property_type}' already exists.")
            
    def remove_property_type(self, property_type):
        """
        Remove a property type from the dictionary.

        Args:
            property_type (str): The property type to remove.
        """
        if property_type in self._property_types:
            del self._property_types[property_type]
        else:
            print(f"Property type '{property_type}' does not exist.")

    # Getter methods
    def get_num_bathrooms(self):
        """
        Get the number of bathrooms.

        Returns:
            int: The current number of bathrooms.
        """
        return self._num_bathrooms
    
    def get_num_rooms(self):
        """
        Get the number of rooms.

        Returns:
            int: The current number of rooms.
        """
        return self._num_rooms
    
    def get_min_value(self):
        """
        Get the minimum value.

        Returns:
            int: The current minimum value.
        """
        return self._min_value
    
    def get_max_value(self):
        """
        Get the maximum value.

        Returns:
            int: The current maximum value.
        """
        return self._max_value
    
    def get_property_types(self):
        """
        Get the list of property types.

        Returns:
            list: List of property types.
        """
        return self._property_types


if __name__ == "__main__":
    # Create an instance of PropertyModel
    model = PropertyModel()

    # Demonstrate setting and getting property values
    model.set_num_bathrooms(2)
    model.set_num_rooms(3)
    model.set_min_value(100000)
    model.set_max_value(300000)

    # Add property types
    model.add_property_type("Apartment")
    model.add_property_type("House")
    model.add_property_type("Land")

    # Set selection status for property types
    model.set_property_type("Apartment", True)
    model.set_property_type("House", True)
    model.set_property_type("Land", False)

    # Get the dictionary of property types and their selection status
    property_types = model.get_property_types()
    print("Property types:", property_types)

    # Remove a property type
    model.remove_property_type("Apartment")
    print("Property types after removal:", model.get_property_types())

    # Demonstrate setting the selection status for a property type
    model.set_property_type("House", True)
    print("Updated property types:", model.get_property_types())