import json

POLICIES = [
    {"key": "info_security_policy", "title": "Information Security Policy"},
    {"key": "access_control_policy", "title": "Access Control Policy"},
    {"key": "password_auth_policy", "title": "Password and Authentication Policy"},
    {"key": "incident_response_policy", "title": "Incident Response Policy"},
    {"key": "change_management_policy", "title": "Change Management Policy"},
    {"key": "vendor_management_policy", "title": "Vendor Management Policy"},
    {"key": "risk_assessment_policy", "title": "Risk Assessment Policy"},
    {"key": "backup_dr_policy", "title": "Backup and Disaster Recovery Policy"},
    {"key": "data_retention_policy", "title": "Data Retention and Disposal Policy"},
    {"key": "acceptable_use_policy", "title": "Acceptable Use Policy"},
]

SYSTEM_PROMPT = """You are a senior SOC2 compliance consultant and technical writer.

Write SOC2-ready policy documents that are professional, clear, structured, and realistic.

Important:
- Do NOT write legal advice.
- Do NOT include placeholders like [Company Name] unless missing from input.
- Do NOT make claims the company did not confirm.
- Use confident, positive language.
- If information is missing, choose the safest common best practice and clearly state it as the organization's standard.
- Output must be in clean Markdown with headings.
- Avoid fluff.
"""


def build_policy_prompt(policy_name: str, company_profile: dict) -> str:
    company_json = json.dumps(company_profile, indent=2, ensure_ascii=False)

    return f"""Create a SOC2-ready policy document for the company described below.

Policy Name: {policy_name}

Company Context (JSON):
{company_json}

Requirements:
1) Write the policy in a confident, optimistic tone (the company is organized and security-conscious).
2) Do NOT invent tools, vendors, or processes not mentioned in the company context.
3) If a detail is missing, choose a widely accepted best practice and present it as the organization's standard operating procedure.
4) Include the following sections exactly in this order:

# 1. Purpose
# 2. Scope
# 3. Definitions (keep short)
# 4. Roles and Responsibilities
# 5. Policy Statements
# 6. Procedures (step-by-step)
# 7. Monitoring and Enforcement
# 8. Exceptions
# 9. Review and Maintenance
# 10. Approval

5) Under “Policy Statements”, use bullet points and be specific.
6) Keep the document between 900 and 1400 words.
7) End with a short “Document Control” table with:
- Version
- Effective Date
- Next Review Date
- Owner
- Approved By

Output format: Markdown only.
"""
