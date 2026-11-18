# SE Assignments

Ishika Jain - PES2UG24AM067

Software Engineering lab submissions.

| Folder | Lab | What's inside |
|---|---|---|
| `Lab-1` | Requirements Engineering & UML Use-Case Modelling | Requirements table, use-case diagram and use-case specification for Problem Statement #61, Household Carbon Footprint & Target Tracker |
| `Lab-2` | Agile Backlog & Sprint Simulation (Jira) | Epics, user stories, story points, sprint plan, burndown charts and reflection |
| `Lab-3` | Component Modelling & Architecture Selection | Client-Server architecture justification and UML component diagram |
| `LAB6` | Code and Branch Coverage | Code coverage and branch coverage test cases for `credit_card_rewards.py`, with screenshots and report |
| `LAB7` | Fuzz Testing | Hypothesis fuzz tests, fixed `credit_card_rewards_parser.py`, screenshots SS1-SS4 and report |

`SE-Lab-Concepts_PES2UG24AM067.pdf` has notes explaining the concepts behind each lab.

## Running the tests

```
pip install pytest coverage hypothesis

cd LAB6
coverage run --branch -m pytest BranchCoverageTest_credit_card_rewards.py
coverage report -m

cd ../LAB7
pytest test_credit_card_rewards_parser.py
```
