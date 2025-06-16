# Debt To Income

Below is a concise “starter payload” you can use for a Debt-to-Income calculator.
Each **key** is the dictionary field name the app expects from the user (or will populate after the computation); the **value** shown is just a placeholder illustrating the data type.

```python
dti_payload = {
    # --- identity / metadata (optional but handy) ---
    "user_id": "",                # str – internal identifier
    "first_name": "",             # str – optional display name
    "last_name": "",              # str

    # --- income ---
    "gross_monthly_income": 0.0,  # float – pre-tax income for the month

    # --- recurring monthly debt payments ---
    "monthly_rent_or_mortgage": 0.0,
    "auto_loan_payments": 0.0,
    "student_loan_payments": 0.0,
    "credit_card_payments": 0.0,  # total of all cards’ minimums
    "personal_loan_payments": 0.0,
    "child_support_alimony": 0.0,
    "other_debt_payments": 0.0,   # catch-all for anything not listed above

    # --- output ---
    "dti_ratio": None             # float – calculated later (% or decimal)
}
```

### Why these keys?

| Group        | Key(s)                               | Reason                                                                                                                                                       |
| ------------ | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Identity** | `user_id`, `first_name`, `last_name` | Lets you cache results per user and show friendly messages.                                                                                                  |
| **Income**   | `gross_monthly_income`               | DTI is based on *gross* (pre-tax) income; easier for users to supply monthly rather than annual.                                                             |
| **Debts**    | Each payment category                | Lenders usually include these items in DTI screens. Splitting them out helps with validation and future analytics (e.g., “where do users carry most debt?”). |
| **Output**   | `dti_ratio`                          | Store the computed result in the same dict so downstream steps (e.g., scoring, UI display, DB insert) can treat it as a single object.                       |

Feel free to add or drop fields (e.g., separate `primary_income` and `secondary_income`, or break out multiple mortgages) as your use-case evolves, but this list will get a basic calculator up and running.
