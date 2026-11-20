# BIT 2118 Scientific Computing: Inputs, Mathematical Operations and Meaning of Output

**Unit:** BIT 2118 Scientific Computing, Group Work

**Covers:** the original programs (folder `Original Programs`) and the parameter-change programs (folder `Parameter Change Programs`)

---

## How to Navigate the Programs

- The programs in the three folders (`Original`, `Parameter Change`, `Modified Case`) are named by Part letter, A to S.
- The assignment document numbers the same work as Tasks 2 to 20, so Part A is Task 2, Part B is Task 3, and so on up to Part S, which is Task 20.
- Each part below states the inputs (B), the mathematical operations (B), the effect of changing a parameter (C) and the meaning of the output (D). The modified real-world cases are explained in `02_Modified_Case_Assumptions.md`.
- Timing results and round-off errors are machine dependent, so another computer may print slightly different values.

| Part | Task | Mathematical concept |
|------|------|----------------------|
| A | 2 | NumPy Arrays and Numerical Computation |
| B | 3 | Mathematical Functions and Vectorization |
| C | 4 | Floating-Point Arithmetic and Numerical Errors |
| D | 5 | Matrix Algebra and Matrix Operations |
| E | 6 | Solution of Systems of Linear Equations |
| F | 7 | Gaussian Elimination and LU Decomposition |
| G | 8 | Iterative Methods for Linear Systems |
| H | 9 | Eigenvalues and Eigenvectors |
| I | 10 | Root Finding: Bisection and Fixed-Point Methods |
| J | 11 | Root Finding: Newton-Raphson and Secant Methods |
| K | 12 | Polynomial and Nonlinear Equation Solving |
| L | 13 | Interpolation |
| M | 14 | Curve Fitting and Approximation |v
| N | 15 | Numerical Differentiation |
| O | 16 | Numerical Integration |
| P | 17 | Ordinary Differential Equations: Euler Method |
| Q | 18 | Numerical Solution of ODEs Using SciPy |
| R | 19 | Numerical Optimization |
| S | 20 | Random Numbers and Monte Carlo Methods |

---

## Part A (Task 2): NumPy Arrays and Numerical Computation

**Inputs**
- A NumPy array of 24 hourly temperature readings in °C, ranging from 17.5 to 29.4.
- The constants 1.8 and 32 used in the Celsius to Fahrenheit formula.

**Mathematical operations**
- Statistics on the array: mean = (sum of the 24 readings) / 24, together with the minimum and maximum.
- Vectorized conversion F = 1.8C + 32 applied to all 24 elements at once, without a loop.

**Effect of the parameter change**
- Every reading was raised by 3 °C. The mean rose from 23.12 to 26.12 °C, the minimum from 17.5 to 20.5 °C and the maximum from 29.4 to 32.4 °C.
- The spread (maximum − minimum) stayed at 11.9 °C, because adding a constant shifts every value equally. The Fahrenheit readings rose by 3 × 1.8 = 5.4 °F.

**Meaning of the output**
- The mean of 23.12 °C is the typical temperature over the day. The minimum of 17.5 °C occurs in the early morning and the maximum of 29.4 °C around midday, which is the normal daily cycle.
- The Fahrenheit values are the same readings on another scale, for example 18.5 °C = 65.3 °F. The program draws no graph.

---

## Part B (Task 3): Mathematical Functions and Vectorization

**Inputs**
- One million random network latencies between 5 and 250 ms, generated with a fixed seed (42) so that the results repeat.
- The divisor 1000 (milliseconds to seconds) and the exponent 2 (squaring).

**Mathematical operations**
- Unit conversion seconds = latency / 1000, then squaring y = seconds², which is used in error calculations.
- The same calculation is done with a Python `for` loop and with a vectorized NumPy expression, and both are timed with `timeit`.

**Effect of the parameter change**
- The number of readings was reduced from 1,000,000 to 100,000. The loop time fell from 0.1236 s to 0.0118 s and the vectorized time from 0.0039 s to 0.0006 s.
- The speed-up dropped from 31.4 times to 20.8 times, because fixed overheads form a bigger share of the vectorized time when there are fewer elements. The first five squared values stayed the same since the seed is unchanged.

**Meaning of the output**
- Each squared value is a latency in seconds squared. For example, 0.0379 corresponds to a latency of about 0.195 s.
- The vectorized version gave the same results about 31 times faster, because NumPy runs the operation in compiled code on a block of memory, while the Python loop executes each iteration separately. The program draws no graph.

---

## Part C (Task 4): Floating-Point Arithmetic and Numerical Errors

**Inputs**
- The numbers 0.1, 0.2 and 0.3 for the equality test.
- The true value √2 and the approximation 1.414 for the error calculations.
- Small values x = 10⁻⁴, 10⁻⁸ and 10⁻¹² for the stability test.

**Mathematical operations**
- Exact comparison with `==` against a tolerance comparison with `np.isclose()`.
- Absolute error = |true − approximate| and relative error = absolute error / |true|.
- Two equivalent formulas for (√(1+x) − 1)/x: the direct form and the stable form 1/(√(1+x) + 1).

**Effect of the parameter change**
- The approximation of √2 was changed from 1.414 to 1.41421. The absolute error fell from 0.00021356 to 0.00000356 and the relative error from 0.0151% to 0.000252%, about 60 times smaller.
- The other outputs did not change, because they do not depend on the approximation.

**Meaning of the output**
- 0.1 + 0.2 gives 0.30000000000000004, so the exact comparison returns False, since 0.1 and 0.2 cannot be stored exactly in binary. `np.isclose()` accepts a very small tolerance and returns True.
- The relative error of 0.0151% is small compared with the size of √2.
- For x = 10⁻¹² the direct formula gives 0.500044450291 while the true limit is 0.5. It fails because 1 + x is rounded and √(1+x) − 1 subtracts two nearly equal numbers (catastrophic cancellation). The stable form has no subtraction and gives 0.500000000000. The program draws no graph.

---

## Part D (Task 5): Matrix Algebra and Matrix Operations

**Inputs**
- The four corners of a unit square, stored as rows [x, y].
- A rotation angle of 45° and scale factors of 2.0 (x direction) and 1.5 (y direction).

**Mathematical operations**
- Rotation matrix R = [[cos θ, −sin θ], [sin θ, cos θ]] and scaling matrix S = diag(2, 1.5).
- Matrix multiplication T = R·S, then every point is transformed with `points @ T.T`. The determinant of T is also calculated.

**Effect of the parameter change**
- The angle was changed from 45° to 90°. Corner (1, 0) now moves to (0, 2) and corner (0, 1) to (−1.5, 0).
- The determinant stays 3, because rotation changes orientation and not area. Values such as 1.22 × 10⁻¹⁶ are round-off errors and should be read as zero.

**Meaning of the output**
- The matrix [[1.414, −1.061], [1.414, 1.061]] combines a stretch (2 in x, 1.5 in y) and a 45° anticlockwise turn in one operation.
- Corner (0, 0) stays at the origin and corner (1, 0) moves to (1.414, 1.414), a point at distance 2 from the origin along 45°.
- The determinant of 3 (printed as 2.9999999999999996 because of round-off) equals 2 × 1.5, so the unit square of area 1 becomes a shape of area 3. A non-zero determinant means the matrix is invertible. The program draws no graph.

---

## Part E (Task 6): Solution of Systems of Linear Equations

**Inputs**
- Coefficient matrix A = [[4, 2], [8, 12]], giving the CPU units and memory (GB) used by one Type A and one Type B server.
- Right-hand side b = [20, 72], the total observed CPU and memory usage.

**Mathematical operations**
- The system 4x + 2y = 20 and 8x + 12y = 72 is written as Ax = b and solved with `np.linalg.solve()`.
- Verification by A @ x, and the residual b − Ax with its norm.

**Effect of the parameter change**
- The totals were changed to b = [24, 64]. The solution changed from 3 Type A and 4 Type B servers to 5 Type A and 2 Type B servers.
- Matrix A is unchanged, so the same method gives a new answer for every b. Type A is CPU-heavy, so a higher CPU-to-memory ratio in the totals means more Type A servers.

**Meaning of the output**
- The answer of 3 Type A and 4 Type B servers is the only combination that gives exactly 20 CPU units (3×4 + 4×2) and 72 GB (3×8 + 4×12).
- A @ solution reproduces [20, 72] and the residual is zero, so both equations are satisfied. The solution is unique because the determinant of A is 4×12 − 2×8 = 32, which is not zero. The program draws no graph.

---

## Part F (Task 7): Gaussian Elimination and LU Decomposition

**Inputs**
- A fixed 3×3 coefficient matrix A = [[4, −1, 0], [−1, 4, −1], [0, −1, 3]].
- Three measurement vectors b: [15, 10, 10], [16, 11, 9] and [14, 12, 11].

**Mathematical operations**
- LU decomposition with pivoting, PA = LU, done once with `lu_factor()`. This is Gaussian elimination stored as the factors L and U.
- For each b: forward substitution (Ly = Pb) and back-substitution (Ux = y) with `lu_solve()`. The residual and a comparison with `np.linalg.solve()` are also calculated.

**Effect of the parameter change**
- The first measurement vector was doubled to [30, 20, 20]. Its solution doubled from [5, 5, 5] to [10, 10, 10], because Ax = b is linear.
- The solutions for the other two vectors did not change, since the factorization of A is reused and only the first b changed.

**Meaning of the output**
- Each solution is the set of unknowns that reproduces its measurement vector. For the first set, 4(5) − 5 = 15, −5 + 4(5) − 5 = 10 and −5 + 3(5) = 10.
- Residual norms of 0 and about 10⁻¹⁵ show the answers satisfy the equations to within round-off.
- The direct solution agrees with the LU solution. LU is cheaper when the same A is used with many b vectors: factoring costs about n³ operations once, and each extra solve costs about n². The program draws no graph.

---

## Part G (Task 8): Iterative Methods for Linear Systems

**Inputs**
- A 5×5 tridiagonal matrix A (2 on the diagonal and −1 on the neighbours), representing five interior points of a rod.
- b = [100, 0, 0, 0, 20], where 100 °C and 20 °C are the left and right boundary temperatures. The starting guess is zero, the tolerance 10⁻⁸ and the maximum 500 iterations.

**Mathematical operations**
- Jacobi method: each unknown is recalculated from the previous iteration's values. Gauss-Seidel method: each unknown uses the newest values already updated in the same sweep.
- The loop stops when the largest change between successive estimates falls below the tolerance. Two print statements were added to report the number of iterations of each method.

**Effect of the parameter change**
- The tolerance was relaxed from 10⁻⁸ to 10⁻⁴ by changing the default value in each function definition. Iterations fell from 150 to 86 for Jacobi and from 75 to 43 for Gauss-Seidel.
- The temperatures are now about 0.0003 °C away from the direct solution, compared with about 10⁻⁸ °C before. A looser tolerance saves computation but accepts a larger error.

**Meaning of the output**
- The temperatures fall from 86.67 °C to 33.33 °C in equal steps of 13.33 °C, so the rod has a linear temperature profile in steady state. Both methods agree with the direct solution to about 8 decimal places.
- Graph: the vertical axis is logarithmic, and both curves are close to straight lines sloping downward, so the error shrinks by a roughly constant factor each iteration (linear convergence). Both start near 50, and the Gauss-Seidel line is steeper, ending at 75 iterations against 150 for Jacobi.
- Convergence is guaranteed because A is diagonally dominant.

---

## Part H (Task 9): Eigenvalues and Eigenvectors

**Inputs**
- A 4×4 adjacency matrix of an undirected network of nodes A, B, C and D, where 1 means two nodes are linked (A–B, A–C, B–C, B–D, C–D).

**Mathematical operations**
- Eigen-decomposition Av = λv with `np.linalg.eig()`. The largest eigenvalue is the dominant one.
- The dominant eigenvector, made positive and scaled to sum to 1, gives the importance of each node. The error ‖Av − λv‖ is calculated as a check.

**Effect of the parameter change**
- The missing link between A and D was added, so every node is linked to all the others. The dominant eigenvalue rose from 2.56 to 3.0 and all four importance scores became equal (0.25).
- The network is now perfectly symmetric, so no node is more important than another.

**Meaning of the output**
- The dominant eigenvalue of 2.5616 is the factor by which the leading pattern of the network is stretched when A is applied.
- B and C score 0.2808 and A and D score 0.2192. B and C have three links each against two for A and D, and a node is important when it is linked to important nodes. For A, (0.2808 + 0.2808)/2.5616 = 0.2192.
- The verification error is only round-off (of the order of 10⁻¹⁵ to 10⁻¹⁶, or 0.0 on some machines), so Av = λv holds. The program draws no graph.

---

## Part I (Task 10): Root Finding, Bisection and Fixed-Point Methods

**Inputs**
- The function f(T) = T − 25 − 10e^(−T/20), where f(T) = 0 is the equilibrium temperature.
- The bisection bracket [20, 40], with f(20) = −8.68 and f(40) = +13.65. The fixed-point form g(T) = 25 + 10e^(−T/20), starting at 30, and a tolerance of 10⁻¹⁰.

**Mathematical operations**
- Bisection: halve the interval repeatedly and keep the half where the sign changes.
- Fixed-point iteration: T(n+1) = g(T(n)) until successive values differ by less than 10⁻¹⁰. A print statement was added to report the bisection iterations.

**Effect of the parameter change**
- The coefficient 10 was changed to 20 in both f and g. The equilibrium rose from 27.525211 °C to 29.561521 °C.
- Bisection still took 38 iterations, because its count depends only on the bracket width and tolerance. Fixed-point rose from 13 to 17 iterations, because the slope of g near the root grew from 0.126 to 0.228.

**Meaning of the output**
- The equilibrium temperature of 27.525 °C is where heat gain equals heat loss. Both methods give the same value to six decimal places.
- Bisection always converges once a sign change is bracketed, but it is slow (38 halvings). Fixed-point converged in 13 steps because |g′| is about 0.126, well below 1. It would fail if |g′| were greater than 1.
- Graph: f(T) rises steadily from about −8.7 at 20 °C to about +13.6 at 40 °C and crosses zero once, at the dashed line at 27.53 °C. Below that temperature f is negative and above it f is positive.

---

## Part J (Task 11): Root Finding, Newton-Raphson and Secant Methods

**Inputs**
- Cash flows of −10,000 at year 0 followed by 3,000, 3,500, 4,000 and 2,500 in years 1 to 4.
- Newton starting guess 10%, secant starting guesses 5% and 20%, and a tolerance of 10⁻¹².

**Mathematical operations**
- NPV(r) = Σ cashflow(t)/(1 + r)^t. The internal rate of return (IRR) is the rate for which NPV(r) = 0.
- Newton-Raphson: r(n+1) = r(n) − NPV(r(n))/NPV′(r(n)). Secant: the derivative is replaced by the slope through the two latest points. Two print statements were added to report the iterations.

**Effect of the parameter change**
- The initial investment was raised from 10,000 to 12,000. The IRR fell from 11.54% to 3.33%.
- Newton needed 5 iterations instead of 4, and secant stayed at 7. Both methods still agree.

**Meaning of the output**
- An IRR of 11.542461% means the investment earns a return equivalent to 11.54% per year. If the required return is lower, the project is worthwhile.
- NPV of 0.000000 at the answer confirms the root.
- Newton converged in 4 steps and secant in 7. Newton uses the exact slope (quadratic convergence), while secant needs no derivative but converges slightly more slowly. The program draws no graph.

---

## Part K (Task 12): Polynomial and Nonlinear Equation Solving

**Inputs**
- The circle x² + y² = 4 and the parabola y = x² − 1, written as two residual equations.
- Two starting guesses, [1, 1] and [−1, 1].

**Mathematical operations**
- Each equation is rewritten so that its residual must equal zero, and `scipy.optimize.root` iterates until both residuals are close to zero.
- Different starting guesses lead to different intersection points.

**Effect of the parameter change**
- The circle was enlarged to x² + y² = 9. The intersections moved from (±1.517, 1.303) to (±1.836, 2.372).
- The two solutions are still mirror images, because both curves are symmetric about the y-axis.

**Meaning of the output**
- Each intersection lies on both curves. For the first, 1.5175² + 1.3028² = 4 and 1.5175² − 1 = 1.3028.
- Residuals of the order of 10⁻¹³ mean both equations are satisfied to within round-off.
- There are only two intersections. By hand, y² + y − 3 = 0, and its second root y = −2.30 would need x² to be negative, which is not real. A solver finds one root per starting guess, so several guesses are needed. The program draws no graph.

---

## Part L (Task 13): Interpolation

**Inputs**
- Seven hourly temperature readings from 08:00 to 14:00: 18.0, 20.0, 22.5, 24.0, 25.0, 25.5 and 25.0 °C.
- Target times: every 10 minutes between 08:00 and 14:00, and 10:30 for the printed estimate.

**Mathematical operations**
- Linear interpolation joins neighbouring readings with straight lines, so at 10:30 it averages 22.5 and 24.0.
- A cubic spline fits smooth cubic curves through all the readings with matching slope and curvature at each joint.

**Effect of the parameter change**
- The 12:00 reading was changed from 25.0 to 28.0 °C. The linear estimate at 10:30 stayed at 23.25 °C, but the cubic estimate moved from 23.36 to 22.99 °C.
- Linear interpolation uses only the two neighbouring readings. The spline is fitted to all the readings together, so one unusual reading changes the whole curve.

**Meaning of the output**
- At 10:30 the temperature is estimated at 23.25 °C (linear) or 23.36 °C (cubic), both between the 10:00 and 11:00 readings. The cubic value is slightly higher because the temperature is levelling off, so the curve lies above the straight line.
- Graph: the dots are the hourly measurements. The linear estimate is a chain of straight segments with corners, and the cubic spline is a smooth curve through the same dots. Both pass exactly through every measurement, which is the property of interpolation.
- Interpolation is reliable only inside the measured range (08:00 to 14:00).

---

## Part M (Task 14): Curve Fitting and Approximation

**Inputs**
- Seven measurements of concurrent users (50 to 350) and server response time in ms (82 to 305).
- A quadratic model y = ax² + bx + c with three unknown parameters.

**Mathematical operations**
- Least squares with `curve_fit`: a, b and c are chosen to minimise Σ(y − ŷ)², the sum of squared residuals.
- RMSE = √(mean of squared residuals) measures the typical error. The fitted model predicts the response at 400 users.

**Effect of the parameter change**
- The quadratic model was replaced by a straight line y = bx + c. The RMSE rose from 1.55 ms to 18.83 ms, about 12 times worse.
- The prediction at 400 users fell from 377.86 ms to 312.86 ms. The line cannot follow the upward bend, so it underestimates the delay at high load.

**Meaning of the output**
- The fitted curve y = 0.002167x² − 0.1345x + 85 shows that response time grows faster than linearly with load, and the constant 85 ms is the extrapolated delay at almost no load.
- An RMSE of 1.55 ms means the curve is typically within about 1.5 ms of the measurements. The prediction at 400 users (377.86 ms) is extrapolation beyond the measured range and is only an estimate.
- Graph: the seven dots lie almost exactly on the curve, which rises gently at first and then sharply after about 250 users. With the straight line, the dots lie above the line at both ends and below it in the middle, a pattern which shows the model shape is wrong.

---

## Part N (Task 15): Numerical Differentiation

**Inputs**
- Seven GPS samples: times 0 to 6 s at 1 s intervals and positions 0.0, 4.8, 10.2, 16.1, 22.7, 30.0 and 38.0 m.

**Mathematical operations**
- Forward difference at the first point, central difference v(i) ≈ (x(i+1) − x(i−1)) / (t(i+1) − t(i−1)) at interior points and backward difference at the last point.
- Each speed is the average rate of change over a small window, used as an estimate of the instantaneous speed.

**Effect of the parameter change**
- The position at t = 3 s was changed from 16.1 to 17.5 m (a GPS error of 1.4 m). The speed at t = 2 s rose from 5.65 to 6.35 m/s and the speed at t = 4 s fell from 6.95 to 6.25 m/s.
- The speed at t = 3 s stayed at 6.25 m/s, because a central difference does not use the middle point. The error is halved (0.7 m/s) and passes to the two neighbours, so differentiation amplifies noise.

**Meaning of the output**
- The speed rises from 4.80 m/s to 8.00 m/s over 6 seconds, so the vehicle is accelerating at roughly 0.6 to 0.7 m/s².
- The first and last values (forward and backward differences) are the least accurate, since central differences are more accurate where both neighbours exist.
- Graph: speed is plotted against time and climbs from left to right, with the steepest rise between 3 s and 5 s. In the changed run, the bad reading produces a bump at 2 s and a dip at 4 s.

---

## Part O (Task 16): Numerical Integration

**Inputs**
- Seven smart-meter power readings in kW taken every 2 hours from 0 to 12 h: 0.8, 1.0, 1.4, 1.8, 1.6, 1.2 and 0.9.

**Mathematical operations**
- Energy = ∫P dt, the area under the power curve.
- Trapezoidal rule: straight lines between readings, with the trapezoid areas added. Simpson's rule: parabolas fitted through groups of three readings. (`np.trapezoid` needs NumPy 2.0 or newer, and `np.trapz` is used on older versions.)

**Effect of the parameter change**
- The reading at 06:00 was raised from 1.8 to 2.4 kW. The trapezoidal energy rose by 1.2 kWh (15.7 to 16.9) and Simpson's by 1.6 kWh (15.8 to 17.4).
- The difference between the methods widened from 0.1 to 0.5 kWh, since a sharper peak is harder to describe with only 7 readings.

**Meaning of the output**
- The energy used in the 12 hours is about 15.7 kWh (trapezoidal) or 15.8 kWh (Simpson), an average power of about 1.3 kW.
- The two methods differ by only 0.1 kWh (under 1%). Simpson's rule is usually more accurate for smooth data, but both are approximations because the meter does not record what happens between readings. The program draws no graph.

---

## Part P (Task 17): Ordinary Differential Equations, Euler Method

**Inputs**
- Ambient temperature 25 °C, initial temperature 90 °C, cooling constant k = 0.12 per minute, step size h = 1 minute and a duration of 30 minutes.

**Mathematical operations**
- The ODE dT/dt = −k(T − T_ambient) says the object cools faster the hotter it is relative to its surroundings.
- Euler's method T(n+1) = T(n) + h·f(T(n)) is repeated 30 times, and the result is compared with the exact solution T(t) = 25 + 65e^(−0.12t).

**Effect of the parameter change**
- The step size was increased from 1 minute to 5 minutes. The final error grew from 0.372 °C to 1.510 °C, about four times larger, and the Euler value dropped to 25.27 °C against the exact 26.78 °C.
- Large steps can fail altogether: with h = 20 minutes (above 2/k = 16.7 minutes) the Euler solution oscillates and blows up to about −153 °C at 60 minutes.

**Meaning of the output**
- After 30 minutes the object has cooled from 90 °C to 26.40 °C (Euler) against 26.78 °C (exact), an error of 0.37 °C. The initial cooling rate is 0.12 × 65 = 7.8 °C per minute and it slows as the object nears room temperature.
- Euler is slightly low because each step uses the rate at the start of the step, which is a little too steep.
- Graph: both curves fall steeply and flatten towards 25 °C, which is exponential decay. The Euler markers lie just below the exact curve, and with the larger step the gap is clearly visible.

---

## Part Q (Task 18): Numerical Solution of ODEs Using SciPy

**Inputs**
- Supply voltage 5 V, resistance 1000 Ω, capacitance 0.001 F (so RC = 1 s) and an initial capacitor voltage of 0 V.
- Time span 0 to 5 s with 200 output times, and tolerances rtol = 10⁻⁹ and atol = 10⁻¹¹.

**Mathematical operations**
- The ODE dV/dt = (Vs − V)/(RC): the voltage rises quickly when the capacitor is empty and more slowly as it fills.
- `solve_ivp` integrates it with an adaptive Runge-Kutta method that chooses its own step sizes. The result is validated against V(t) = Vs(1 − e^(−t/RC)).

**Effect of the parameter change**
- The capacitance was doubled to 0.002 F, so the time constant became 2 s. The voltage at 5 s fell from 4.9663 V (99.3%) to 4.5896 V (91.8%).
- The error against the exact solution stayed near 10⁻⁹ V, because the solver tolerance sets the accuracy. A larger capacitor charges more slowly.

**Meaning of the output**
- After 5 s (five time constants) the capacitor has reached 1 − e⁻⁵ = 99.3% of the supply voltage. `Solver success: True` means the solver completed the interval within its tolerances.
- The maximum error of 9.3 × 10⁻¹⁰ V shows the numerical solution is practically the same as the exact one.
- Graph: the voltage climbs steeply from 0 V and flattens as it approaches 5 V. The solid `solve_ivp` line and the dashed exact line overlap completely. With the larger capacitor the curve rises more slowly and is still climbing at 5 s.

---

## Part R (Task 19): Numerical Optimization

**Inputs**
- Objective: cost = 12x + 18y, where x and y are the amounts of Type A and Type B capacity.
- Constraint: 100x + 170y ≥ 1000, and bounds x ≥ 0 and y ≥ 0. Starting guess [5, 3] and the SLSQP method.

**Mathematical operations**
- Constrained minimisation of a linear objective with `minimize`. The constraint function returns capacity minus 1000 and must stay at or above zero.
- An integer search over 0 to 19 of each server type finds the best whole-server plan.

**Effect of the parameter change**
- The cost of Type B was raised from 18 to 22 (in both the cost function and the integer search). The solution changed from 5.882 units of Type B to 10 units of Type A, with the cost rising from 105.88 to 120.00.
- The cost per unit of capacity is 12/100 = 0.120 for A and was 18/170 = 0.106 for B, which is now 22/170 = 0.129. The cheapest source is used exclusively, and the switch happens when B costs 20.4.

**Meaning of the output**
- The cheapest plan to reach a capacity of 1,000 uses 5.882 units of Type B and no Type A, at a cost of 105.88. Total capacity of exactly 1000 means the constraint is binding, since extra capacity only costs more.
- The best whole-server plan is 6 Type B servers (capacity 1,020, cost 108), because servers cannot be bought in fractions.
- A linear problem has its optimum at a corner of the feasible region, so the answer is all of one type. The program draws no graph.

---

## Part S (Task 20): Random Numbers and Monte Carlo Methods

**Inputs**
- Server capacity 1000 units and demand that is normally distributed with mean 850 and standard deviation 120.
- N = 100,000 simulated scenarios with a fixed seed (42).

**Mathematical operations**
- Random sampling with `rng.normal()`, then each scenario is tested against the capacity (demand > 1000).
- Overload probability = (number of overloaded scenarios) / N. A running estimate is also calculated to show convergence.

**Effect of the parameter change**
- The mean demand was raised from 850 to 900. The overload probability rose from 10.6% to 20.2%.
- An increase of 6% in average demand roughly doubles the risk, because the tail of the normal distribution above 1000 grows quickly as the mean approaches the capacity.

**Meaning of the output**
- There is about a 10.6% chance (10,616 of 100,000 scenarios) that demand exceeds the capacity. This is close to the exact value from the normal distribution (10.56%), and the small difference is sampling error of about 0.1 percentage points.
- A larger N gives a more reliable estimate, but the error falls only in proportion to 1/√N.
- Graph: the horizontal axis (number of simulations) is logarithmic. With 10 to 100 simulations the line jumps around, and as the number grows into the thousands it settles near 0.106, the final estimate.
