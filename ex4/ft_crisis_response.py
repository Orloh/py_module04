# *************************************************************************** # #
#                                                        :::      ::::::::    #
#    ft_crisis_response.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/29 01:04:01 by orhernan         #+#    #+#              #
#    Updated: 2026/03/29 01:36:08 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


def crisis_handler(vault_name: str) -> None:
    """
    Implements a crisis handler function for archive operations.
    Manages missing archives, security violations and standard access.
    """
    attempt_msg = f"Attempting access to '{vault_name}'..."

    try:
        with open(vault_name, mode="r", encoding="utf-8") as vault:
            data = vault.read().strip()
        print(f"ROUTINE ACCESS: {attempt_msg}")
        print(f"SUCCESS: Archive recovered - '{data}'")
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print(f"CRISIS ALERT: {attempt_msg}")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print(f"CRISIS ALERT: {attempt_msg}")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception as error:
        print(f"CRISIS ALERT: {attempt_msg}")
        print(f"RESPONSE: Unexpected system anomaly: {error}")
        print("STATUS: Crisis handled, system stable")
    finally:
        print()


def main() -> None:
    """
    Main entry point for testing Crisis Response protocols.
    """
    print("=== CYBER ARCHIVES CRISIS RESPONSE SYSTEM ===")
    print()
    vault_names = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]

    for vault in vault_names:
        crisis_handler(vault)

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
