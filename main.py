from extractors.wanted import extract_wandted_jobs

keyward = input("What do you want to search for?")

jobs = extract_wandted_jobs(keyward)

file = open(f"{keyward}.csv", "w")
file.write("Title,Company,Location,Reward,Link\n")

for job in jobs:
    file.write(f"{job['title']},{job['company_name']}, {job['location']}, {job['reward']}, {job['link']}\n")

file.close()