# Mock Debug Q&A

## Correlation IDs

Q: Where is the correlation ID created and propagated?

A: `CorrelationIdMiddleware` clears request context, reuses `x-request-id` when provided, otherwise generates `req-<8 hex>`. It binds the ID into structlog contextvars, stores it on `request.state`, and returns it in the `x-request-id` response header.

Q: How do you prove correlation ID propagation works?

A: Send multiple `/chat` requests, then run `python scripts/validate_logs.py`. The validator should report at least two unique correlation IDs and a final score of 100/100.

## PII Redaction

Q: Where is PII scrubbed?

A: `scrub_event` in `app/logging_config.py` runs before JSON rendering and recursively scrubs string values in the log event dictionary.

Q: What PII patterns are covered?

A: Email addresses, Vietnam phone numbers, CCCD-style 12 digit IDs, credit card numbers, passport-like IDs, and simple address fields using `address:` or `dia chi:`.

## Metrics to Traces to Logs

Q: How would you debug a latency incident?

A: Start from `/metrics` and confirm P95 latency is high, open the slowest Langfuse trace to identify whether RAG or LLM spans dominate, then inspect logs with the same correlation ID for feature, session, and sanitized message context.

Q: How would you debug an error-rate incident?

A: Check `/metrics` error breakdown, inspect failed traces, then filter JSON logs by `error_type` and `correlation_id` to find the failing request path.

## SLOs and Alerts

Q: What are the required dashboard panels?

A: Latency P50/P95/P99, traffic, error rate, cost, tokens in/out, and quality score.

Q: What alerts are configured?

A: High latency P95, high error rate, and cost budget spike. Each alert has a runbook link in `config/alert_rules.yaml`.
