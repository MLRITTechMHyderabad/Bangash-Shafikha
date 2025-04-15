import pandas as pd

# Load the CSV file
file_path = "task.csv"  # Replace with your path if running locally
df = pd.read_csv(file_path)

# Original number of records
original_count = len(df)

# Remove duplicates based on 'uuid', keeping the first occurrence
df_no_duplicates = df.drop_duplicates(subset='uuid', keep='first')
duplicates_removed = original_count - len(df_no_duplicates)

# Identify rows with missing values (either empty or NaN) in firstname, surname, or email
incomplete_records = df_no_duplicates[
    df_no_duplicates[['firstname', 'surname', 'email']].isnull().any(axis=1) |
    (df_no_duplicates[['firstname', 'surname', 'email']] == '').any(axis=1)
]

# Remaining records are clean
complete_records = df_no_duplicates.drop(incomplete_records.index)

# Count of incomplete records
missing_values_count = len(incomplete_records)

# Save cleaned and incomplete datasets
complete_records.to_csv("cleaned_users_data.csv", index=False)
incomplete_records.to_csv("incomplete_users_data.csv", index=False)

# Output the results
print(f"Duplicates removed: {duplicates_removed}")
print(f"Records with missing values: {missing_values_count}")