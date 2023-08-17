import openpyxl
def extract_area_perimeter(file_name):
    #load the excel file
    workbook = openpyxl.load_workbook(file_name)
    sheet = workbook.active

    #dictionary to store column names and formulas
    formulas_dict = {}

    for column in sheet.iter_cols(min_row=1, max_row=1, values_only=True):
        for col_name in column:
            if col_name:
                area_formula = f'=A1*B1'  #area formula
                perimeter_formula = f'=2*(A1+B1)'  #perimeter formula

                formulas_dict[col_name] = {
                    'area': area_formula,
                    'perimeter': perimeter_formula
                }

    return formulas_dict
# Example usage
file_name = 'area_and_perimeter.xlsx'  # replace with your ebxcel files name
formulas = extract_area_perimeter(file_name)
print(formulas)
