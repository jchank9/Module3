import matplotlib.pyplot as plt

# Function for a plot that makes a letter
# Input: a letter, Output: a plot with the letter

def PlotLetter(c):
   plt.text(0.6, 0.7, c, size=50, rotation=30.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )