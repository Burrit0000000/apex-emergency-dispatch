# Apex Dispatch: Post-Sale Client Onboarding Playbook

This document outlines the exact step-by-step workflow for onboarding a paying contractor after they complete checkout.

---

## 1. Instant Post-Payment Intake
As soon as the $500 payment clears on Stripe, the client is redirected to the confirmation screen or receives an automated welcome email with this simple 4-question intake:

1. **Company Greeting Name:** (e.g., *"Nick's Plumbing & Air Conditioning"*)
2. **Primary On-Call Technician Mobile Number:** (For instant SMS dispatch alerts)
3. **Backup / Owner Mobile Number:** (For escalation if primary doesn't answer)
4. **Primary Service Area:** (e.g., *"Greater Houston Metro / Harris County"*)

---

## 2. Fulfillment Checklist (Internal - 3 Minutes)
- [ ] Buy dedicated local area code number in Vapi ($1.15).
- [ ] Duplicate master Emma assistant -> rename to `[Client Name] Dispatch`.
- [ ] Customize greeting: *"Thank you for calling [Company Name] Emergency Services, this is Emma..."*
- [ ] Assign phone number to assistant.
- [ ] Set notification email / webhook to technician's mobile.
- [ ] Place one test call to verify audio quality.

---

## 3. The Activation & Handoff Email (Sent to Contractor)

**Subject:** Your Apex 24/7 Dispatch line is LIVE!

Hey [Owner Name],

Welcome aboard! Your dedicated 24/7 emergency dispatch line has been provisioned and custom-trained for [Company Name]:

📞 **Your Dedicated Forwarding Number:** [Dedicated Number]
📱 **Dispatches Routed To:** [Technician Mobile]

### How to Route Your Calls (Takes 60 Seconds):
Simply set your office phone provider to **conditionally forward after-hours or unanswered calls** to your dedicated number above:
- **RingCentral / Nextiva / VOIP:** Go to *Settings -> Call Handling -> After Hours -> Forward to External Number*.
- **Comcast / Spectrum / Landline:** Use your portal or carrier star-code (typically `*71` or `*72` + dedicated number).

Whenever a customer calls after hours, Emma answers on the first ring, verifies the address, and immediately shoots the customer details to your on-call cell phone.

You are 100% covered 24/7/365. Reply to this email anytime if you need adjustments to your routing rules.

Best regards,  
Xenia  
Apex Dispatch Systems  
support@apexdispatchai.com

---

## 4. The "First Win" Retention Email
Sent after Emma captures their first active emergency job:

**Subject:** 🚨 First emergency job captured!

Hey [Owner Name],

Emma just fielded an emergency call from [Customer Name] at [Customer Address] and dispatched the lead to your crew.

A single emergency job like this easily covers your entire Apex service for the year. Glad to have you on the network!
