# e.g. delta = 0.57
# 	result = [qH1, qH2, QH, qL1, qL2, QL, Q, 2*Qbar, # 0 - 7
#               pH, pL, p_avg, p_sd, #8 - 11
#               profit1, profit2, profit1+profit2] 12 - 14

lambda_c, lambda_i = symbols('lambda_c lambda_i')
# When Collusion
qc_H_M = lambda_c*resultN_M[2].subs(lambda_c,(1-2*lambda_i)/2)
qc_L_M = lambda_c*resultN_M[5].subs(lambda_c,(1-2*lambda_i)/2)
qi_H_M = lambda_i*resultN_M[2]
qi_L_M = lambda_i*resultN_M[5]
p_H_M = resultN_M[8]
p_L_M = resultN_M[9]
profit_c_M = p_H_M+qc_H_M + p_L_M+qc_L_M
profit_i_M = p_H_M+qi_H_M + p_L_M+qi_L_M
# When i Deviates
profit_i_C = get_pH(QH)*qi_H + get_pL(QL)*qi_L
profit_i_C = profit_i_C.subs(QH, qi_H+qi_H_M+2*qc_H_M).subs(QL, qi_L+qi_L_M+2*qc_L_M)
eq_qH = solve(solve(diff(profit_i_C, qi_H), qi_H)[0] - q_H, q_H)[0]
eq_qL = solve(solve(diff(profit_i_C, qi_L), qi_L)[0] - q_L, q_L)[0]
eq_pH = get_pH(N*eq_qH)
eq_pL = get_pL(N*eq_qL)
profit_i_C = factor(eq_pH*eq_qH + eq_pL*eq_qL)