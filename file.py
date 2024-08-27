import csv

def save_to_csv(jobs):

    with open("./to_save.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)

        csv_writer.writerow(["No", "공고", "사명", "장소", "참조"]
                            )
        
        for index, job in enumerate(jobs):
            csv_writer.writerow([index + 1, job["title"], job["company"], job["location"], job["link"]])
