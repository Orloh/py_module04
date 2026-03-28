# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_archive_creation.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/25 22:19:52 by orhernan         #+#    #+#              #
#    Updated: 2026/03/26 00:45:54 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


def initialize_storage_unit(vault_name: str) -> "io.TextIOWrapper":
    """
    Opens a file in write mode and returns the file object.
    Handles the intialization logging.
    """
    print(f"Initializing new storage unit: {vault_name}")
    vault = open(vault_name, "w")
    print("Storage unit created successfully...")
    print()
    return vault


def preserve_data(vault: "io.TextIOWrapper", entries: list[str]) -> None:
    """
    Writes a list of data entries into the provided file object.
    Handles the inscription logging.
    """
    print("Inscribing preservation data...")
    i = 1
    for entry in entries:
        formatted_entry: str = f"[ENTRY {i:03d}] {entry}\n"
        vault.write(formatted_entry)
        print(formatted_entry.strip())
        i += 1
    print()


def seal_storage_unit(vault: "io.TextIOWrapper") -> None:
    """
    Safely closes the file object and logs completion.
    """
    vault.close()
    print("Data inscription complete. Storage unit sealed.")
    print()


def main() -> None:
    """
    Main entry point for the Archive Creation protocol.
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    preservation_data: list[str] = [
        "New quantum algorithm discovered",
        "Efficiency increased by 346%",
        "Archived by data Archivist trainee"
    ]

    vault_name = "new_discovery.txt"
    vault = initialize_storage_unit(vault_name)
    preserve_data(vault, preservation_data)
    seal_storage_unit(vault)

    print(f"Archive '{vault_name}' ready for long-term preservation")


if __name__ == "__main__":
    main()
