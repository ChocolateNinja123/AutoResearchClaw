import timeit
from researchclaw.pipeline.executor import _extract_multi_file_blocks

text = """
Some text
```filename:main.py
import os
print(os.environ)
```

```python
filename:utils.py
def hello():
    pass
```
"""

def bench():
    _extract_multi_file_blocks(text)

if __name__ == "__main__":
    n = 10000
    t = timeit.timeit(bench, number=n)
    print(f"Baseline: {t / n * 1000000:.2f} µs per call")
