# PandasGUI

## What is PandasGUI?
PandasGUI is a Python-based graphical user interface (GUI) tool that allows users to interactively explore and manipulate Pandas DataFrames without writing extensive code. It provides a user-friendly way to perform data analysis, generate visualizations, and automatically generate Python scripts for operations performed through the interface.

---

### Installation
To install PandasGUI, run:
```bash
pip install pandasgui
```
For better compatibility, it is recommended to use Python 3.8 or above in a virtual environment.

To create a virtual environment and install PandasGUI:
```bash
conda create -n pandasgui_env python=3.8
conda activate pandasgui_env
pip install pandasgui
```

---

### Using PandasGUI
#### 1. Launching PandasGUI
To open PandasGUI without any dataset:
```python
from pandasgui import show
show()
```
This will launch an interactive GUI where you can manually load datasets.

#### 2. Loading a DataFrame
To open PandasGUI with a DataFrame:
```python
import pandas as pd
from pandasgui import show

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
})

# Launch GUI
show(df)
```
This will open the GUI with the dataset loaded, allowing you to explore it visually.

---

### Features of PandasGUI
1. Interactive Data Viewing  
   - View datasets in an Excel-like format.
   - Sort and filter rows using a graphical interface.

2. Data Editing
   - Directly edit cells within the GUI.

3. Visualization Tools
   - Create charts such as bar plots, histograms, and scatter plots without coding.

4. Automatic Code Generation
   - Any operation performed in the GUI generates equivalent Python code for reproducibility.

5. Multiple Dataset Handling
   - Load and compare multiple datasets in a single session:
   ```python
   show(df1, df2, df3)
   ```

---

### Mini-Tutorial: Analyzing Data with PandasGUI
#### Step 1: Load the Dataset
Assuming you have a CSV file `data.csv`, you can load it as follows:
```python
df = pd.read_csv("data.csv")
show(df)
```

#### Step 2: Visualize the Data
Once the GUI opens:
- Click on the Plots tab.
- Select X-axis and Y-axis values.
- Choose a plot type (e.g., scatter plot, histogram).
- Click Generate Plot.

#### Step 3: Edit Data
- Click on any cell to modify its value.
- Use the right-click menu to delete or duplicate rows.

#### Step 4: Export the Changes
Once you've modified the data, save it:
```python
df.to_csv("updated_data.csv", index=False)
```

---

### Conclusion
PandasGUI is a powerful and intuitive tool for exploring and analyzing Pandas DataFrames with minimal coding effort. It is especially useful for data analysts who prefer a GUI-based approach to handling data.

Would you like to see an example of how PandasGUI generates Python scripts based on GUI interactions? 🚀