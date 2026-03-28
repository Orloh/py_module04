# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_stream_management.py                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/28 22:01:22 by orhernan         #+#    #+#              #
#    Updated: 2026/03/28 22:12:41 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import sys


def get_input(prompt: str) -> str:
    """
    Read from sys.stdin if data is being piped.
    Otherwise falls back to interactive input().
    """
    if sys.stdin.isatty():
        return input(prompt)
    return sys.stdin.readline().strip()


def main() -> None:
    print("===CYBER ARCHIVES - COMMUNICATION SYSTEM===")
    print()

    archivist_id = get_input("Input Stream active. Enter archivist ID: ")
    status = get_input("Input Stream active. Enter status report: ")
    print()

    status_msg = f"[STANDARD] Archive status from {archivist_id}: {status}\n"
    alert_msg = "[ALERT] System diagnostic: Communication channels verified\n"
    complete_msg = "[STANDARD] Data transmission complete\n"

    sys.stdout.write(status_msg)
    sys.stderr.write(alert_msg)
    sys.stdout.write(complete_msg)
    print()
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
