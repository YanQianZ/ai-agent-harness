from agent.basic_agent import Agent


agent = Agent()

result = agent.run("Analyze a RNA-seq dataset")

print(result)
print(agent.history)
