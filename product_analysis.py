import pandas as pd


# =========================
# 1. Load data
# =========================

df = pd.read_csv("user_activity.csv")

df["date"] = pd.to_datetime(df["date"])


# =========================
# 2. Main KPIs
# =========================

total_users = df["user_id"].nunique()

active_users = df.loc[
    df["event_type"] == "login",
    "user_id"
].nunique()

payment_users = df.loc[
    df["event_type"] == "payment",
    "user_id"
].nunique()

payment_df = df[df["event_type"] == "payment"].copy()

total_payment_volume = payment_df["amount"].sum()

payment_count = len(payment_df)

average_payment_amount = payment_df["amount"].mean()

conversion_rate = (
    payment_users / active_users * 100
    if active_users > 0
    else 0
)


kpi_df = pd.DataFrame({
    "metric": [
        "Total Users",
        "Active Users",
        "Payment Users",
        "Conversion Rate (%)",
        "Payment Count",
        "Total Payment Volume",
        "Average Payment Amount"
    ],
    "value": [
        total_users,
        active_users,
        payment_users,
        round(conversion_rate, 2),
        payment_count,
        total_payment_volume,
        round(average_payment_amount, 2)
    ]
})


# =========================
# 3. Daily Active Users
# =========================

dau = (
    df[df["event_type"] == "login"]
    .groupby("date")["user_id"]
    .nunique()
    .reset_index(name="DAU")
)


# =========================
# 4. Daily payment dynamics
# =========================

daily_payments = (
    payment_df
    .groupby("date")
    .agg(
        payment_count=("user_id", "count"),
        payment_volume=("amount", "sum")
    )
    .reset_index()
)


# =========================
# 5. Channel analytics
# =========================

channel_activity = (
    df.groupby("channel")
    .agg(
        event_count=("event_type", "count"),
        unique_users=("user_id", "nunique")
    )
    .reset_index()
)


channel_payments = (
    payment_df
    .groupby("channel")
    .agg(
        payment_count=("user_id", "count"),
        payment_volume=("amount", "sum"),
        average_payment_amount=("amount", "mean")
    )
    .reset_index()
)

channel_payments["average_payment_amount"] = (
    channel_payments["average_payment_amount"]
    .round(2)
)


# =========================
# 6. Top users
# =========================

top_users = (
    payment_df
    .groupby("user_id")
    .agg(
        payment_count=("amount", "count"),
        payment_volume=("amount", "sum")
    )
    .reset_index()
    .sort_values(
        "payment_volume",
        ascending=False
    )
)


# =========================
# 7. User activity frequency
# =========================

user_activity = (
    df.groupby("user_id")
    .agg(
        total_events=("event_type", "count"),
        active_days=("date", "nunique")
    )
    .reset_index()
    .sort_values(
        ["active_days", "total_events"],
        ascending=False
    )
)


# =========================
# 8. User-level product funnel
# =========================

login_users = set(
    df.loc[
        df["event_type"] == "login",
        "user_id"
    ]
)

payment_users_set = set(
    df.loc[
        df["event_type"] == "payment",
        "user_id"
    ]
)

funnel_df = pd.DataFrame({
    "stage": [
        "Active Users",
        "Payment Users"
    ],
    "users": [
        len(login_users),
        len(payment_users_set)
    ]
})

funnel_df["conversion_from_active_%"] = [
    100,
    round(conversion_rate, 2)
]


# =========================
# 9. Export to Excel
# =========================

output_file = "product_analysis_results.xlsx"

with pd.ExcelWriter(
    output_file,
    engine="openpyxl"
) as writer:

    kpi_df.to_excel(
        writer,
        sheet_name="KPIs",
        index=False
    )

    dau.to_excel(
        writer,
        sheet_name="DAU",
        index=False
    )

    daily_payments.to_excel(
        writer,
        sheet_name="Daily Payments",
        index=False
    )

    channel_activity.to_excel(
        writer,
        sheet_name="Channel Activity",
        index=False
    )

    channel_payments.to_excel(
        writer,
        sheet_name="Channel Payments",
        index=False
    )

    top_users.to_excel(
        writer,
        sheet_name="Top Users",
        index=False
    )

    user_activity.to_excel(
        writer,
        sheet_name="User Activity",
        index=False
    )

    funnel_df.to_excel(
        writer,
        sheet_name="Funnel",
        index=False
    )


print("Analysis completed successfully.")
print(f"Results saved to: {output_file}")
