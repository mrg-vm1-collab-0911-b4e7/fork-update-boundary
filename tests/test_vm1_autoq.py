import os


def test_vm1_autoq_crossjob_identity():
    behavior = os.environ.get("VM1_AUTOQ_BEHAVIOR", "pass")
    run_index = int(os.environ.get("VM1_RUN_INDEX", "1"))
    if behavior == "flaky":
        assert run_index not in {2, 4}, f"VM1_AUTOQ_NOISY_FAILURE_{run_index}"
    elif behavior == "fail":
        assert False, "VM1_AUTOQ_SECURITY_FAILURE"
    else:
        assert True
