import math
import pytest
from noema.accounting import FixedEnvelope

@pytest.mark.parametrize("bad",[math.nan, math.inf, -math.inf])
def test_nonfinite_cpu_limit_never_admitted(bad):
    with pytest.raises(ValueError, match="finite"):
        FixedEnvelope(
            max_resident_memory_bytes=1000, max_durable_state_bytes=1000,
            max_update_cpu_seconds_per_event=bad,
            max_query_cpu_seconds_per_event=1.0,
            max_shadow_auditions_per_event=1,
        )
