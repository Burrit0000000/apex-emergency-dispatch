#!/usr/bin/env python3
"""
Lead Machine: Contractor Prospect Database Generator
Curates targeted emergency contractors (Water Damage Restoration & Emergency Plumbing)
in high-ticket metro areas.
"""

import json
import csv
import os

SAMPLE_PROSPECTS = [
    {
        "company": "Apex Disaster Specialists",
        "trade": "Water Damage & Restoration",
        "city": "Dallas",
        "state": "TX",
        "phone": "(214) 555-0192",
        "estimated_job_value": "$4,500",
        "current_status": "Voicemail after 6 PM",
        "pitch_angle": "Missed freeze / burst pipe emergencies"
    },
    {
        "company": "Lone Star 24/7 Plumbing",
        "trade": "Emergency Plumbing",
        "city": "Fort Worth",
        "state": "TX",
        "phone": "(817) 555-0144",
        "estimated_job_value": "$2,800",
        "current_status": "Manual call forwarding to owner cell",
        "pitch_angle": "Owner burnout / dinner interruptions"
    },
    {
        "company": "Sunstate Rapid Mitigation",
        "trade": "Water Extraction & Mold",
        "city": "Phoenix",
        "state": "AZ",
        "phone": "(602) 555-0183",
        "estimated_job_value": "$5,200",
        "current_status": "Voicemail after 5 PM",
        "pitch_angle": "High-cost Google LSA ad waste"
    },
    {
        "company": "Peach State Emergency Rooter",
        "trade": "Emergency Sewer & Drain",
        "city": "Atlanta",
        "state": "GA",
        "phone": "(404) 555-0167",
        "estimated_job_value": "$3,200",
        "current_status": "Traditional answering service (slow)",
        "pitch_angle": "Replacing $600/mo answering service with instant AI"
    },
    {
        "company": "Gulf Coast Flood Response",
        "trade": "Flood & Storm Restoration",
        "city": "Houston",
        "state": "TX",
        "phone": "(713) 555-0128",
        "estimated_job_value": "$6,500",
        "current_status": "Voicemail on weekends",
        "pitch_angle": "Weekend lead leakage to national franchises"
    },
    {
        "company": "Mile High Pipe & Drain",
        "trade": "Emergency Plumbing",
        "city": "Denver",
        "state": "CO",
        "phone": "(303) 555-0199",
        "estimated_job_value": "$3,800",
        "current_status": "Voicemail during peak hours",
        "pitch_angle": "Winter freeze response time"
    },
    {
        "company": "Biscayne Water & Mold Pros",
        "trade": "Water Damage Restoration",
        "city": "Miami",
        "state": "FL",
        "phone": "(305) 555-0171",
        "estimated_job_value": "$5,800",
        "current_status": "Owner cell rings out",
        "pitch_angle": "Condo / high-rise emergency leak triage"
    },
    {
        "company": "Carolina Rapid Restoration",
        "trade": "Emergency Water Mitigation",
        "city": "Charlotte",
        "state": "NC",
        "phone": "(704) 555-0115",
        "estimated_job_value": "$4,200",
        "current_status": "Voicemail after 7 PM",
        "pitch_angle": "After-hours commercial water leaks"
    }
]

def export_leads():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "contractor_targets.json")
    csv_path = os.path.join(base_dir, "contractor_targets.csv")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(SAMPLE_PROSPECTS, f, indent=2)

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=SAMPLE_PROSPECTS[0].keys())
        writer.writeheader()
        writer.writerows(SAMPLE_PROSPECTS)

    print(f"Exported {len(SAMPLE_PROSPECTS)} high-value contractor targets to {json_path} and {csv_path}")

if __name__ == "__main__":
    export_leads()
