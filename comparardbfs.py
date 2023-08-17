#Compara los campos y tamaños de dos dbf's
#Just compares fields and field sizes between two pdf's

from dbfread import DBF

def compare_dbf_files(file1, file2):
    # Read the structure of the first DBF file
    table1 = DBF(file1)
    fields1 = [(field.name, field.type, field.length) for field in table1.fields]

    # Read the structure of the second DBF file
    table2 = DBF(file2)
    fields2 = [(field.name, field.type, field.length) for field in table2.fields]

    # Find the differences in fields
    fields_only_in_file1 = set(fields1) - set(fields2)
    fields_only_in_file2 = set(fields2) - set(fields1)

    # Print out the fields in each DBF file
    print(f"Fields in {file1}:")
    print_fields(fields1)
    print()

    print(f"Fields in {file2}:")
    print_fields(fields2)
    print()

    # Print the differences in structure
    print("Differences in structure:")
    if fields_only_in_file1:
        print(f"Fields only in {file1}:")
        print_fields(fields_only_in_file1)
        print()
    if fields_only_in_file2:
        print(f"Fields only in {file2}:")
        print_fields(fields_only_in_file2)
        print()

def print_fields(fields):
    for field_name, field_type, field_length in fields:
        print(f"{field_name} ({field_type}) - Size: {field_length}")

# Example usage
file1 = "movdias.dbf"
file2 = "enviar.dbf"
#file2 = "./src/structure.dbf"

compare_dbf_files(file1, file2)
