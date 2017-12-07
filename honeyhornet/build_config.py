class BuildConfig:
    def __init__(self):
        with open("config.yml", "w") as config_file:
            config_file.write("# Configuration file for Honey Hornet.\n"
                              "# Defines the type of scan to run.\n"
                              "# Uncomment one option only.\n"
                              "scanType:\n"
                              "  #- 1  # Port Scan\n"
                              "  - 2  # Check Credentials\n"
                              "# File path to save the reports\n"
                              "reportFilePath: ~/path/to/reports\n"
                              "resultsFormat:\n"
                              "  - csv\n"
                              "  - json\n"
                              "# Uncomment to do banner grabs on HTTP ports.\n"
                              "bannerGrab: False\n"
                              "# Ports to scan on each target.\n"
                              "ports:\n"
                              "  - 21\n"
                              "  - 22\n"
                              "  - 23\n"
                              "  - 2332\n"
                              "  - 9191\n"
                              "  #- 9443\n"
                              "# Users to test when running in Check Credentials mode.\n"
                              "users:\n"
                              "  #- admin\n"
                              "  # - root\n"
                              "  - user\n"
                              "  - viewer\n"
                              "# Blank User\n"
                              "  # - ''\n"
                              "# Passwords to test when running in Check Credentials mode.\n"
                              "passwords:\n"
                              "  # - admin\n"
                              "  # - camera\n"
                              "  - 12345\n"
                              "# Blank Password\n"
                              "  # - ''\n"
                              "# Path to list of targets for scanning.\n"
                              "targets:\n"
                              "# Must be in the same folder as main program.\n"
                              "  - targets.txt")