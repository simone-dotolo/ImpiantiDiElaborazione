def MeanValueAnalysis(flow_ratios, mean_service_times, n_users):
    
    n_subsystems = len(flow_ratios)

    if(n_users == 0):
        mean_response_times = [0 for i in range(n_subsystems)]
        mean_jobs = [0 for i in range(n_subsystems)]
        mean_arrival_rates = [0 for i in range(n_subsystems)]
    else:
        previous_mean_jobs = MeanValueAnalysis(flow_ratios, mean_service_times, n_users-1)[1]
        mean_response_times = [(1 + previous_mean_jobs[i]) * mean_service_times[i] for i in range(n_subsystems)]
        mean_jobs = [n_users * flow_ratios[i] * mean_response_times[i] / sum([flow_ratios[j] * mean_response_times[j] for j in range(n_subsystems)]) for i in range(n_subsystems)]
        mean_arrival_rates = [mean_jobs[i] / mean_response_times[i] for i in range(n_subsystems)]

    return mean_response_times, mean_jobs, mean_arrival_rates

flow_ratios = [3, 1]
mean_service_times = [1/5, 1/2]
n_users = 100

mean_response_times, mean_jobs, mean_arrival_rates = MeanValueAnalysis(flow_ratios, mean_service_times, n_users)

print('------------------- DATA -------------------')
print(f'Number of users: {n_users}')
print(f'Number of subsystems: {len(flow_ratios)}')
print(f'Flow ratios per subsystem: {flow_ratios}')
print(f'Mean service time per subsystem: {mean_service_times}')

print('\n------------------- RESULTS -------------------')
print(f'Mean response time per subsystem: {mean_response_times}')
print(f'Mean number of jobs per subsystem: {mean_jobs}')
print(f'Mean arrival rates per subsystem: {mean_arrival_rates}')