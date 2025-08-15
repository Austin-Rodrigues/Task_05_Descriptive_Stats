# Task_05_Descriptive_Stats

## Can Large Language Models Actually Analyze Sports Statistics?
### A Study Using Syracuse Women's Lacrosse 2024 Season Data

---

## Project Background

As someone working with data analysis and curious about the capabilities of LLMs like Claude and ChatGPT, I wanted to find out: **Can these AI systems actually understand and analyze sports statistics meaningfully?** 

For this research, I chose to focus on Syracuse University Women's Lacrosse 2024 season data. Having access to comprehensive player statistics from their 16-6 season seemed like the perfect opportunity to put LLMs through their paces with real-world data analysis challenges.

## What I'm Testing

The core question driving this research is whether LLMs can move beyond simple data regurgitation to provide genuine analytical insights that would be useful to coaches, players, or fans.

### My Testing Approach
I've designed three levels of questions to progressively challenge the LLMs:

**Level 1: Basic Data Retrieval**
- "What was the team's record this season?"
- "Who scored the most goals?"
- Simple factual questions that should be easy wins

**Level 2: Analytical Calculations** 
- "Calculate shooting percentages for the top scorers"
- "Which players provide the most balanced offensive contributions?"
- Questions requiring mathematical reasoning and comparisons

**Level 3: Strategic Insights**
- "What should the coach focus on to win more games next season?"
- "Which statistical improvements would have the biggest impact?"
- Questions demanding sports knowledge and strategic thinking

## The Syracuse 2024 Dataset

**Team Performance:** 16-6 record (22 games total)  
- Home: 9-2 | Away: 5-2 | Conference: 9-1

**Key Players:**
- **Meaghan Tyrrell**: 70 goals, 32 assists (team leader in scoring)
- **Emma Ward**: 44 goals, 37 assists (team leader in assists) 
- **Olivia Adamson**: 58 goals, 25 assists
- **11 players** scored 5+ goals (showing good offensive depth)

The dataset includes complete statistics for 34 players covering goals, assists, shots, shooting percentages, and games played.

## My Testing Framework

I built a Python validation system that automatically checks LLM responses against the known correct answers. This removes human bias from accuracy assessment and ensures consistent evaluation.

### Tools Used
- **Python** for data processing and validation
- **Pandas** for statistical calculations
- **Claude Sonnet 4** as primary LLM for testing
- **Syracuse Official Statistics** as ground truth data source

## Initial Results (Part 1 - July 31, 2025)

After conducting my first round of systematic testing, here's what I discovered:

### **Perfect Performance on Basic Questions**
**Success Rate: 100% (5/5 tests)**

The LLM nailed every basic statistical question:
- Correctly identified the 16-6 season record
- Accurately named Meaghan Tyrrell as top scorer (70 goals)
- Properly calculated team totals (319 goals, 167 assists)
- Precisely identified Emma Ward as assist leader (37 assists)

### **What This Means**
LLMs excel at straightforward data retrieval when the information is clearly presented. No surprises here, but it's good to confirm the foundation is solid.

### **Next Phase Testing (August 15 Target)**
- Intermediate calculation questions
- Multi-step analytical reasoning
- Strategic coaching recommendations
- Cross-validation with other LLMs


## Key Insights So Far (Part 1)
1. **Clear Data Presentation**: LLMs handle well-formatted statistics effectively.
2. **Direct Questions**: Straightforward queries get accurate responses.
3. **Validation Framework**: Automated checking catches errors reliably.
4. No hallucination of player names or statistics encountered.

---

## Latest Findings (Part 2 – August 15, 2025)

Following the initial success in Part 1, Phase 2 testing introduced **intermediate calculations** and **complex strategic analysis**.

### **Intermediate Questions**
- **Shooting % (Top 3 Scorers)** – Correct within ±0.5% tolerance.
- **Players with ≥10 Goals** – Incorrect (8 reported vs 9 actual).

### **Complex Strategic Questions (Rubric Scored)**
| Prompt | Specificity | Actionability | Plausibility | Verdict |
|--------|-------------|---------------|--------------|---------|
| Improve 16–6 to 18–4 | 2 | 5 | 2 | Fail |
| Biggest Impact Beyond Goals | 4 | 4 | 4 | Pass |

### **Key Insights**
**Strengths:**
- Accurate numeric calculations when formulas are clear.
- Clear formatting and explanation of results.
- Actionable coaching advice in certain contexts.

**Weaknesses:**
- Occasionally misses players in threshold-based lists.
- Strategic recommendations can lack specificity or balance.

**Pattern Observed:**
- Fact-based, formula-driven prompts produce consistent accuracy.
- Open-ended strategy prompts benefit from explicit context.

---

## Updated Next Steps
- Cross-validate performance with ChatGPT and Copilot.
- Integrate defensive metrics into prompts to balance recommendations.
- Explore prompt engineering to improve specificity in strategic answers.

---

*All data sources are publicly available team statistics.*

**Contact**: arodr173@syr.edu  
**Course**: Research Methods  
**Instructor**: Dr. J. R. Strome (jrstrome@syr.edu)  
**Timeline**: July 2025 - August 2025
