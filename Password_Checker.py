{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "import re\n",
        "\n",
        "def check_password_strength(password):\n",
        "    score = 0\n",
        "    suggestions = []\n",
        "\n",
        "    # Length check\n",
        "    if len(password) >= 8:\n",
        "        score += 1\n",
        "    else:\n",
        "        suggestions.append(\"Use at least 8 characters\")\n",
        "\n",
        "    # Uppercase check\n",
        "    if re.search(r\"[A-Z]\", password):\n",
        "        score += 1\n",
        "    else:\n",
        "        suggestions.append(\"Add uppercase letters\")\n",
        "\n",
        "    # Lowercase check\n",
        "    if re.search(r\"[a-z]\", password):\n",
        "        score += 1\n",
        "    else:\n",
        "        suggestions.append(\"Add lowercase letters\")\n",
        "\n",
        "    # Digit check\n",
        "    if re.search(r\"\\d\", password):\n",
        "        score += 1\n",
        "    else:\n",
        "        suggestions.append(\"Include numbers\")\n",
        "\n",
        "    # Special character check\n",
        "    if re.search(r\"[!@#$%^&*(),.?\\\":{}|<>]\", password):\n",
        "        score += 1\n",
        "    else:\n",
        "        suggestions.append(\"Add special characters\")\n",
        "\n",
        "    # Strength result\n",
        "    if score <= 2:\n",
        "        strength = \"Weak ❌\"\n",
        "    elif score == 3 or score == 4:\n",
        "        strength = \"Medium ⚠️\"\n",
        "    else:\n",
        "        strength = \"Strong ✅\"\n",
        "\n",
        "    return strength, suggestions\n",
        "\n",
        "\n",
        "# Main program\n",
        "password = input(\"Enter your password: \")\n",
        "\n",
        "strength, suggestions = check_password_strength(password)\n",
        "\n",
        "print(\"\\nPassword Strength:\", strength)\n",
        "\n",
        "if suggestions:\n",
        "    print(\"Suggestions to improve:\")\n",
        "    for s in suggestions:\n",
        "        print(\"-\", s)\n",
        "else:\n",
        "    print(\"Your password is secure!\")"
      ],
      "metadata": {
        "id": "KUwGmBFh9b4U",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c5d398c1-d2af-4d2e-9d31-0e62e15d7eb8"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your password: asjug8279hFo\n",
            "\n",
            "Password Strength: Medium ⚠️\n",
            "Suggestions to improve:\n",
            "- Add special characters\n"
          ]
        }
      ]
    }
  ]
}
