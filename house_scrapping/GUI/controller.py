from view import PropertyInputView
from model import PropertyModel
import tkinter as tk
from house_scrapping.remax_url_scrapper import RemaxURLScraper
class PropertyController:
    def __init__(self, view, model=None):
        """
        Initialize the PropertyController.

        Args:
            view (PropertyInputView): The associated view.
            model (PropertyModel, optional): The associated model. Defaults to None.
        """
        self.view = view
        self.model = model
        self.view.set_controller(self)
        # You can create your model instance here if needed

    def get_property_types(self):
        return self.model.get_property_types()
    
    def submit_values(self, num_bathrooms, num_rooms, min_value, max_value, selected_property_types):
        """
        Handle the submission of property values.

        Args:
            num_bathrooms (str): Number of bathrooms input.
            num_rooms (str): Number of rooms input.
            min_value (str): Minimum value input.
            max_value (str): Maximum value input.
            selected_property_types (dictionary): dictionary of property types and state of selection.
        """
        error = False
        # Validate num_bathrooms and num_rooms
        if not (0 <= int(num_bathrooms) < 99):
            print("Error: Invalid number of bathrooms. Need to be between 0 and 99.")
            error = True
        if not (0 <= int(num_rooms) < 99):
            print("Error: Invalid number of rooms. Need to be between 0 and 99.")
            error = True
            
        # Validate min_value and max_value
        if not min_value.isdigit():
            error = True
            if min_value.startswith('-'):
                if min_value[1:].isdigit():  # Check if the rest of the string is composed of digits
                    print("Error: Minimum value cannot be negative.")
                else:
                    print("Error: Minimum value must be a digit.")
        else:
            min_value = int(min_value)
        if not max_value.isdigit():
            error = True
            if max_value.startswith('-'):

                if max_value[1:].isdigit():  # Check if the rest of the string is composed of digits
                    print("Error: Minimum value cannot be negative.")
                else:
                    print("Error: Minimum value must be a digit.")
        else:
            max_value = int(max_value)
        
        if isinstance( max_value, int) and isinstance( min_value, int):
            if max_value < min_value:
                print("Error: Maximum value must be greater than or equal to minimum value.")
                error = True

        if error==True:
            return
        
        # Process the input values, interact with the model, etc.
        self.model.set_num_bathrooms( int(num_bathrooms) )
        self.model.set_num_rooms( int(num_rooms) )
        self.model.set_min_value( int(min_value) )
        self.model.set_max_value( int(max_value) )
        for property_type_keys, property_type_value in selected_property_types.items():
            self.model.set_property_type(property_type_keys, property_type_value)
    
        get_query = self.get_query()
    
    def get_query(self):
        """
        Generate a query string based on the current model values.

        Returns:
            str: The query string.
        """
        remax_scrapper = RemaxURLScraper()  
        remax_scrapper.set_search_param("price", {"min": self.model.get_min_value(), "max": self.model.get_max_value()})
        remax_scrapper.set_search_param("rooms", self.model.get_num_rooms())
        remax_scrapper.set_search_param("bathrooms", self.model.get_num_bathrooms())
        remax_search_query = remax_scrapper.construct_search_url()
        print( remax_search_query )
    
    def decrease_bathrooms(self, user_input):
        """
        Decrease the number of bathrooms.

        Args:
            user_input (str): Current input value.

        Returns:
            int: Updated value after decreasing.
        """
        if user_input.isdigit() and int(user_input) >= 0 and int(user_input) < 99:
            if int(user_input) == 0:
                self.model.set_num_bathrooms( int(user_input) )
                return int(self.model.get_num_bathrooms() )
            self.model.set_num_bathrooms( int(user_input) - 1 )
        return int(self.model.get_num_bathrooms() )

    def increase_bathrooms(self, user_input):
        """
        Increase the number of bathrooms.

        Args:
            user_input (str): Current input value.

        Returns:
            int: Updated value after increasing.
        """
        if user_input.isdigit() and int(user_input) >= 0 and int(user_input) < 99:
            self.model.set_num_bathrooms( int(user_input) + 1 )
        return int(self.model.get_num_bathrooms() )

    def decrease_rooms(self, user_input):
        """
        Decrease the number of rooms.

        Args:
            user_input (str): Current input value.

        Returns:
            int: Updated value after decreasing.
        """
        if user_input.isdigit() and int(user_input) >= 0 and int(user_input) < 99:
            if int(user_input) == 0:
                self.model.set_num_rooms( int(user_input) )
                return int(self.model.get_num_rooms() )
            self.model.set_num_rooms( int(user_input) - 1 )
        return int(self.model.get_num_rooms() )

    def increase_rooms(self, user_input):
        """
        Increase the number of rooms.

        Args:
            user_input (str): Current input value.

        Returns:
            int: Updated value after increasing.
        """
        if user_input.isdigit() and int(user_input) >= 0 and int(user_input) < 99:
            self.model.set_num_rooms( int(user_input) + 1 )
        return int( self.model.get_num_rooms() )

    def set_model(self, model):
        """
        Set the associated model.

        Args:
            model (PropertyModel): The model to associate with.
        """
        self.model = model


if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    root.title("Property Input Application")

    # Instantiate the model
    property_model = PropertyModel()

    # Instantiate the view
    property_input_view = PropertyInputView(root)

    # Instantiate the controller
    property_controller = PropertyController(property_input_view, property_model)

    # Set the controller for the view
    property_input_view.set_controller(property_controller)

    # Run the application
    property_input_view.run()