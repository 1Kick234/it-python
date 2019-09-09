def banner(subject, author):
    byline = f"By {author}"
    banner_length = max(len(subject), len(byline)) + 4
    print("=" * banner_length)
    print(f"|{subject:^{banner_length-2}}|")
    print(f"|{byline:^{banner_length-2}}|")
    print("=" * banner_length)
banner("Time Machine", "Rocket Man")