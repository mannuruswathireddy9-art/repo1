import pytest
import os
import json
import re

# Correct actual path where file already exists
JSON_PATH = r"C:\Users\chinna\DESKTOP\swathi.json"
OUTPUT_PATH = r"C:\Users\chinna\DESKTOP\s.txt"

def load_users(path=JSON_PATH):
    if not os.path.exists(path):
        pytest.fail(f"[FAIL] JSON file not found at: {path}")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["users"]

def extract_emails_from_file(path=JSON_PATH):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    with open(path, "r", encoding="utf-8") as f:
        return re.findall(pattern, f.read())

@pytest.fixture(scope="module")
def users():
    return load_users(JSON_PATH)

def test_max_age_user(users):
    max_user = max(users, key=lambda u: u["age"])
    print(f"\n[MAX AGE USER] {max_user['name']} → {max_user['age']} years")
    assert max_user["age"] == 40
    print("[PASS] Max age user validated")

def test_write_sorted_users(users):
    users_sorted = sorted(users, key=lambda u: u["age"])
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("ascending order of age:\n")
        for u in users_sorted:
            f.write(f"{u['name']},{u['age']}\n")

    print(f"\n[WRITE] Output saved to: {OUTPUT_PATH}")
    assert os.path.exists(OUTPUT_PATH)
    print("[PASS] Sorting + file write validated")

def test_print_output_file(users):
    print("\n--- Output File Content ---")
    print(open(OUTPUT_PATH, "r", encoding="utf-8").read())
    print("--- End of File ---")

def test_email_extraction(users):
    emails = extract_emails_from_file(JSON_PATH)
    print("\n[EMAILS FOUND]")
    for e in emails:
        print(" →", e)
    assert len(emails) == 5
    print("[PASS] Email extraction validated")

def test_path_negative():
    bad_path = r"C:\Users\chinna\DESKTOP\wrong.json"
    assert not os.path.exists(bad_path)
    if not os.path.exists(bad_path):
        pytest.fail(f"[FAIL] JSON file not found at: {bad_path}")
