from crewai import Agent, Task, Crew, Process, LLM

llm=LLM(
  model="ollama/qwen2.5:3b"
)

receptionist=Agent(
  role="Receptionist",
  goal="Register patients",
  backstory="You collect patient information.",
  llm=llm,
  verbose=True
)

doctor = Agent(
 role="Doctor",
 goal="Diagnose patients",
 backstory="You are an experienced physician.",
 llm=llm,
 verbose=True
)
# -- AGENT 3: Pharmacist -----------------------------------------------
pharmacist = Agent(
 role="Pharmacist",
 goal="Suggest medicines and precautions",
 backstory="You provide prescriptions and advice.",
 llm=llm,
 verbose=True
)
# -- AGENT 4: Billing Officer --------------------------------------------
billing_officer = Agent(
 role="Billing Officer",
 goal="Generate hospital bills",
 backstory="You manage patient billing.",
 llm=llm,
 verbose=True
)

# -- TASK 1: Register the patient ------------------------------------------
registration_task = Task(
 description="""
 Patient Details:
 Name: Ravi
 Age: 35
 Symptoms:
 - Fever
 - Headache
 - Body Pain
 Register the patient.
 """,
 expected_output="Patient registration summary.",
 agent=receptionist
)

# -- TASK 2: Diagnose based on symptoms --------------------------------------
diagnosis_task = Task(
 description="Analyze symptoms and provide diagnosis.",
 expected_output="Doctor diagnosis report.",
 agent=doctor
)
# -- TASK 3: Recommend medicines ---------------------------------------------
medicine_task = Task(
 description="Suggest medicines and precautions.",
 expected_output="Prescription details.",
 agent=pharmacist
)
# -- TASK 4: Generate the bill -------------------------------------------------
billing_task = Task(
 description="Generate consultation and medicine bill.",
 expected_output="Hospital bill.",
 agent=billing_officer
)

# -- CREW: 4 agents -> 4 tasks, sequential pipeline ------------------------------
crew = Crew(
 agents=[receptionist, doctor, pharmacist, billing_officer],
 tasks=[registration_task, diagnosis_task, medicine_task, billing_task],
 process=Process.sequential,
 verbose=True
)
result = crew.kickoff()
print("\nFINAL RESULT:\n")
print(result)