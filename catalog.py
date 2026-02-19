import json
import random

def get_random_domain_and_subskill():
    with open("inputs/tcm_catalog.json") as f:
        data = json.load(f)

    domain = random.choice(data["domains"])
    subskill = random.choice(domain["subskills"])

    return domain["name"], subskill
