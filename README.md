# Shamir-s-Secret-Sharing-
This code implements Shamir's Secret Sharing, a cryptographic algorithm created by Adi Shamir. It is designed to securely divide a secret into multiple parts, known as shares.

Functionality:
The user can input a secret, specify the total number of shares (total_shares), and set the threshold number of shares required to reconstruct the secret (threshold). The algorithm also allows for custom coefficients and uses a fixed key value of 3, implying a polynomial degree of K-1 (where K=3).

Features
Secure Secret Sharing:
The program divides a secret into multiple shares, ensuring that only a specified number of shares can reconstruct the original secret.
Customizable Parameters:
Users can define the total number of shares, the minimum number of shares required to reconstruct the secret, and the coefficients for the polynomial.
