import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# SIR outbreak model on a campus (assumed values, not real data).
# S = susceptible, I = infected, R = recovered/immune
# dS/dt = -beta*S*I/N
# dI/dt =  beta*S*I/N - gamma*I
# dR/dt =  gamma*I
N = 5000.0          # campus population
beta = 0.4          # contacts that spread infection per person per day
gamma = 0.1         # recovery rate per day (about 10 days infectious)
I0 = 5.0            # initial infected people
days = 100

def sir(t, y):
    S, I, R = y
    new_infections = beta * S * I / N
    return [-new_infections, new_infections - gamma * I, gamma * I]

t_eval = np.linspace(0, days, 501)
solution = solve_ivp(
    sir,
    (0, days),
    [N - I0, I0, 0.0],
    t_eval=t_eval,
    rtol=1e-9,
    atol=1e-9
)

S, I, R = solution.y
peak = np.argmax(I)

print("Solver success:", solution.success)
print(f"Basic reproduction number R0 = beta/gamma = {beta / gamma:.1f}")
print(f"Peak infected: {I[peak]:.0f} people on day {solution.t[peak]:.1f}")
print(f"Ever infected by day {days}: {R[-1] + I[-1]:.0f} of {N:.0f} ({(R[-1] + I[-1]) / N:.1%})")
print(f"Never infected: {S[-1]:.0f}")
print(f"Largest deviation of S+I+R from N: {np.max(np.abs(S + I + R - N)):.2e}")
print("Number of function evaluations:", solution.nfev)

plt.plot(solution.t, S, label="Susceptible")
plt.plot(solution.t, I, label="Infected")
plt.plot(solution.t, R, label="Recovered")
plt.xlabel("Day")
plt.ylabel("People")
plt.title("SIR outbreak on a campus")
plt.legend()
plt.grid(True)
plt.show()