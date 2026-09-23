import os
import subprocess
import sys


def _set_mergify_language(request, language: str) -> None:
    plugin = request.config.pluginmanager.get_plugin("PytestMergify")
    assert plugin is not None, "pytest-mergify plugin missing"
    attrs = plugin.mergify_ci.resource_attributes
    assert attrs is not None, "Mergify CI resource attributes unavailable"
    attrs["telemetry.sdk.language"] = language


def test_vm1_autoq_crossjob_identity(request):
    nested_language = os.environ.get("VM1_LANG_NESTED")
    language = nested_language or "ruby"
    _set_mergify_language(request, language)

    if nested_language is None:
        env = os.environ.copy()
        env["VM1_LANG_NESTED"] = "nodejs"
        env["VM1_AUTOQ_BEHAVIOR"] = "pass"
        subprocess.run(
            [sys.executable, "-m", "pytest", "-q", __file__],
            env=env,
            check=True,
        )

    assert True
