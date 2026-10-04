import json

from part4_agent.agent_runner import run_agent, save_json


results = [
    {
        "category": "Ethnic Wear",
        "previous_month": "May",
        "current_month": "June",
        "previous_revenue": 185107.61,
        "current_revenue": 76371.53,
        "mom_pct": -58.74,
        "status": "flagged"
    },
    {
        "category": "Home & Kitchen",
        "previous_month": "May",
        "current_month": "June",
        "previous_revenue": 91152.57,
        "current_revenue": 129971.22,
        "mom_pct": 42.59,
        "status": "flagged"
    },
    {
        "category": "Kids Wear",
        "previous_month": "May",
        "current_month": "June",
        "previous_revenue": 45793.78,
        "current_revenue": 56737.78,
        "mom_pct": 23.90,
        "status": "flagged"
    },
    {
        "category": "Western Wear",
        "previous_month": "May",
        "current_month": "June",
        "previous_revenue": 86998.18,
        "current_revenue": 97415.64,
        "mom_pct": 11.97,
        "status": "flagged"
    }
]


output = run_agent([], results)

save_json(output, "agent_output.json")

print("Agent output saved successfully.")