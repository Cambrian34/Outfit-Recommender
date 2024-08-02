

# create a method to add clothes to the closet
# create a method to remove clothes from the closet
# create a method to display all clothes in the closet
# create a method to display all clothes in the closet of a certain type
# create a method to display all clothes in the closet of a certain color
#also add the ability to add a picture of the clothes
# create a method to combine the clothes of different types

class Closet:
    def __init__(self):
        self.clothes = []

    def add_clothes(self, clothes):
        self.clothes.append(clothes)

    def remove_clothes(self, clothes):
        self.clothes.remove(clothes)

    def display_all_clothes(self):
        for clothes in self.clothes:
            print(clothes)

    def display_clothes_type(self, type):
        for clothes in self.clothes:
            if clothes.type == type:
                print(clothes)

    def display_clothes_color(self, color):
        for clothes in self.clothes:
            if clothes.color == color:
                print(clothes)

    def combine_clothes(self, clothes1, clothes2):
        self.clothes.append(combine_clothes(clothes1, clothes2))
   

class Clothes:
    #add mopre attributes such as , type ie shoes, shirt, pants, color, picture
    def __init__(self, type, color, picture):
        self.type = type
        self.color = color
        self.picture = picture

    def __str__(self):
        return f"{self.color} {self.type}"

    
    

def combine_clothes(clothes1, clothes2):
    return Clothes(f"{clothes1.type} {clothes2.type}", f"{clothes1.color} {clothes2.color}", "combined")

#method:does a combination of the clothes to create a combined clothes
#get a list of clothes
#combine the clothes


def combination(clothes):
    if len(clothes) <= 2:  # Base case: Combine at most two items
        return combine_clothes(clothes[0], clothes[1])

    all_combinations = []
    for pair in combination(clothes, 2):  # Get pairs without repetition
        combined_outfit = combine_clothes(pair[0], pair[1])
        all_combinations.append(combined_outfit)
    return all_combinations  # A list of potential outfits







#make it vsisble using tkinter
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ClosetApp:
    # Initialize the application
    def __init__(self, root):
        self.root = root
        self.root.title("Closet App")
        self.closet = Closet()
        self.create_widgets()
    
    # Create the widgets for the application
    def create_widgets(self):
        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)
        
        # Create a button to add clothes
        self.add_button = tk.Button(self.button_frame, text="Add Clothes", command=self.add_clothes)
        self.add_button.pack(side=tk.LEFT, padx=10)
        
        # Create a button to display all clothes
        self.display_button = tk.Button(self.button_frame, text="Display All Clothes", command=self.display_all_clothes)
        self.display_button.pack(side=tk.LEFT, padx=10)
        
        # Create a button to combine clothes
        self.combine_button = tk.Button(self.button_frame, text="Combine Clothes", command=self.combine_clothes)
        self.combine_button.pack(side=tk.LEFT, padx=10)
        
        # Create a frame to display the clothes
        self.clothes_frame = tk.Frame(self.root)
        self.clothes_frame.pack(pady=10)

    # Method to add clothes to the closet
    def add_clothes(self):
        # Create a file dialog to select an image
        file_path = filedialog.askopenfilename()
        if file_path:
            # Create a new clothes object
            clothes = Clothes("shirt", "blue", file_path)
            self.closet.add_clothes(clothes)
            # Display the clothes in the frame
            self.display_clothes(clothes)

    # Method to display all clothes in the closet
    def display_all_clothes(self):
        for clothes in self.closet.clothes:
            self.display_clothes(clothes)

    # Method to combine clothes in the closet
    def combine_clothes(self):
        combined_clothes = combination(self.closet.clothes)
        for clothes in combined_clothes:
            self.display_clothes(clothes)

    
    ##show the app
    def display_clothes(self, clothes):
        # Load the image
        image = Image.open(clothes.picture)
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        
        # Create a label to display the image
        label = tk.Label(self.clothes_frame, image=photo)
        label.image = photo
        label.pack(side=tk.LEFT, padx=10)
        # Frame for each item
        item_frame = tk.Frame(self.clothes_frame)
        item_frame.pack(side=tk.LEFT, padx=10)

        # Image Label 
        image_label = tk.Label(item_frame, image=photo)
        image_label.image = photo  # Keep reference
        image_label.pack()

        # Info labels
        tk.Label(item_frame, text=f"Type: {clothes.type}").pack()
        tk.Label(item_frame, text=f"Color: {clothes.color}").pack()


# Create the main window
root = tk.Tk()
app = ClosetApp(root)
root.mainloop()
