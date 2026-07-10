from crewai import Agent, Task, Crew, Process, LLM

llm=LLM(model="ollama/qwen2.5:3b")

skill_analyser=Agent(
  role="Skill Analyst",
  goal="Analyse student skills and strengths",
  backstory="You are an expert in evaluating sutdent's abilities.",
  llm=llm,
  verbose=True
)

career_advisor=Agent(
  role="Career Advisor",
  goal="Suggest suitable career paths.",
  backstory="You help students choose careers.",
  llm=llm,
  verbose=True
)

# -- AGENT 3: Learning Mentor -----------------------------------------
learning_mentor = Agent(
 role="Learning Mentor",
 goal="Create a learning roadmap",
 backstory="You design study plans and learning paths.",
 llm=llm,
 verbose=True
)

# -- TASK 1: Analyze the student's profile -----------------------------
# give description and also expected output
analysis_task = Task(
 description="""
 Student Details:
 Skills:
 - Python
 - SQL
 - Communication
 Interests:
 - Artificial Intelligence
 - Data Science
 Analyze strengths and weaknesses.
 """,
 expected_output="Detailed skill analysis.",
 agent=skill_analyser
)

# -- TASK 2: Recommend careers (uses Task 1's context) -------------------
career_task = Task(
 description="""
 Based on the student's skills and interests,
 recommend suitable career options.
 """,
 expected_output="List of career recommendations.",
 agent=career_advisor
)

# -- TASK 3: Build a learning roadmap (uses Task 1 & 2 context) ----------
roadmap_task = Task(
 description="""
 Create a 6-month roadmap for the student
 to become job-ready.
 """,
 expected_output="Detailed learning roadmap.",
 agent=learning_mentor
)

crew = Crew(
 agents=[skill_analyser, career_advisor, learning_mentor],
 tasks=[analysis_task, career_task, roadmap_task],
 process=Process.sequential,
 verbose=True
)
result = crew.kickoff()
print("\nFINAL RESULT:\n")
print(result)
