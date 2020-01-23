import csv

groups = [
  [],
  [],
  [],
  []
]

def grouper(num_of_groups):
    groups = []
    for i in range(0, num_of_groups):
        groups.append([])

    with open('emails.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            email = row[0]
            email_group = hash(email) % num_of_groups
            groups[email_group].append(email)

    return groups

def writer(groups):
    for idx, group in enumerate(groups):
        with open(f'group{idx}.csv', 'w') as csvfile:
            email_writer = csv.writer(csvfile)
            for email in group:
                email_writer.writerow([email])

groups = grouper(4)
writer(groups)
