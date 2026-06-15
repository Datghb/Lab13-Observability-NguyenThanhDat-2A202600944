# Day 13 Observability Lab Report

> **Instruction**: Fill in all sections below. This report is designed to be parsed by an automated grading assistant. Ensure all tags (e.g., `[GROUP_NAME]`) are preserved.

## 1. Team Metadata
- [GROUP_NAME]: 
- [REPO_URL]: 
- [MEMBERS]:
  - Member A: [Name] | Role: Logging & PII
  - Member B: [Name] | Role: Tracing & Enrichment
  - Member C: [Name] | Role: SLO & Alerts
  - Member D: [Name] | Role: Load Test & Dashboard
  - Member E: [Name] | Role: Demo & Report

---

## 2. Group Performance (Auto-Verified)
- [VALIDATE_LOGS_FINAL_SCORE]: 100/100
- [TOTAL_TRACES_COUNT]: 10+ 
- [PII_LEAKS_FOUND]: 0
---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing
### 3.1 Logging & Tracing
- [EVIDENCE_CORRELATION_ID_SCREENSHOT]: docs/evidence/correlation-id.png
- [EVIDENCE_PII_REDACTION_SCREENSHOT]: docs/evidence/pii-redaction.png
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]: docs/evidence/langfuse-waterfall.png
- [TRACE_WATERFALL_EXPLANATION]: Trace shows the /chat agent run with metadata including hashed user_id, session_id, feature tag, model, token usage, and sanitized query preview.
- [EVIDENCE_TRACE_LIST_SCREENSHOT]: docs/evidence/langfuse-trace-list.png

- [ALERT_RULES_SCREENSHOT]: docs/evidence/alert-rules.png
- [SAMPLE_RUNBOOK_LINK]: docs/alerts.md#1-high-latency-p95
### 3.2 Dashboard & SLOs
- [DASHBOARD_6_PANELS_SCREENSHOT]: docs/evidence/dashboard.png
- [SLO_TABLE]:
| SLI | Target | Window | Current Value |
|---|---:|---|---:|
| Latency P95 | < 3000ms | 28d | |
| Error Rate | < 2% | 28d | |
| Cost Budget | < $2.5/day | 1d | |

### 3.3 Alerts & Runbook

- [ALERT_RULES_SCREENSHOT]: docs/evidence/alert-rules.png
- [SAMPLE_RUNBOOK_LINK]: docs/alerts.md#1-high-latency-p95

---

## 4. Incident Response (Group)
- [SCENARIO_NAME]: rag_slow
- [SYMPTOMS_OBSERVED]: P95 latency increased after enabling the rag_slow incident.
- [ROOT_CAUSE_PROVED_BY]: Langfuse trace and JSON logs with matching correlation_id showed slow retrieval behavior.
- [FIX_ACTION]: Disabled the rag_slow incident toggle.
- [PREVENTIVE_MEASURE]: Use high_latency_p95 alert and inspect traces before logs during latency incidents.
---

## 5. Individual Contributions & Evidence

### [MEMBER_A_NAME]
- [TASKS_COMPLETED]: 
- [EVIDENCE_LINK]: (Link to specific commit or PR)

### [MEMBER_B_NAME]
- [TASKS_COMPLETED]: 
- [EVIDENCE_LINK]: 

### [MEMBER_C_NAME]
- [TASKS_COMPLETED]: 
- [EVIDENCE_LINK]: 

### [MEMBER_D_NAME]
- [TASKS_COMPLETED]: 
- [EVIDENCE_LINK]: 

### [MEMBER_E_NAME]
- [TASKS_COMPLETED]: 
- [EVIDENCE_LINK]: 

---

## 6. Bonus Items (Optional)
- [BONUS_COST_OPTIMIZATION]: Used cost metrics from `/metrics` (`avg_cost_usd`, `total_cost_usd`) to monitor spend during load testing. Evidence: docs/evidence/dashboard.png
- [BONUS_AUDIT_LOGS]: Added separate audit logging to `data/audit.jsonl` for chat completion/failure and incident control events. Evidence: docs/evidence/audit-logs.png
- [BONUS_CUSTOM_METRIC]: Added and dashboarded `quality_avg` as a quality proxy metric. Evidence: docs/evidence/dashboard.png
