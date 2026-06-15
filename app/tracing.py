from __future__ import annotations

import os
from typing import Any

from dotenv import load_dotenv

load_dotenv()

if os.getenv("LANGFUSE_BASE_URL") and not os.getenv("LANGFUSE_HOST"):
    os.environ["LANGFUSE_HOST"] = os.getenv("LANGFUSE_BASE_URL", "")

os.environ.setdefault("LANGFUSE_TIMEOUT", "15")
os.environ.setdefault("LANGFUSE_FLUSH_AT", "1")
os.environ.setdefault("LANGFUSE_FLUSH_INTERVAL", "1")

try:
    from langfuse import get_client, observe
except Exception:  # pragma: no cover
    def observe(*args: Any, **kwargs: Any):
        def decorator(func):
            return func
        return decorator

    class _DummyContext:
        def update_current_trace(self, **kwargs: Any) -> None:
            return None

        def update_current_observation(self, **kwargs: Any) -> None:
            return None

        def flush(self) -> None:
            return None

    langfuse_context = _DummyContext()
else:
    class _LangfuseContext:
        def update_current_trace(self, **kwargs: Any) -> None:
            get_client().update_current_trace(**kwargs)

        def update_current_observation(self, **kwargs: Any) -> None:
            get_client().update_current_generation(**kwargs)

        def flush(self) -> None:
            get_client().flush()

    langfuse_context = _LangfuseContext()


def tracing_enabled() -> bool:
    return bool(os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY"))
