# :cake: Korean Bakery Sales - Preprocessing and Visualization (Python).
In this project, we are going to perform a data preprocessing and visualization of a Bakery Sales dataset from [kaggle]() using Python.

## :file_folder: Folders
| Folder Name                             | Description    |
|-----------------------------------------|----------------|
| [Images](https://github.com/radianlukman/Korean-Bakery-Sales/tree/main/Images)  | Images and Plots for README.md |

## :card_index: Files
- [Korean Bakery Sales Data](https://github.com/radianlukman/Korean-Bakery-Sales/blob/main/Bakery%20Sales.csv)

| File   Name                             | Description    |
|-----------------------------------------|----------------|
| [Bakery_Sales.ipynb](https://github.com/radianlukman/Korean-Bakery-Sales/blob/main/Bakery_Sales.ipynb)  | Full Project (Python Notebook) |
| [Bakery_Sales.py](https://github.com/radianlukman/Korean-Bakery-Sales/blob/main/Bakery%20Sales.py)  | Python Script |

## :hammer_and_wrench: Preprocessing
At first, the raw data is shown in the following figure:

![](https://github.com/radianlukman/Korean-Bakery-Sales/blob/main/Images/Uncleaned%20Data.jpg)

We can see that there are lots of NaN values, empty rows, and unnecessary columns. We need to clean the data first before processing it. 
The cleaned data can be seen in the following image:

![](https://github.com/radianlukman/Korean-Bakery-Sales/blob/main/Images/Cleaned%20Data.jpg)

You can view the full project (steps) [here](https://github.com/radianlukman/Korean-Bakery-Sales/blob/main/Bakery_Sales.ipynb).

## :chart_with_upwards_trend: Plots Preview
![](https://github.com/radianlukman/Korean-Bakery-Sales/blob/main/Images/Bakery%20Sales%20-%20Pie%20Chart.jpg)
![](https://github.com/radianlukman/Korean-Bakery-Sales/blob/main/Images/Bakery%20Sales%20-%20Bar%20Chart.jpg)
![](https://github.com/radianlukman/Korean-Bakery-Sales/blob/main/Images/Bakery%20Sales%20-%20Line%20Plot.jpg)

## :pushpin: Conclusion
1. The data that we obtained from Kaggle was raw data so we need to preprocess it first. There are six steps in preprocessing the data: deleting unnecessary rows & columns, replace NaN values with 0, change the datetime data type, combining rows that are on the same date, and make a "total" column that contains the sum of products sold.
2. The best-selling product in that bakery was angbutter which was sold 3.229 pieces or 29.79% of the total sales. There are also other best-selling products such as croissant, plain bread, and tiramisu croissant.
3. Sales trend at the bakery are unstable but still around average. There was a significant increase in sales during March 2020 but dropped again after that.



