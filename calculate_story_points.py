import pandas as pd

def calculate_total_story_points(file_path):
  """Calculates the total story points from a product backlog Excel file.

  Args:
    file_path: Path to the Excel file.

  Returns:
    Total story points.
  """

  df = pd.read_excel(file_path)
  total_story_points = df['Story Points'].sum()
  return total_story_points

if __name__ == "__main__":
  file_path = 'product_backlog.xlsx'
  total_points = calculate_total_story_points(file_path)
  print("Total story points:", total_points)
  print("More Upgradation is coming soon...")
