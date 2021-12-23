from passax.chrome import macos

mac = macos.ChromeMacOS("chrome", blank_passwords=False)
mac.get_macos()
mac.retrieve_database()
print(mac.pretty_print())