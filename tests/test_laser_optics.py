import pytest
import game.laser_optics as mod

CASES = [
    ("mirror_angle_auth_interp", (1,)),
    ("reflection_depth_unify", (1,)),
    ("barrier_registry_fence", (1,)),
    ("optic_state_migrate", (1,)),
    ("critical_angle_consistent", (1,)),
    ("optic_version_rollback", (1,)),
    ("load_room_optics", (1,)),
    ("rotate_mirror", (1,)),
    ("trace_laser", (1,)),
    ("present_laser", (1,)),
    ("validate_laser", (1,)),
    ("metrics_laser", (1,)),
    ("audit_laser", (1,)),
    ("fallback_laser", (1,)),
    ("determinism_laser", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
