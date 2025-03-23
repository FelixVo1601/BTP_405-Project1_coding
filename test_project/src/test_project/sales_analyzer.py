# sales_analyzer.py
import numpy as np

# Sample sales data: daily revenue for a retail store over 30 days (in dollars)
SALES_DATA = [
    120.50, 150.75, 200.00, 180.25, 90.00, 110.30, 250.60, 300.00, 280.40, 190.20,
    175.80, 220.10, 130.90, 160.00, 210.50, 195.75, 230.00, 270.25, 140.00, 155.60,
    205.30, 240.00, 260.80, 185.40, 165.90, 225.00, 245.50, 290.00, 135.20, 170.80
]

def analyze_sales(data):
    # Convert list to numpy array for efficient computation
    sales_array = np.array(data)
    
    # Calculate statistics using numpy functions
    stats = {
        "average_sales": np.mean(sales_array),  # Average daily sales
        "std_dev_sales": np.std(sales_array),   # Standard deviation (variability)
        "max_sales": np.max(sales_array)        # Highest sales day
    }
    return stats

def format_results(stats):
    return (f"Average Daily Sales: ${stats['average_sales']:.2f}\n"
            f"Standard Deviation: ${stats['std_dev_sales']:.2f}\n"
            f"Maximum Daily Sales: ${stats['max_sales']:.2f}")

if __name__ == "__main__":
    # Analyze the sales data
    results = analyze_sales(SALES_DATA)
    
    # Print formatted results
    print("Sales Analysis Report")
    print("-" * 20)
    print(format_results(results))
    
    # Example of using a list comprehension (course concept) to find days above average
    avg = results["average_sales"]
    above_avg_days = len([sale for sale in SALES_DATA if sale > avg])
    print(f"Number of days with sales above average: {above_avg_days}")