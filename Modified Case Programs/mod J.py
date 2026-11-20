from scipy.optimize import root_scalar

# Effective interest rate of a mobile loan.
# Borrower asks for KES 20,000 but receives KES 19,000 (KES 1,000 fee deducted upfront)
# and repays 6 monthly instalments of KES 3,800. (assumed figures)
# Monthly rate r solves: 19000 = sum of 3800 / (1 + r)^t, t = 1..6
amount_received = 19000.0
instalment = 3800.0
months = 6

# Cash flow from the borrower's side: +received now, then -instalment each month
cash_flows = [amount_received] + [-instalment] * months

def npv(r):
    return sum(cf / (1 + r)**t for t, cf in enumerate(cash_flows))

def d_npv(r):
    return sum(-t * cf / (1 + r)**(t + 1) for t, cf in enumerate(cash_flows) if t > 0)

newton = root_scalar(npv, fprime=d_npv, x0=0.05, method="newton", xtol=1e-12)
secant = root_scalar(npv, x0=0.02, x1=0.10, method="secant", xtol=1e-12)

monthly_newton = newton.root
monthly_secant = secant.root
annual_effective = (1 + monthly_newton)**12 - 1

print(f"Monthly rate (Newton-Raphson): {monthly_newton:.6%}")
print(f"Monthly rate (Secant):         {monthly_secant:.6%}")
print(f"Effective annual rate:         {annual_effective:.2%}")
print(f"NPV at Newton solution: {npv(monthly_newton):.6f}")
print("Newton iterations:", newton.iterations, "| function calls:", newton.function_calls)
print("Secant iterations:", secant.iterations, "| function calls:", secant.function_calls)
print(f"Total repaid: KES {instalment * months:,.0f}, total cost of credit: KES {instalment * months - amount_received:,.0f}")