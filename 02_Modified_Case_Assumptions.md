# BIT 2118 Scientific Computing: Modified Case Assumptions

**Unit:** BIT 2118 Scientific Computing, Group Work

**Covers:** the modified real-world programs in the folder `Modified Case Programs`

---

## How to Navigate the Programs

- The modified programs are named by Part letter, A to S.
- The assignment document numbers the same work as Tasks 2 to 20, so Part A is Task 2, Part B is Task 3, and so on up to Part S, which is Task 20.
- This document explains the assumptions, input data, output and interpretation for the modified case in each part.
- The original and parameter-change programs are explained in `01_Inputs_Operations_and_Output_Meaning.md`.
- Values marked as assumptions are invented for the exercise and are not real service tariffs or measurements.

| Part | Task | Mathematical concept | Modified case |
|------|------|----------------------|---------------|
| A | 2 | NumPy Arrays and Numerical Computation | M-Pesa agent transactions |
| B | 3 | Mathematical Functions and Vectorization | M-Pesa Send Money amounts |
| C | 4 | Floating-Point Arithmetic and Numerical Errors | M-Pesa agent reconciliation |
| D | 5 | Matrix Algebra and Matrix Operations | Surveyed plot layout |
| E | 6 | Solution of Systems of Linear Equations | M-Pesa agent end-of-day totals |
| F | 7 | Gaussian Elimination and LU Decomposition | Three-loop resistor network |
| G | 8 | Iterative Methods for Linear Systems | Heat-sink plate |
| H | 9 | Eigenvalues and Eigenvectors | M-Pesa transfer network |
| I | 10 | Root Finding, Bisection and Fixed-Point Methods | M-Pesa agent break-even |
| J | 11 | Root Finding, Newton-Raphson and Secant Methods | Mobile-loan effective interest |
| K | 12 | Polynomial and Nonlinear Equation Solving | Mobile phone location |
| L | 13 | Interpolation | M-Pesa cumulative transactions |
| M | 14 | Curve Fitting and Approximation | M-Pesa agent growth |
| N | 15 | Numerical Differentiation | M-Pesa transaction rate |
| O | 16 | Numerical Integration | Cell-tower data traffic |
| P | 17 | Ordinary Differential Equations: Euler Method | Mobile-money adoption |
| Q | 18 | Numerical Solution of ODEs Using SciPy | Campus disease outbreak |
| R | 19 | Numerical Optimization | M-Pesa working-capital allocation |
| S | 20 | Random Numbers and Monte Carlo Methods | M-Pesa cash-stock risk |

---

## Part A (Task 2): NumPy Arrays and Numerical Computation

**Modified case:** M-Pesa agent transactions

**Assumptions**
- One M-Pesa agent records hourly transaction counts from 00:00 to 23:00 on a normal day.
- The transaction data is simulated rather than collected from a real agent.
- The average value of each transaction is KES 1,850.
- The agent receives commission at 0.4% of the value handled.

**Input data**
- A 24-element NumPy array containing hourly counts:
  `2, 1, 0, 1, 3, 8, 20, 45, 60, 55, 48, 52, 70, 65, 50, 46, 58, 80, 75, 40, 25, 15, 8, 4`.
- Average transaction value: KES 1,850.
- Commission rate: 0.004.

**Program output**
- Total transactions: 831.
- Mean transactions per hour: 34.62.
- Peak hour: 17:00 with 80 transactions.
- Quietest hour: 2:00 with 0 transactions.
- Total value handled: KES 1,537,350.00.
- Total commission earned: KES 6,149.40.
- Busy hours: 07:00 to 19:00, represented by array indices `[7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]`.

**Interpretation**
- The agent handles 831 transactions in a day, or about 35 per hour on average.
- Activity is highest at 17:00, with 80 transactions, and lowest at 2:00. The pattern shows a quiet overnight period, a lunch-time rise and an evening peak.
- Float and staff should be concentrated in the busy period from 07:00 to 19:00.
- The vectorized calculations apply the average value and commission rate to every hourly count at once.
- Raising the commission rate from 0.4% to 0.6% would increase commission to KES 9,224.10, which is a 50% increase.

---

## Part B (Task 3): Mathematical Functions and Vectorization

**Modified case:** M-Pesa Send Money transactions

**Assumptions**
- One million Send Money transactions are simulated.
- Amounts are uniformly distributed between KES 50 and KES 5,000.
- The platform applies an assumed flat transaction charge of 1%.
- The assumed exchange rate is KES 129 per USD.
- The charge, conversion and squared deviation calculations are repeated for every transaction.

**Input data**
- 1,000,000 amounts generated with NumPy's fixed seed 42.
- Fee rate: 0.01.
- Exchange rate: 129 KES per USD.
- The mean of all generated amounts.

**Program output**
- First five amounts: KES 3,881.08, 2,222.45, 4,300.06, 3,501.97 and 516.18.
- First five totals including the fee in USD: 30.39, 17.40, 33.67, 27.42 and 4.04.
- Total fees collected: KES 25,251,310.57.
- Variance of transaction amounts: KES² 2,041,313.27.
- Vectorized time: about 0.0100 s.
- Loop time: about 0.2227 s.
- Approximate speed-up: 22.3 times.

**Interpretation**
- The vectorized expression calculates the charge and USD value for all transactions together.
- The total charge is 1% of the total value moved, so it equals about KES 25.25 million.
- The variance shows substantial variation in transaction amounts. The standard deviation is about KES 1,429.
- The vectorized implementation is much faster than the loop, which is important for a payment platform that processes millions of transfers.
- The assumed fee applies in both the loop and vectorized calculations.
- Changing the fee rate from 1% to 0.5% would halve total fees to about KES 12.63 million. It would not change the amount variance or timing comparison.

---

## Part C (Task 4): Floating-Point Arithmetic and Numerical Errors

**Modified case:** M-Pesa agent reconciliation

**Assumptions**
- The agent records ten deposits of KES 0.10.
- The agent also accumulates 1,000,000 fee entries of KES 0.10.
- Ordinary binary floating-point numbers, integer cents and Python `Decimal` are compared.
- Financial records should not depend on the exact equality of binary floating-point sums.

**Input data**
- Ten float values of 0.10.
- 1,000,000 float values of 0.10.
- The true running total: KES 100,000.00.
- Integer cents: 10 cents for every entry.
- `Decimal("0.10")` for decimal arithmetic.

**Program output**
- Ten deposits give 0.9999999999999999 with floats.
- Exact comparison with 1.00 returns False.
- Tolerance comparison with `np.isclose()` returns True.
- The million-entry float running total is 100000.000001.
- Absolute error is about KES 0.000001.
- Relative error is about 1.333 × 10⁻¹¹.
- Integer cents return KES 100,000.0.
- `Decimal` returns exactly KES 100,000.00.

**Interpretation**
- Repeated decimal fractions can produce tiny binary round-off errors.
- An exact equality check can incorrectly reject a legitimate KES 1.00 total, while a tolerance check recognizes the small difference.
- In one million additions, the error remains tiny but still demonstrates cumulative round-off.
- Financial systems avoid this problem by storing whole cents in integers or by using decimal arithmetic.
- Using KES 0.25 deposits instead of KES 0.10 deposits would give exactly KES 2.50 for ten deposits, because 0.25 is exactly representable in binary.

---

## Part D (Task 5): Matrix Algebra and Matrix Operations

**Modified case:** rotating and scaling a surveyed plot

**Assumptions**
- A rectangular plot measures 40 m by 25 m.
- One corner is at the origin.
- The plot is enlarged by 20%, rotated by 30° to match road alignment and translated to position (100, 50) m.
- A homogeneous coordinate system is required because ordinary 2×2 matrices cannot represent translation.

**Input data**
- Plot corners:
  `(0, 0), (40, 0), (40, 25), (0, 25)`.
- Rotation angle: 30°.
- Scale factor: 1.2.
- Translation: `(100, 50)`.
- Three homogeneous matrices for translation, rotation and scaling.

**Program output**
- Transformation matrix:
  `[[1.0392, -0.6, 100], [0.6, 1.0392, 50], [0, 0, 1]]`.
- Transformed corners:
  `(100, 50), (141.569, 74), (126.569, 99.981), (85, 75.981)`.
- Area scale factor: 1.44.
- Original area: 1,000 m².
- New area: 1,440 m².
- Inverse transformation restores the original: True.

**Interpretation**
- The first corner is moved to the selected map position (100, 50).
- The operation order is scale, rotate and then translate.
- The 20% length increase produces a 44% area increase because area scales by 1.2².
- The inverse matrix returns the transformed corners to their original coordinates.
- Setting the scale factor to 1.0 would keep the area at 1,000 m² while still rotating and moving the plot.

---

## Part E (Task 6): Solution of Systems of Linear Equations

**Modified case:** M-Pesa agent end-of-day totals

**Assumptions**
- The unknowns are the numbers of deposits, withdrawals and airtime sales.
- Assumed commission values are KES 25 per deposit, KES 40 per withdrawal and KES 5 per airtime sale.
- Assumed average amounts are KES 1,500 per deposit, KES 2,000 per withdrawal and KES 100 per airtime sale.
- The end-of-day totals are 120 transactions, KES 3,000 commission and KES 158,000 value handled.

**Input data**
- Coefficient matrix:
  `[[1, 1, 1], [25, 40, 5], [1500, 2000, 100]]`.
- Right-hand side: `[120, 3000, 158000]`.
- Unknown vector: `[deposits, withdrawals, airtime sales]`.

**Program output**
- Deposits: 50.
- Withdrawals: 40.
- Airtime sales: 30.
- Verification: `[120, 3000, 158000]`.
- Residual: `[0, 0, 0]`.
- Residual norm: 0.0.
- Determinant: −11,000.

**Interpretation**
- The 50, 40 and 30 counts reproduce all three end-of-day totals.
- The non-zero determinant indicates that the equations are independent and give a unique solution.
- Two totals alone would not determine three transaction types. The value-handled equation supplies the third independent relation.
- Changing the withdrawal commission from KES 40 to KES 50 would change the coefficient matrix and the solution. The existing totals would give non-whole counts and would therefore conflict with the assumed rates.

---

## Part F (Task 7): Gaussian Elimination and LU Decomposition

**Modified case:** three-loop resistor network

**Assumptions**
- A three-loop circuit contains resistances that remain fixed across several tests.
- Battery voltages are applied at the corresponding loop locations and change between tests.
- Mesh-current directions follow one consistent convention.
- Resistances are assumed values expressed in ohms.

**Input data**
- Resistance matrix:
  `[[10, -4, 0], [-4, 12, -5], [0, -5, 9]]`.
- Voltage tests:
  `[12, 6, 0]`, `[9, 6, 3]` and `[15, 0, 5]` volts.
- Unknown vector: `[i1, i2, i3]` in amperes.

**Program output**
- Lower-triangular matrix L:
  `[[1, 0, 0], [-0.4, 1, 0], [0, -0.4808, 1]]`.
- Upper-triangular matrix U:
  `[[10, -4, 0], [0, 10.4, -5], [0, 0, 6.5962]]`.
- P @ L @ U equals R: True.
- Test 1 currents: about 1.7668, 1.4169 and 0.7872 A.
- Test 2 currents: about 1.4913, 1.4781 and 1.1545 A.
- Test 3 currents: about 1.9606, 1.1516 and 1.1953 A.
- Residual norms are of the order of 10⁻¹⁵.

**Interpretation**
- The resistance matrix is factored once, while forward and back substitution are repeated for each voltage vector.
- LU decomposition therefore avoids repeating the expensive elimination process.
- The printed Gauss elimination and LU results agree for all tests.
- Small residual norms are round-off errors rather than meaningful mismatches.
- Doubling the first voltage test to `[24, 12, 0]` would double all first-test mesh currents because the system is linear.

---

## Part G (Task 8): Iterative Methods for Linear Systems

**Modified case:** steady-state heat-sink plate

**Assumptions**
- The plate is divided into an 8 by 8 grid of interior points.
- The left edge is at 80 °C, representing a hot component.
- The top, bottom and right edges are at 25 °C.
- A point temperature equals the average of its four neighbours.
- Zero is the initial estimate for all interior temperatures.
- Jacobi and Gauss-Seidel stop at a tolerance of 10⁻⁸.

**Input data**
- Grid size: 8 × 8, giving 64 unknown temperatures.
- CPU temperature: 80 °C.
- Air temperature: 25 °C.
- Matrix A has 4 on each main diagonal and −1 for each neighbouring point.
- Boundary values are moved into the right-hand-side vector b.

**Program output**
- Number of equations: 64.
- Number of non-zero entries: 288, or 7.0% of the matrix.
- Jacobi iterations: 318.
- Gauss-Seidel iterations: 166.
- Maximum difference between Jacobi and direct solution: 1.5325 × 10⁻⁷ °C.
- Maximum difference between Gauss-Seidel and direct solution: 6.7058 × 10⁻⁸ °C.
- Hottest interior point: 67.54 °C.
- Coolest interior point: 25.75 °C.
- Temperature next to the hot edge in the middle row: 67.54 °C.
- Temperature next to the far edge in the middle row: 27.14 °C.

**Interpretation**
- The matrix is sparse because most points interact only with their four neighbours.
- Iterative methods store only the repeated stencil operations and avoid a large dense factorization.
- Gauss-Seidel converges in about half as many iterations as Jacobi for this grid.
- The hottest interior point is below the 80 °C edge because the surrounding cooler boundaries remove heat.
- The left edge stays hottest and the temperature falls toward the right and other 25 °C boundaries.
- Raising the CPU temperature from 80 °C to 120 °C would raise the hottest point to about 98.48 °C and the coolest point to about 26.30 °C.

---

## Part H (Task 9): Eigenvalues and Eigenvectors

**Modified case:** M-Pesa transfer network

**Assumptions**
- Five entities send digital payments to one another: Student, Boda rider, Mama Mboga, Shop and Agent.
- A link represents a direct transfer route.
- Each sender distributes its outgoing links evenly.
- The network follows 85% of transfer links and makes a random jump 15% of the time.
- Importance is calculated using a PageRank-style eigenvector.

**Input data**
- Student: Agent and Shop.
- Boda rider: Agent and Mama Mboga.
- Mama Mboga: Agent and Shop.
- Shop: Agent and Boda rider.
- Agent: Mama Mboga, Shop and Boda rider.
- Damping factor: 0.85.

**Program output**
- Dominant eigenvalue: 1.0.
- Agent: 0.3193.
- Shop: 0.2233.
- Boda rider: 0.2154.
- Mama Mboga: 0.2120.
- Student: 0.0300.
- Scores sum to 1.0.
- Matches power iteration: True.
- Verification error: 2.1511 × 10⁻¹⁶.

**Interpretation**
- The eigenvector gives each entity an importance score rather than simply counting direct links.
- The M-Pesa Agent is most important because several entities send money to it and it also sends to common recipients.
- The Student has the lowest score because the Student mostly sends money and receives less importance through incoming links.
- A dominant eigenvalue of 1 is expected after normalization for a probability-based transfer network.
- The eigenvector calculation agrees with repeated application of the Google matrix.

---

## Part I (Task 10): Root Finding, Bisection and Fixed-Point Methods

**Modified case:** M-Pesa agent break-even point

**Assumptions**
- Daily revenue is an assumed KES 30 commission per transaction.
- Fixed costs are KES 1,200 per day for rent and attendant wages.
- Variable handling cost is KES 8 per transaction.
- Float and queue cost is `40 × sqrt(n)` for n transactions.
- The fixed charge and sqrt term make the profit curve nonlinear.

**Input data**
- Profit function:
  `profit(n) = 30n − (1200 + 8n + 40√n)`.
- Bisection bracket: `[10, 200]`.
- Fixed-point form:
  `g(n) = (1200 + 40√n) / 22`.
- Starting fixed-point value: 100.
- Tolerance: 10⁻¹⁰.

**Program output**
- Bisection break-even: 69.7279 transactions per day.
- Fixed-point break-even: 69.7279 transactions per day.
- Bisection iterations: 41.
- Fixed-point iterations: 13.
- Profit at 69.7279 transactions: 1.65 × 10⁻⁹ KES.
- Profit at 50 transactions: −KES 382.84.
- Profit at 120 transactions: KES 1,001.82.

**Interpretation**
- The agent makes a loss below about 69.73 transactions and a profit above that count.
- Both root-finding methods obtain the same break-even point.
- Fixed-point iteration is faster for this form, but bisection is more reliable once a sign-changing bracket is known.
- The result is a threshold for planning. A normal day below the threshold is not profitable under these assumptions.

---

## Part J (Task 11): Root Finding, Newton-Raphson and Secant Methods

**Modified case:** effective interest rate of a mobile loan

**Assumptions**
- The borrower receives KES 19,000 after a KES 1,000 fee is deducted from a KES 20,000 loan.
- Six monthly instalments of KES 3,800 are repaid.
- The true monthly rate is the rate that makes the present value of instalments equal the amount received.

**Input data**
- Initial cash flow: +19,000.
- Six monthly cash flows: −3,800.
- Newton starting guess: 5%.
- Secant starting guesses: 2% and 10%.
- Tolerance: 10⁻¹².

**Program output**
- Monthly Newton-Raphson rate: 5.471793%.
- Monthly Secant rate: 5.471793%.
- Effective annual rate: 89.51%.
- NPV at the Newton solution: 0.000000.
- Newton iterations: 4.
- Secant iterations: 6.
- Total repaid: KES 22,800.
- Total cost of credit: KES 3,800.

**Interpretation**
- The NPV equation is zero at an approximately 5.47% monthly rate.
- Compound conversion gives an effective annual rate of 89.51%, which is much larger than the simple total repayment difference.
- Newton-Raphson converges in fewer iterations because it uses the exact derivative.
- Secant takes one extra iteration but needs no derivative.
- The total cost of KES 3,800 includes both the instalments paid above the received amount and the upfront fee.

---

## Part K (Task 12): Polynomial and Nonlinear Equation Solving

**Modified case:** mobile-phone location using two cell towers

**Assumptions**
- Tower 1 is at `(0, 0)` km and the phone is 5 km away.
- Tower 2 is at `(6, 2)` km and the phone is 4 km away.
- A phone position must satisfy both distance equations.
- The positions and distances are assumed values.

**Input data**
- First circle:
  `(x − 0)² + (y − 0)² = 25`.
- Second circle:
  `(x − 6)² + (y − 2)² = 16`.
- Starting guesses:
  `(3, 4)` and `(5, −2)`.

**Program output**
- Position from `(3, 4)` guess: `(2.6753, 4.2241)` km.
- Position from `(5, −2)` guess: `(4.6747, −1.7741)` km.
- Residuals are 0 or of the order of 10⁻¹⁵.
- Both positions are 5.0000 km from Tower 1 and 4.0000 km from Tower 2.
- Polynomial roots for x are 2.6753 and 4.6747.

**Interpretation**
- Two circles can intersect at two points, so two starting guesses find two possible locations.
- The nonlinear solver converged for both guesses.
- A real positioning system needs another tower or an additional constraint to choose one of the two intersections.
- The polynomial check gives the same x-coordinates as the nonlinear equations.

---

## Part L (Task 13): Interpolation

**Modified case:** M-Pesa cumulative transaction counts

**Assumptions**
- Cumulative transaction counts are recorded every two hours from 06:00 to 20:00.
- Cumulative counts cannot decrease over time.
- Three methods estimate the count at 13:00 and at times outside the first recording interval.
- Cubic spline and PCHIP extrapolation are only estimates outside the measured interval.

**Input data**
- Hours: `6, 8, 10, 12, 14, 16, 18, 20`.
- Cumulative counts: `0, 6, 28, 58, 98, 134, 170, 200`.
- Target time: 13:00.

**Program output**
- Linear estimate at 13:00: 78.00.
- Cubic-spline estimate at 13:00: 77.65.
- PCHIP estimate at 13:00: 77.55.
- Cubic-spline estimate at 07:00: 0.24.
- PCHIP estimate at 07:00: 1.82.
- PCHIP never decreases: True.
- Cubic spline never decreases: False.
- Lowest cubic-spline value: −0.68.
- PCHIP increase from 13:00 to 14:00: 20.45 transactions.

**Interpretation**
- The three methods give almost the same estimate near the 12:00 and 14:00 readings.
- Linear interpolation gives 78 because 13:00 is midway between 58 and 98.
- PCHIP is shape-preserving, so it remains consistent with a cumulative count that cannot fall.
- The cubic spline oscillates slightly and even produces a negative estimate outside the measured range, so it is less suitable for extrapolation.
- PCHIP indicates about 20.45 new transactions between 13:00 and 14:00.

---

## Part M (Task 14): Curve Fitting and Approximation

**Modified case:** M-Pesa agent network growth

**Assumptions**
- Average daily transactions per agent are observed for 12 months.
- The market has a capacity limit, so growth is expected to slow and approach saturation.
- A logistic model is therefore compared with a quadratic model.
- Month 15 is a forecast beyond the observed 12 months.

**Input data**
- Months: 1 to 12.
- Daily transactions:
  `60, 105, 170, 260, 380, 500, 620, 740, 820, 880, 915, 945`.
- Logistic parameters: capacity L, growth rate k and midpoint t0.

**Program output**
- Logistic fit: L = 978.4, k = 0.534, t0 = 5.91.
- Quadratic fit: `y = −2.052t² + 117.564t − 120.11`.
- Logistic RMSE: 3.97 transactions.
- Quadratic RMSE: 40.41 transactions.
- Logistic forecast for month 15: 970.8 transactions.
- Quadratic forecast for month 15: 1,181.7 transactions.

**Interpretation**
- The logistic curve follows the saturation pattern and has a much smaller RMSE.
- The quadratic curve turns upward and overpredicts growth in the later months.
- The estimated capacity is about 978 transactions per agent per day.
- Month 15 forecast values are estimates outside the fitting range.
- The logistic model is more suitable because it does not pass the market capacity unrealistically.

---

## Part N (Task 15): Numerical Differentiation

**Modified case:** M-Pesa transaction rate from cumulative counts

**Assumptions**
- Cumulative transaction counts are recorded once per hour from 06:00 to 20:00.
- The transaction rate is the derivative of the cumulative count.
- Counts are rounded to whole transactions.
- A logistic model is used to provide exact reference rates.

**Input data**
- Hours: 6 to 20.
- Cumulative counts generated from
  `C(t) = 2000 / (1 + exp(-0.6(t - 13)))`.
- Exact rate:
  `kC(t)(1 − C(t)/2000)`.
- Forward difference at the first hour, central differences in the middle and backward difference at the last hour.

**Program output**
- Peak estimated rate: 291 transactions per hour at 13:00.
- Estimated and exact rates include:
  - 06:00: 23.0 and 17.5.
  - 10:00: 148.5 and 146.1.
  - 12:00: 268.5 and 274.5.
  - 13:00: 291.0 and 300.0.
  - 14:00: 268.5 and 274.5.
  - 16:00: 148.5 and 146.1.
  - 20:00: 23.0 and 17.5.
- `np.gradient` agrees with the manually calculated differences.

**Interpretation**
- Differentiating cumulative counts gives the approximate number of transactions per hour.
- The estimated peak occurs at 13:00 and is close to the exact logistic peak.
- The central-difference estimate is generally more accurate than the one-sided endpoint estimates.
- At 10:00, forward and central errors decrease as the step size becomes smaller.
- With h = 0.25, the forward error is 7.9879 and the central error is 0.1472, showing that central differences are much more accurate for the same spacing.

---

## Part O (Task 16): Numerical Integration

**Modified case:** cell-tower data traffic

**Assumptions**
- Throughput is measured at a cell tower from 06:00 to 18:00.
- The smooth throughput model is
  `20 + 60 exp(-((t − 8)/2.5)²) Mbps`.
- The x variable is hours since 06:00.
- Total data equals the area under the throughput curve.
- 1 Mbps for 1 hour equals 0.45 GB.

**Input data**
- 2-hour readings: 7 points.
- 1-hour readings: 13 points.
- Adaptive quadrature over the full model.

**Program output**
- Every 2 hours:
  - Trapezoidal estimate: 225.380 GB.
  - Trapezoidal error: 0.8450 GB.
  - Simpson estimate: 224.332 GB.
  - Simpson error: 1.8933 GB.
- Every 1 hour:
  - Trapezoidal estimate: 226.005 GB.
  - Trapezoidal error: 0.2202 GB.
  - Simpson estimate: 226.213 GB.
  - Simpson error: 0.0119 GB.
- Adaptive quadrature: 226.225 GB.

**Interpretation**
- All estimates represent the total data transferred during 12 hours.
- Halving the interval greatly improves both approximations.
- With 1-hour readings, Simpson's rule is almost exact for this smooth curve.
- In the 2-hour case, Simpson's estimate is not automatically better for every model shape, so the error must be tested.
- A denser measurement schedule gives a more reliable transfer total.

---

## Part P (Task 17): Ordinary Differential Equations: Euler Method

**Modified case:** mobile-money adoption

**Assumptions**
- Active mobile-money users follow logistic growth.
- Market capacity is 40 million users.
- Annual growth rate is 35%.
- Initial active-user count is 2 million.
- The model is simulated for 20 years.

**Input data**
- ODE:
  `dN/dt = 0.35N(1 − N/40)`.
- Initial value: `N(0) = 2`.
- Euler step sizes: 4, 2, 1, 0.5 and 0.1 years.
- Exact logistic solution:
  `40 / (1 + 19exp(-0.35t))`.

**Program output**
For h = 1 year:
- Year 5: Euler 7.92 million, exact 9.30 million.
- Year 10: Euler 22.68 million, exact 25.42 million.
- Year 15: Euler 35.98 million, exact 36.37 million.
- Year 20: Euler 39.46 million, exact 39.32 million.
- Euler first passes 20 million in year 10.

For year 10:
- h = 4: Euler 10.42 million, error 8.134 million.
- h = 2: Euler 19.84 million, error 5.578 million.
- h = 1: Euler 22.68 million, error 2.742 million.
- h = 0.5: Euler 24.08 million, error 1.334 million.
- h = 0.1: Euler 25.16 million, error 0.259 million.

**Interpretation**
- Euler is inaccurate with large annual steps because it uses the growth rate at the beginning of each year.
- A smaller step improves the estimate and gives results closer to the logistic solution.
- The adoption curve accelerates in the early years and slows as it approaches 40 million users.
- Euler first predicts that 20 million users will be reached at year 10, while the exact model reaches that level slightly earlier.

---

## Part Q (Task 18): Numerical Solution of ODEs Using SciPy

**Modified case:** SIR disease model on a campus

**Assumptions**
- The campus population is 5,000.
- Five people are initially infected.
- The transmission parameter beta is 0.4 per day.
- The recovery parameter gamma is 0.1 per day.
- Recovered people remain immune.
- The solver uses 501 output points over 100 days.

**Input data**
- Susceptible initial value: 4995.
- Infected initial value: 5.
- Recovered initial value: 0.
- ODE system:
  `dS/dt = -betaSI/N`,
  `dI/dt = betaSI/N - gammaI`,
  `dR/dt = gammaI`.

**Program output**
- Solver success: True.
- Basic reproduction number R0: 4.0.
- Peak infected: 2018 people on day 27.2.
- Ever infected by day 100: 4901 people, or 98.0%.
- Never infected: 99 people.
- Largest population-conservation deviation: 2.73 × 10⁻¹².
- Number of function evaluations: 1238.

**Interpretation**
- R0 = 4 indicates that, at the start, each infected person infects many susceptible people on average.
- The infected population reaches its peak near day 27.
- Almost everyone becomes infected or remains susceptible only briefly under these assumed parameters.
- The sum S + I + R stays almost exactly 5,000, confirming that the model conserves the population.
- The final susceptible count shows that about 99 people avoid infection.

---

## Part R (Task 19): Numerical Optimization

**Modified case:** M-Pesa working-capital allocation

**Assumptions**
- An agent allocates KES 200,000 between e-float and cash.
- E-float earns KES 16 per KES 1,000 per day.
- Cash earns KES 18 per KES 1,000 per day.
- Deposit demand limits e-float to KES 125,000.
- Withdrawal demand limits cash to KES 120,000.
- At least KES 40,000 must remain as cash.

**Input data**
- Capital: KES 200,000.
- Objective in thousands:
  `profit = 16e + 18c`.
- Constraint: `e + c <= 200`.
- Bounds: `0 <= e <= 125` and `40 <= c <= 120`.
- Initial guess: 50 units of each.

**Program output**
- Optimization success: True.
- E-float: KES 80,000.
- Cash: KES 120,000.
- Capital used: KES 200,000.
- Maximum daily commission: KES 3,440.
- Brute-force search gives the same profit and allocation.

**Interpretation**
- The agent uses all available capital because unused capital earns no commission.
- Cash is more profitable per thousand shillings and reaches its maximum demand limit of KES 120,000.
- The remaining KES 80,000 is assigned to e-float.
- The SLSQP result agrees with a brute-force search in steps of KES 5,000.

---

## Part S (Task 20): Random Numbers and Monte Carlo Methods

**Modified case:** M-Pesa cash-stock risk

**Assumptions**
- The agent holds KES 120,000 in cash at the start of a day.
- The number of withdrawing customers follows a Poisson distribution with mean 50.
- Each withdrawal follows a lognormal distribution with assumed parameters mu = 7.3 and sigma = 0.8.
- The simulation represents 100,000 possible days.
- A shortage occurs when total daily demand exceeds the cash held.

**Input data**
- Seed: 42.
- Cash held: KES 120,000.
- Mean customers: 50.
- Lognormal parameters: mu = 7.3 and sigma = 0.8.
- Number of simulated days: 100,000.

**Program output**
- Average simulated withdrawals: KES 101,919.
- Estimated probability of running out: 17.83%.
- Standard error: 0.121%.
- 95% interval: 17.59% to 18.07%.
- Days short of cash: 17,829 out of 100,000.
- Cash needed to cover 95% of days: KES 136,431.
- Cash needed to cover 99% of days: KES 153,634.

**Interpretation**
- There is about an 17.83% chance that a normal simulated day will need more than KES 120,000 in cash.
- The 95% range for the risk estimate is narrow because the sample contains 100,000 days.
- KES 136,431 would cover 95% of simulated demand, while KES 153,634 would cover 99%.
- Holding only to the average would leave the agent short on many days.
- The percentage error falls approximately as 1/sqrt(N), so a much larger simulation is needed for very small gains in precision.
