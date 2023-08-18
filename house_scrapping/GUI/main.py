import tkinter as tk
from model import PropertyModel
from view import PropertyInputView
from controller import PropertyController

# Instantiate the main application window
app = tk.Tk()
app.title("Variable Input App")

# Instantiate the models
property_model = PropertyModel()

# Instantiate the view
property_input_view = PropertyInputView(app)

# Instantiate the controller
property_controller = PropertyController(property_input_view, property_model)

# Set the controller for the view
property_input_view.set_controller(property_controller)

# Run the application
property_input_view.run()
