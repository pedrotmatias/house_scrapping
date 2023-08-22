import tkinter as tk
from tkinter import font
from tkinter import ttk

class PropertyInputView:
    def __init__(self, root):
        """
        Initialize the PropertyInputView.

        Parameters:
            root (Tk): The main application window.

        Attributes:
            root (Tk): The main application window.
            controller: The controller associated with the view.
            title_font (Font): Font for the title label.
            normal_font (Font): Font for normal text.
            title_label (Label): Label for the title of the application.
            frame1 (Frame): Frame for the first section of UI elements.
            frame_prices (Frame): Frame for the prices section of UI elements.
            frame_checkboxes (Frame): Frame for the checkboxes section of UI elements.
            submit_button (Button): Button to submit the input values.
            frame_button1 (Frame): Sub-frame for buttons in the first row.
            frame_button2 (Frame): Sub-frame for buttons in the second row.
            label_num_bathrooms (Label): Label for the number of bathrooms.
            entry_num_bathrooms (Entry): Entry widget for entering the number of bathrooms.
            button_increase_bathrooms (Button): Button to increase the number of bathrooms.
            button_decrease_bathrooms (Button): Button to decrease the number of bathrooms.
            label_num_rooms (Label): Label for the number of rooms.
            entry_num_rooms (Entry): Entry widget for entering the number of rooms.
            button_increase_rooms (Button): Button to increase the number of rooms.
            button_decrease_rooms (Button): Button to decrease the number of rooms.
            label_min_value (Label): Label for the minimum value.
            entry_min_value (Entry): Entry widget for entering the minimum value.
            label_max_value (Label): Label for the maximum value.
            entry_max_value (Entry): Entry widget for entering the maximum value.
            property_types (list): List of available property types.
            property_type_vars (list): List of StringVar variables for property types.
        """
        self.root = root
        self.controller = None  # We'll set this later

        # Configure fonts for title and normal text
        self.title_font = font.Font(family="Arial", size=20, weight="bold")
        self.normal_font = font.Font(family="Helvetica", size=30)

        # Create the title label and set its font
        self.title_label = tk.Label(self.root, text="Property Input Application", font=self.title_font)
        self.title_label.grid(row=0, columnspan=4, pady=20, sticky='n')

        # Create frames for different sections
        self.frame1 = tk.Frame(self.root)
        self.frame1.grid(row=1, column=0, padx=0, pady=(0, 0), sticky='w')
        
        self.frame_prices = tk.Frame(self.root)
        self.frame_prices.grid(row=2, column=0, padx=0, pady=20, sticky='w')
        
        self.frame_location = tk.Frame(self.root)
        self.frame_location.grid(row=3, column=0, padx=0, pady=20, sticky='w')
        
        self.frame_checkboxes = tk.Frame(self.root)
        self.frame_checkboxes.grid(row=4, column=0, padx=0, pady=20, sticky='w')

        # Create Submit button and set its command
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_values)
        self.submit_button.grid(row=5, pady=20, sticky='n')
        
        # Layout configuration for the first frame
        # Create sub-frames for buttons
        self.frame_button1 = tk.Frame(self.frame1)
        self.frame_button2 = tk.Frame(self.frame1)
        
        # Create labels, entry widgets, and buttons for the first row
        self.label_num_bathrooms = tk.Label(self.frame1, text="Number of Bathrooms:")
        self.entry_num_bathrooms = tk.Entry(self.frame1)
        self.button_increase_bathrooms = tk.Button(self.frame_button1, text="+", command=self.increase_bathrooms)
        self.button_increase_bathrooms.pack(side="left")
        self.button_decrease_bathrooms = tk.Button(self.frame_button1, text="-", command=self.decrease_bathrooms)
        self.button_decrease_bathrooms.pack(side="left")
        
        # Place widgets in the grid for the first row
        self.label_num_bathrooms.grid(row=0, column=0, padx=(0, 10), sticky='w')
        self.entry_num_bathrooms.grid(row=0, column=1, padx=(0, 10), sticky='w')
        self.frame_button1.grid(row=0, column=2, padx=(0, 10), sticky='w')
        
        # Create labels, entry widgets, and buttons for the second row
        self.label_num_rooms = tk.Label(self.frame1, text="Number of Rooms:")
        self.entry_num_rooms = tk.Entry(self.frame1)
        self.button_increase_rooms = tk.Button(self.frame_button2, text="+", command=self.increase_rooms)
        self.button_increase_rooms.pack(side="left")
        self.button_decrease_rooms = tk.Button(self.frame_button2, text="-", command=self.decrease_rooms)
        self.button_decrease_rooms.pack(side="left")
        
        # Place widgets in the grid for the second row
        self.label_num_rooms.grid(row=1, column=0, padx=(0, 10), sticky='w')
        self.entry_num_rooms.grid(row=1, column=1, padx=(0, 10), sticky='w')
        self.frame_button2.grid(row=1, column=2, padx=(0, 10), sticky='w')
        
        # Layout configuration for the "Prices" frame
        # Create labels and entry widgets for minimum and maximum values
        self.label_min_value = tk.Label(self.frame_prices, text="Minimum Value:")
        self.entry_min_value = tk.Entry(self.frame_prices)
        self.label_max_value = tk.Label(self.frame_prices, text="Maximum Value:")
        self.entry_max_value = tk.Entry(self.frame_prices)

        # Place widgets in the grid for the "Prices" frame
        self.label_min_value.grid(row=0, column=0, sticky='w')
        self.entry_min_value.grid(row=0, column=1, sticky='w')
        self.label_max_value.grid(row=0, column=2)
        self.entry_max_value.grid(row=0, column=3)

        
        # Initialize all entry values to 0
        self.entry_num_bathrooms.insert(0, "0")
        self.entry_num_rooms.insert(0, "0")
        self.entry_min_value.insert(0, "0")
        self.entry_max_value.insert(0, "0")
        
        # Set entry widgets for number of bathrooms and rooms as read-only
        self.entry_num_bathrooms.config(state="readonly")
        self.entry_num_rooms.config(state="readonly")

        
    def submit_values(self):
        """
        Handle the submission of input values.

        If a controller is set, gather input values from various UI elements,
        then call the controller's `submit_values` method with the gathered values.

        """
        if self.controller:
          num_bathrooms_text = self.entry_num_bathrooms.get()
          num_rooms_text = self.entry_num_rooms.get()
          min_value_text = self.entry_min_value.get()
          max_value_text = self.entry_max_value.get()
          
          selected_property_types = {
              property_type: var.get() for var, property_type in zip(self.property_type_vars, self.property_types.keys() )
          }
          self.controller.submit_values(num_bathrooms_text, num_rooms_text, min_value_text, max_value_text, selected_property_types)

      
    def set_controller(self, controller):
        """
        Set the controller for the view.

        Parameters:
            controller: The controller associated with the view.

        """
        self.controller = controller
        
        # Create Checkboxes and Labels for Property Types
        self.property_types = self.controller.get_property_types()
        
        self.property_type_vars = []

        #Drop down menu
        self.frame_district = tk.Frame(self.frame_location)
        self.frame_district.grid(row=0, column=0, padx= 10, sticky='w')
        self.frame_concelho = tk.Frame(self.frame_location)
        self.frame_concelho.grid(row=0, column=1, padx=10, sticky='w')
        self.frame_freguesia = tk.Frame(self.frame_location)
        self.frame_freguesia.grid(row=0, column=2, padx=10, sticky='w')
            
        self.distrito_dropdown_label = ttk.Label(self.frame_district, text="Seloecionar Distrito")
        self.distrito_dropdown_label.pack(side="top")
        self.options_distrito = self.controller.get_distritos()
        self.distrito_dropdown_var = tk.StringVar(value=self.options_distrito[-1])
        self.distrito_dropdown = ttk.Combobox(self.frame_district, textvariable=self.distrito_dropdown_var, values=self.options_distrito)
        self.distrito_dropdown.bind("<<ComboboxSelected>>", self.on_distrito_dropdown_selected)
        self.distrito_dropdown.pack(side="left")
        
        self.concelho_dropdown_label = ttk.Label(self.frame_concelho, text="Selecionar Concelho")
        self.concelho_dropdown_label.pack(side="top")
        self.options_concelho = self.controller.get_concelhos('All')
        self.concelho_dropdown_var = tk.StringVar(value=self.options_concelho[0])
        self.concelho_dropdown = ttk.Combobox(self.frame_concelho, textvariable=self.concelho_dropdown_var, values=self.options_concelho, state="disabled")
        self.concelho_dropdown.bind("<<ComboboxSelected>>", self.on_concelho_dropdown_selected)
        self.concelho_dropdown.pack(side="left")
        
        self.freguesia_dropdown_label = ttk.Label(self.frame_freguesia, text="Selecionar Freguesia")
        self.freguesia_dropdown_label.pack(side="top")
        self.options_freguesia = self.controller.get_freguesias('All', 'All')
        self.freguesia_dropdown_var = tk.StringVar(value=self.options_freguesia[0])
        self.freguesia_dropdown = ttk.Combobox(self.frame_freguesia, textvariable=self.freguesia_dropdown_var, values=self.options_freguesia, state="disabled"  )
        self.freguesia_dropdown.pack(side="left")

        # Loop to create checkboxes and labels for property types
        i = 0
        for property_name, property_select_status in self.property_types.items():
            var = tk.StringVar( value=property_select_status )
            checkbox = tk.Checkbutton(self.frame_checkboxes, text=property_name, variable=var)
            checkbox.grid(row=0 + (i % 4), column=i // 4, sticky="w")
            i += 1
            self.property_type_vars.append(var)
            

    def run(self):
        """
        Run the main event loop of the Tkinter application.

        """
        # Start the main event loop
        self.root.mainloop()


    def decrease_bathrooms(self):
        """
        Handle the decrease of the number of bathrooms.

        If a controller is set, call the controller's `decrease_bathrooms` method,
        update the UI accordingly, and keep the entry widget read-only.

        """
        if self.controller:
            updated_value = self.controller.decrease_bathrooms( self.entry_num_bathrooms.get() )
            self.entry_num_bathrooms.config(state="normal")
            self.entry_num_bathrooms.delete(0, tk.END)
            self.entry_num_bathrooms.insert(0, str( updated_value ) )
            self.entry_num_bathrooms.config(state="readonly")
            
    def increase_bathrooms(self):
        """
        Handle the increase of the number of bathrooms.

        If a controller is set, call the controller's `increase_bathrooms` method,
        update the UI accordingly, and keep the entry widget read-only.

        """
        if self.controller:
            updated_value = self.controller.increase_bathrooms( self.entry_num_bathrooms.get() )
            self.entry_num_bathrooms.config(state="normal")
            self.entry_num_bathrooms.delete(0, tk.END)
            self.entry_num_bathrooms.insert(0, str( updated_value ) )
            self.entry_num_bathrooms.config(state="readonly")
            
    def decrease_rooms(self):
        """
        Handle the decrease of the number of rooms.

        If a controller is set, call the controller's `decrease_rooms` method,
        update the UI accordingly, and keep the entry widget read-only.

        """
        if self.controller:
            updated_value = self.controller.decrease_rooms( self.entry_num_rooms.get() )
            self.entry_num_rooms.config(state="normal")
            self.entry_num_rooms.delete(0, tk.END)
            self.entry_num_rooms.insert(0, str( updated_value ) )
            self.entry_num_rooms.config(state="readonly")
            
    def increase_rooms(self):
        """
        Handle the increase of the number of rooms.

        If a controller is set, call the controller's `increase_rooms` method,
        update the UI accordingly, and keep the entry widget read-only.

        """
        if self.controller:
            updated_value = self.controller.increase_rooms( self.entry_num_rooms.get() )
            self.entry_num_rooms.config(state="normal")
            self.entry_num_rooms.delete(0, tk.END)
            self.entry_num_rooms.insert(0, str( updated_value ) )
            self.entry_num_rooms.config(state="readonly")

    def on_distrito_dropdown_selected(self, event):
            self.options_concelho = self.controller.get_concelhos( event.widget.get() )
            self.concelho_dropdown_var = tk.StringVar(value=self.options_concelho[-1])
            
            self.options_freguesia = self.controller.get_freguesias()
            self.freguesia_dropdown_var = tk.StringVar(value=self.options_freguesia[0])  
            self.freguesia_dropdown.config( textvariable=self.freguesia_dropdown_var, values=self.options_freguesia, state="disabled")
            
            if event.widget.get() == 'All':
                self.concelho_dropdown.config( textvariable=self.concelho_dropdown_var, values=self.options_concelho, state="disabled")
                return
            
            self.concelho_dropdown.config(textvariable=self.concelho_dropdown_var, values=self.options_concelho, state="normal")
        
    def on_concelho_dropdown_selected(self, event):
        self.options_freguesia = self.controller.get_freguesias( self.distrito_dropdown.get(), event.widget.get())
        self.freguesia_dropdown_var = tk.StringVar(value=self.options_freguesia[0])

        if event.widget.get() == 'All':
            self.freguesia_dropdown.config( textvariable=self.freguesia_dropdown_var, values=self.options_freguesia, state="disabled")
            return
        
        self.freguesia_dropdown.config( textvariable=self.freguesia_dropdown_var, values=self.options_freguesia, state="normal")