
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def cost_benefit_analysis(C_disposable, C_operation, C_cleaning, initial_cost, D, cluster_size, weeks_in_month=4.33, month=6):
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    
    data = []
    for idx, M in enumerate(cluster_size):
        for r in np.arange(0.1, 1.1, 0.1):
            # 회수된 컵 수
            N_reusable = D * r * M
            
            # 변동 비용 (Variable cost)
            variable_monthly_cost = C_cleaning * N_reusable
            
            # 고정 비용 (Fixed monthly cost)
            fixed_monthly_cost = C_operation * weeks_in_month / M
            
            # 총 월 비용 (Total monthly cost)
            total_monthly_cost = variable_monthly_cost + fixed_monthly_cost
            
            # 6개월 동안의 총 비용
            total_cost_for_period = initial_cost + total_monthly_cost * month
            
            # 일회용 컵 비용 (6개월 기준)
            single_use_monthly_cost = C_disposable * D * 30 * month  # 일회용 컵 비용
            
            # 이익 계산 (Benefit)
            benefit = single_use_monthly_cost - total_cost_for_period
            
            # Store results for each recovery rate
            data.append([r, total_cost_for_period, single_use_monthly_cost, benefit])
    
        # Convert to DataFrame for plotting
        df_temp = pd.DataFrame(data, columns=['Recovery Rate', 'Total Cost (₩)', 'Single-use Cup Cost (₩)', 'Benefit (₩)'])
        
        # Plotting on subplots
        ax = axs[idx // 2, idx % 2]  # Determine the subplot position
        ax.plot(df_temp['Recovery Rate'], df_temp['Total Cost (₩)'], marker='o', label=f'Total Cost for 1 year (₩)')
        ax.plot(df_temp['Recovery Rate'], df_temp['Single-use Cup Cost (₩)'], marker='o', label=f'Single-use Cup Cost for 1 year (₩)')
        ax.plot(df_temp['Recovery Rate'], df_temp['Benefit (₩)'], marker='o', label=f'Benefit for 1 year (₩)')
        
        ax.set_title(f'Cluster Size: {M}')
        ax.set_xlabel('Recovery Rate')
        ax.set_ylabel('Cost / Benefit (₩)')
        ax.grid(True)
        ax.legend()

    # Adjust layout
    plt.tight_layout()
    plt.show()
