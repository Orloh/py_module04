# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_vault_security.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/28 23:46:52 by orhernan         #+#    #+#              #
#    Updated: 2026/03/29 00:52:04 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


def secure_archive(
    file_name: str,
    mode: str = "r",
    content: str | None = None
) -> tuple[bool, str]:
    try:
        if mode in ("r", "read"):
            with open(file_name, "r") as vault:
                data = vault.read()
                return (True, data)

        elif mode in ("w", "write"):
            if content is None:
                return (
                    False,
                    "Error: Write action requested but no content provided"
                )
            with open(file_name, "w") as vault:
                vault.write(content)
                return (True, "Content successfully written to file")

        else:
            return (False, f"Unknown mode '{mode}'")

    except OSError as e:
        return (False, str(e))

def secure_archive(file_name: str, action: str = "read", content: str = "") -> tuple[bool, str]:
    """
    Safely accesses a file for reading or writing using a context manager.
    Returns a tuple indicating success (bool) and the data or error message (str).
    """
    try:
        # Check if the user requested a read action
        if action == "read" or action == "r":
            # The 'with' statement automatically handles opening and closing!
            with open(file_name, "r") as vault:
                data = vault.read()
                return (True, data)
                
        # Check if the user requested a write action
        elif action == "write" or action == "w":
            with open(file_name, "w") as vault:
                vault.write(content)
                return (True, "Content successfully written to file")
                
        # Handle unsupported actions gracefully
        else:
            return (False, f"Unknown action: '{action}'")

    # Catch any file system errors (like missing files or permission denials)
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file', 'read'))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('passwd', 'read'))

    print("Using 'secure_archive' to read from a regular file:")
    success, content = secure_archive('ancient_fragment.txt', 'read')
    print((success, content))

    print("Using 'secure_archive' to write previous content to a new file:")
    content_to_write = content if success else "Fallback text"
    print(secure_archive('new_vault.txt', 'write', content_to_write))


if __name__ == "__main__":
    main()
