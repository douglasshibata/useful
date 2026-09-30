#!/usr/bin/env python3
"""
Hash Generator Script (MD5, SHA1, SHA256, SHA512)
Provides secure hashing functionality via CLI arguments or interactive prompt.
"""

import argparse
import hashlib
import sys
from typing import Dict, Optional


# Supported hash algorithms mapped to hashlib functions
HASH_ALGORITHMS = {
    "1": ("md5", hashlib.md5),
    "2": ("sha1", hashlib.sha1),
    "3": ("sha256", hashlib.sha256),
    "4": ("sha512", hashlib.sha512),
    "md5": ("md5", hashlib.md5),
    "sha1": ("sha1", hashlib.sha1),
    "sha256": ("sha256", hashlib.sha256),
    "sha512": ("sha512", hashlib.sha512),
}

# Algorithms considered cryptographically weak for security applications
WEAK_ALGORITHMS = {"md5", "sha1"}


def generate_hash(text: str, algorithm: str = "sha256") -> str:
    """
    Generates hexadecimal hash digest for the input string using specified algorithm.

    :param text: The input string to hash.
    :param algorithm: The hash algorithm name ('md5', 'sha1', 'sha256', 'sha512').
    :return: Hexadecimal string digest of the hash.
    :raises ValueError: If an unsupported algorithm is provided.
    """
    algo_key = algorithm.lower().strip()
    if algo_key not in HASH_ALGORITHMS:
        valid_algos = ", ".join(sorted(set(v[0] for v in HASH_ALGORITHMS.values())))
        raise ValueError(f"Unsupported algorithm '{algorithm}'. Choose from: {valid_algos}")

    algo_name, hasher_func = HASH_ALGORITHMS[algo_key]
    encoded_bytes = text.encode("utf-8")
    hasher = hasher_func(encoded_bytes)
    return hasher.hexdigest()


def print_menu() -> None:
    """Prints the menu banner and choices for interactive mode."""
    print('\n \033[33m""" Programa Gerador de Hash (MD5, SHA1, SHA256, SHA512) """\033[m \n')


def interactive_mode() -> None:
    """Runs interactive command line loop for hash generation."""
    print_menu()

    try:
        string_to_hash = input("\n \033[36mDigite um texto para gerar hash:\033[m ")
    except (KeyboardInterrupt, EOFError):
        print("\nOperação cancelada pelo usuário.")
        sys.exit(0)

    while True:
        try:
            choice = input(
                "\n \033[1;35mMENU - ESCOLHA O TIPO DE HASH: \n"
                "1 - MD5 (Obs: Criptograficamente fraco)\n"
                "2 - SHA1 (Obs: Criptograficamente fraco)\n"
                "3 - SHA256 (Recomendado)\n"
                "4 - SHA512 (Recomendado)\n"
                "Digite a opção desejada (1-4): \033[m"
            ).strip()

            if choice in HASH_ALGORITHMS:
                algo_name, _ = HASH_ALGORITHMS[choice]

                # Security notice for weak algorithms
                if algo_name in WEAK_ALGORITHMS:
                    print(
                        f"\033[1;33mAviso de Segurança: O algoritmo {algo_name.upper()} é considerado "
                        f"criptograficamente fraco. Recomendado usar SHA256 ou SHA512.\033[m"
                    )

                digest = generate_hash(string_to_hash, algo_name)
                print(
                    f'\n \033[1;32mO hash {algo_name.upper()} da string \033[4m"{string_to_hash}"\033[m é: {digest}\033[m'
                )
                break
            else:
                print("\033[1;31mOpção inválida! Escolha entre 1 e 4.\033[m")
        except (KeyboardInterrupt, EOFError):
            print("\nOperação cancelada pelo usuário.")
            sys.exit(0)
        except Exception as err:
            print(f"\033[1;31mErro inesperado: {err}\033[m")
            break


def main() -> None:
    """CLI entry point for argument parsing and routing."""
    parser = argparse.ArgumentParser(
        description="Gerador de Hash MD5, SHA1, SHA256 e SHA512."
    )
    parser.add_argument(
        "-s", "--string", type=str, help="Texto a ser convertido em hash"
    )
    parser.add_argument(
        "-a",
        "--algorithm",
        type=str,
        default="sha256",
        choices=["md5", "sha1", "sha256", "sha512"],
        help="Algoritmo de hash desejado (default: sha256)",
    )

    args = parser.parse_args()

    if args.string is not None:
        if args.algorithm in WEAK_ALGORITHMS:
            print(
                f"Aviso de Segurança: O algoritmo {args.algorithm.upper()} é criptograficamente fraco.",
                file=sys.stderr,
            )
        digest = generate_hash(args.string, args.algorithm)
        print(digest)
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
