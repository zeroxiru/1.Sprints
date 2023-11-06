import json

# Sample data
sample_data = [{
    "author": "F. Scott Fitzgerald",
    "id": 1,
    "title": "The Great Gatsby"
  },
  {
    "author": "George Orwell",
    "id": 2,
    "title": "1984"
  },
  {
    "author": "Harper Lee",
    "id": 3,
    "title": "To Kill a Mockingbird"
  }]

# Generate 200 samples
samples = []

for i in range(1, 201):
    # Create a copy of the sample data
    for entry in sample_data:
        sample_entry = entry.copy()

        # Set the ID for each entry
        sample_entry["id"] += i - 1

        # Append the sample entry to the list of samples
        samples.append(sample_entry)

# Save the generated samples to a JSON file
with open('sample_data.json', 'w') as json_file:
    json.dump(samples, json_file, indent=4)

print("Samples saved to sample_data.json")
