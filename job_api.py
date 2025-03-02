import csv
from jobspy import scrape_jobs
import os
import datetime

def find_job(role, country, location):
    # Generate a unique filename with a timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{role.replace(' ', '_')}_{location.replace(' ', '_')}_{timestamp}.csv"

    # Print the current working directory
    print(f"Current working directory: {os.getcwd()}")

    # Scrape job information from multiple websites
    jobs = scrape_jobs(
        site_name=["indeed", "linkedin", "glassdoor"],
        search_term=role,
        location=location,
        results_wanted=20,
        hours_old=72,  # (only Linkedin/Indeed is hour specific, others round up to days old)
        country_indeed=country,  # only needed for indeed / glassdoor
    )

    # Save the jobs DataFrame to a CSV file
    jobs.to_csv(filename, quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)
    print(f"CSV saved as {filename}")


    return filename
