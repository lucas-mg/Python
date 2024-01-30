import subprocess
import json
from datetime import datetime

def get_instance_creation_dates():
    # Run gcloud command to get a list of instances in JSON format
    command = "gcloud compute instances list --format=json"
    output = subprocess.check_output(command, shell=True).decode("utf-8")

    # Parse JSON output
    instances = json.loads(output)

    # Extract instance names and creation dates
    instance_info = {}
    for instance in instances:
        instance_name = instance["name"]
        creation_timestamp = instance["creationTimestamp"]
        creation_date = datetime.strptime(creation_timestamp, "%Y-%m-%dT%H:%M:%S.%f%z")
        instance_info[instance_name] = creation_date

    return instance_info

if __name__ == "__main__":
    instance_info = get_instance_creation_dates()

    if instance_info:
        print("Instances and their creation dates:")
        for instance, creation_date in sorted(instance_info.items(), key=lambda x: x[1]):
            print(f"{instance}: {creation_date.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("No instances found.")
###DON'T FORGET DO CHANGE PERMISSION USING CHMOD
