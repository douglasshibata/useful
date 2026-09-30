import hashlib
import os
import subprocess
import sys
import unittest
from io import StringIO
from unittest.mock import patch

# Ensure Scripts directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Scripts")))

from generateMD5_SHA1_SHA256_SHA512_WithPython import generate_hash, main


class TestHashGenerator(unittest.TestCase):

    def test_generate_hash_md5(self):
        text = "test string"
        expected = hashlib.md5(text.encode("utf-8")).hexdigest()
        self.assertEqual(generate_hash(text, "md5"), expected)
        self.assertEqual(generate_hash(text, "1"), expected)

    def test_generate_hash_sha1(self):
        text = "test string"
        expected = hashlib.sha1(text.encode("utf-8")).hexdigest()
        self.assertEqual(generate_hash(text, "sha1"), expected)
        self.assertEqual(generate_hash(text, "2"), expected)

    def test_generate_hash_sha256(self):
        text = "test string"
        expected = hashlib.sha256(text.encode("utf-8")).hexdigest()
        self.assertEqual(generate_hash(text, "sha256"), expected)
        self.assertEqual(generate_hash(text, "3"), expected)

    def test_generate_hash_sha512(self):
        text = "test string"
        expected = hashlib.sha512(text.encode("utf-8")).hexdigest()
        self.assertEqual(generate_hash(text, "sha512"), expected)
        self.assertEqual(generate_hash(text, "4"), expected)

    def test_generate_hash_unsupported_algorithm(self):
        with self.assertRaises(ValueError):
            generate_hash("text", "invalid_algo")

    @patch("sys.argv", ["generateMD5_SHA1_SHA256_SHA512_WithPython.py", "-s", "hello", "-a", "sha256"])
    def test_cli_mode_sha256(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()
            self.assertEqual(mock_stdout.getvalue().strip(), hashlib.sha256(b"hello").hexdigest())

    @patch("sys.argv", ["generateMD5_SHA1_SHA256_SHA512_WithPython.py", "-s", "hello", "-a", "md5"])
    def test_cli_mode_weak_algorithm_warning(self):
        with patch("sys.stderr", new_callable=StringIO) as mock_stderr, patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()
            self.assertIn("Aviso de Segurança", mock_stderr.getvalue())
            self.assertEqual(mock_stdout.getvalue().strip(), hashlib.md5(b"hello").hexdigest())

    @patch("builtins.input", side_effect=["test string", "3"])
    def test_interactive_mode_valid(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            with patch("sys.argv", ["generateMD5_SHA1_SHA256_SHA512_WithPython.py"]):
                main()
                expected = hashlib.sha256(b"test string").hexdigest()
                self.assertIn(expected, mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["test string", "9", "3"])
    def test_interactive_mode_invalid_then_valid(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            with patch("sys.argv", ["generateMD5_SHA1_SHA256_SHA512_WithPython.py"]):
                main()
                self.assertIn("Opção inválida", mock_stdout.getvalue())


class TestBashScripts(unittest.TestCase):

    def test_generate_md5_sh_valid(self):
        script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Scripts", "generateMD5.sh"))
        result = subprocess.run([script_path, "hello world"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        expected = hashlib.md5(b"hello world").hexdigest()
        self.assertEqual(result.stdout.strip(), expected)

    def test_generate_md5_sh_no_arg(self):
        script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Scripts", "generateMD5.sh"))
        result = subprocess.run([script_path], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Uso:", result.stderr)


if __name__ == "__main__":
    unittest.main()
