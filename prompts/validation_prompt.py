VALIDATION_RULES = """
1. **Wrong Expiry Date Check**
   - From the dataset fetched via TML API:
     - For each row:
       - Compute: `Expected Validity End Date = Renewal Date + 365 days`
       - Compare with actual `Validity End Date`
       - If mismatch, flag the entry with "Wrong Expiry Date"

"""
