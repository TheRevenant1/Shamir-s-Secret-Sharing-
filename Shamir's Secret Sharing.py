import random
import sympy

def generate_shares(secret, total_shares, threshold, coefficients):
    poly = [secret] + coefficients[:threshold-1]
    
    # Generate the shares
    shares = []
    for i in range(1, total_shares + 1):
        share_value = sum([coeff * (i ** power) for power, coeff in enumerate(poly)])
        shares.append((i, share_value))
    
    return shares

def reconstruct_secret(shares, threshold):
    x_values, y_values = zip(*shares)
    secret = sum([y * sympy.prod([(x_values[j] / (x_values[j] - x_values[i])) for j in range(threshold) if i != j]) for i, y in enumerate(y_values)])
    return int(secret)

def main():
    secret = int(input("Enter the secret (S): "))
    total_shares = int(input("Enter the total number of shares (N): "))

    coefficients = [int(input(f"Enter coefficient a{i}: ")) for i in range(2)]

    shares = generate_shares(secret, total_shares, 3, coefficients)
    print("Shares:", shares)
    selected_shares = []
    for i in range(3):
        share_num = int(input(f"Enter the number of share {i+1} to use for reconstruction: "))
        selected_shares.append(shares[share_num - 1])

    reconstructed_secret = reconstruct_secret(selected_shares, 3)
    print("Reconstructed Secret:", reconstructed_secret)

if __name__ == "__main__":
    main()
