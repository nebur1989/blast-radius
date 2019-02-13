def go_to_latest_dir():
    all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]
    latest_subdir = max(all_subdirs, key=os.path.getmtime)
    os.chdir(latest_subdir)


def go_to_terragrunt_cache():
    os.chdir('.terragrunt-cache')
    go_to_latest_dir()
    go_to_latest_dir()
    print(os.getcwd())
