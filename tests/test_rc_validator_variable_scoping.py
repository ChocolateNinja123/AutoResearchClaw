from researchclaw.experiment.validator import check_variable_scoping

def test_variable_scoping_basic():
    code = """
def my_func():
    if condition:
        x = 1
    print(x)
    """
    warnings = check_variable_scoping(code)
    assert len(warnings) == 1
    assert "Variable 'x' is assigned" in warnings[0]

def test_variable_scoping_no_issue():
    code = """
def my_func():
    x = 0
    if condition:
        x = 1
    print(x)
    """
    warnings = check_variable_scoping(code)
    assert len(warnings) == 0

def test_variable_scoping_nested():
    code = """
def my_func():
    if cond1:
        if cond2:
            x = 1
    print(x)
    """
    warnings = check_variable_scoping(code)
    assert len(warnings) == 1
    assert "Variable 'x' is assigned" in warnings[0]

def test_variable_scoping_tuple_assignment():
    code = """
def my_func():
    if cond:
        x, y = 1, 2
    print(x)
    """
    warnings = check_variable_scoping(code)
    assert len(warnings) == 1
    assert "Variable 'x' is assigned" in warnings[0]
