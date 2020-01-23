import csv

groups = [
  [],
  [],
  [],
  []
]

def grouper():
  with open('emails.csv') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
          email = row[0]
          email_group = hash(email) % 4
          groups[email_group].append(email)

def writer():
    for idx, group in enumerate(groups):
        with open(f'group{idx}.csv', 'w') as csvfile:
            email_writer = csv.writer(csvfile)
            for email in group:
                email_writer.writerow([email])

grouper()
writer()
