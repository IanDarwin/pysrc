from collections import Counter
from pathlib import Path

# Path's rglob() is a Recursive Glob (like *nix find(1))
# and returns a Generator for matching Path objects
# Counter(iterable) returns a Map<iter_value,its_count>
file_counts = Counter(
    path.suffix for path in (Path.home() / "Downloads").rglob("*.*"))

print(file_counts)