import pytest
import os
import json
import re
import time
import functools

# ================= TIMING DECORATOR =================
def timer(func):
    @functools.wraps(func)   # 🔴 REQUIRED for pytest
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            end = time.time()
            print(f"\n⏱ TIME: {func.__name__} took {end - start:.4f} seconds")
    return wrapper


# ================= PATHS =================
JSON_PATH = r"C:\Users\chinna\Desktop\swathi.json"
OUTPUT_PATH = r"C:\Users\chinna\Desktop\s.txt"


# ================= UTILITY FUNCTIONS =================
def load_users(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"JSON file not found at: {path}")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["users"]


def extract_emails_from_file(path):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    with open(path, "r", encoding="utf-8") as f:
        return re.findall(pattern, f.read())


# ================= FIXTURE =================
@pytest.fixture(scope="module")
def users():
    try:
        return load_users(JSON_PATH)
    except FileNotFoundError as e:
        pytest.fail(f"[FIXTURE ERROR] {e}")


# ================= TESTS =================
@pytest.mark.positive
@timer
def test_max_age_user(users):
    max_user = max(users, key=lambda u: u["age"])
    print(f"\n[MAX AGE USER] {max_user['name']} → {max_user['age']}")
    assert max_user["age"] == 40


@pytest.mark.sort
@timer
def test_write_sorted_users(users):
    users_sorted = sorted(users, key=lambda u: u["age"])
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("Ascending order of age:\n")
        for u in users_sorted:
            f.write(f"{u['name']}, {u['age']}\n")
    assert os.path.exists(OUTPUT_PATH)


@pytest.mark.output
@timer
def test_print_output_file(users):
    print("\n--- OUTPUT FILE CONTENT ---")
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        print(f.read())
    print("--- END OF FILE ---")
    assert True


@pytest.mark.email
@timer
def test_email_extraction(users):
    emails = extract_emails_from_file(JSON_PATH)
    print("\n[EMAILS FOUND]")
    for e in emails:
        print("→", e)
    assert len(emails) == 5


@pytest.mark.negative
@timer
def test_path_negative():
    bad_path = r"C:\Users\chinna\Desktop\wrong.json"
    with pytest.raises(FileNotFoundError):
        load_users(bad_path)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (10, 5, 15),
        (0, 0, 0),
    ]
)
@pytest.mark.math
@timer
def test_add(a, b, expected):
    print(f"\n[ADD TEST] {a} + {b} = {expected}")
    assert a + b == expected
