from RPA.Robocorp.Vault import Vault

VAULT = Vault()


def reading_secrets():
    print(f"My secrets: {VAULT.get_secret('credentials')}")


def modifying_secrets():
    secret = VAULT.get_secret("credentials")
    secret["username"] = "nobody"
    secret.set_secret(secret)


reading_secrets()
