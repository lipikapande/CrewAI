from crewai import LLM, Agent, Task, Crew, Process

llm=LLM(model="ollama/qwen2.5:3b")

#we give an agent its role, goal, backstory and llm to be used
travel_researcher=Agent(
  role="Travel Researcher",
  goal="Find the best tourist attraction in Goa",
  backstory="You are an experienced travel expert.",
  llm=llm,
  verbose=True
)

research_task= Task(
  description="""
Find 5 popular tourist places in Goa.
Mention why tourists visit them.
""",
expected_output="List of 5 tourist attractions with explanations.",
agent=travel_researcher
)

#we create a crew, and explain the agents+tasks
crew=Crew(
  agents=[travel_researcher],
  tasks=[research_task],
  process=Process.sequential,
  verbose=True
)

result=crew.kickoff()

print("\nFINAL RESULT:\n")
print(result)