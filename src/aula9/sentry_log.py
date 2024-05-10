import sentry_sdk

sentry_sdk.init(
    dsn="""https://5775b1c52c2d0ef0b75c860729536ece@o4507232464535552.
    ingest.us.sentry.io/4507232467353600""",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

division_by_zero = 1 / 0
