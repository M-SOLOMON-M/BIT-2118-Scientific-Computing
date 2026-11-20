import numpy as np

# M-Pesa transfer network: who sends money to whom (directed links).
# Node order: 0 Student, 1 Boda rider, 2 Mama Mboga, 3 Shop, 4 Agent
names = ["Student", "Boda rider", "Mama Mboga", "Shop", "Agent"]
sends_to = {
    0: [4, 3],        # Student  -> Agent, Shop
    1: [4, 2],        # Boda     -> Agent, Mama Mboga
    2: [4, 3],        # Mama     -> Agent, Shop
    3: [4, 1],        # Shop     -> Agent, Boda
    4: [2, 3, 1],     # Agent    -> Mama Mboga, Shop, Boda
}
N = len(names)
damping = 0.85            # probability of following a transfer link

# Column-stochastic link matrix: column i spreads node i's importance equally
M = np.zeros((N, N))
for i, targets in sends_to.items():
    for j in targets:
        M[j, i] = 1.0 / len(targets)

# Google matrix: follow a link with probability d, jump to any node with 1-d
G = damping * M + (1 - damping) / N * np.ones((N, N))

eigenvalues, eigenvectors = np.linalg.eig(G)
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
v = np.real(eigenvectors[:, index])
rank = np.abs(v) / np.abs(v).sum()       # normalise so the scores sum to 1

# Check with power iteration (repeatedly applying G)
r = np.ones(N) / N
for _ in range(100):
    r = G @ r

print("Dominant eigenvalue:", round(dominant_value, 6))
print("Importance scores (PageRank-style):")
for k in np.argsort(-rank):
    print(f"  {names[k]:<11} {rank[k]:.4f}")
print("Scores sum to:", round(rank.sum(), 6))
print("Matches power iteration:", np.allclose(rank, r))
print("Verification error:", np.linalg.norm(G @ v - dominant_value * v))