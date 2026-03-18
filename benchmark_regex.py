import timeit

setup = """
from researchclaw.experiment.sandbox import extract_paired_comparisons

stdout = '''PAIRED: method_A vs baseline_B regime=test mean_diff=1.0 std_diff=0.1 t_stat=2.0 p_value=0.05
PAIRED: method_C vs baseline_D regime=train mean_diff=-0.5 std_diff=0.2 t_stat=-1.5 p_value=0.10
''' * 10000
"""

stmt = """
extract_paired_comparisons(stdout)
"""

time_taken = timeit.timeit(stmt, setup=setup, number=100)
print(f"Time taken: {time_taken:.4f} seconds")
