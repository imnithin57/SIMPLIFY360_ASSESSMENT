def find_min_max_schedule(tasks, dependencies, durations):
    # Construct a graph (adjacency list) based on dependencies
    graph = {}
    for task, dep in dependencies:
        if task not in graph:
            graph[task] = []
        graph[task].append(dep)

    # Initialize completion days
    completion_days = [0] * len(tasks)

    # Topological ordering
    for task in tasks:
        if task in graph:
            for dep in graph[task]:
                completion_days[task] = max(completion_days[task], completion_days[dep])

    # Calculate the overall completion day
    overall_completion_day = max(completion_days)

    # Calculate latest start times
    latest_start_times = [overall_completion_day - durations[task] for task in tasks]

    # Latest time when all tasks will be completed
    latest_completion_time = max(latest_start_times)

    return overall_completion_day, latest_completion_time

# Example tasks, dependencies, and durations
tasks = [0, 1, 2, 3, 4]
dependencies = [(1, 0), (2, 0), (3, 1), (4, 2)]
durations = [3, 4, 2, 5, 3]

# Find earliest and latest completion times
earliest_time, latest_time = find_min_max_schedule(tasks, dependencies, durations)
print(f"Earliest completion time: Day {earliest_time}")
print(f"Latest completion time: Day {latest_time}")
